import mysql.connector

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'prakash@kgkite2023',
    'database': 'llm'
}

# Function to establish database connection
def connect_to_database():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as error:
        print("Error connecting to the database:", error)
        return None
    
def get_user_by_email(email):
    try:
        connection = connect_to_database()
        if connection:
            with connection.cursor(dictionary=True) as cursor:
                # Execute query
                query = "SELECT * FROM users WHERE email = %s"
                cursor.execute(query, (email,))

                # Fetch user data
                user = cursor.fetchone()
                return user
        else:
            return None
    except mysql.connector.Error as error:
        # Handle database errors
        print("Error fetching user data:", error)
        return None
    finally:
        if connection:
            connection.close()


# Function to fetch teachers from the database
def get_teachers():
    try:
        connection = connect_to_database()
        if connection:
            with connection.cursor(dictionary=True) as cursor:
                # Execute query
                cursor.execute("SELECT * FROM teachers")

                # Fetch data
                teachers = cursor.fetchall()
                return teachers
        else:
            return None

    except mysql.connector.Error as error:
        # Print or log the error for debugging
        print("Error fetching data from the database:", error)
        return None

    except Exception as e:
        # Print or log other exceptions for debugging
        print("An unexpected error occurred:", e)
        return None

# Function to print list of teachers
def print_teachers(teachers):
    if teachers:
        print("List of Teachers")
        print("Name\tEmail\tDegree\tWork Experience")
        for teacher in teachers:
            print(f"{teacher['name']}\t{teacher['email']}\t{teacher['degree']}\t{teacher['work_experience']}")
    else:
        print("No teachers found in the database")

# Function to create database if not exist
def create_database():
    try:
        connection = mysql.connector.connect(host=db_config['host'], user=db_config['user'], password=db_config['password'])
        if connection:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS llm")
            print("Database created successfully!")
    except mysql.connector.Error as error:
        print("Error creating database:", error)
    finally:
        if connection:
            connection.close()

# Function to create tables if not exist
def create_tables():
    try:
        connection = connect_to_database()
        if connection:
            cursor = connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS teachers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    degree VARCHAR(100),
                    work_experience INT
                )
            """)
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS login (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(100) NOT NULL,
                    password VARCHAR(100) NOT NULL
                )
            """)
            print("Tables created successfully!")
    except mysql.connector.Error as error:
        print("Error creating tables:", error)
    finally:
        if connection:
            connection.close()

# Call the function to create the database if it doesn't exist
create_database()

# Call the function to create tables if they don't exist
create_tables()