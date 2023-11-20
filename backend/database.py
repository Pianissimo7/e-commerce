from dotenv import load_dotenv
import mysql.connector
import os

# Load environment variables from .env file
load_dotenv()

# DB config used for accessing the database
db_config = {
    'host': os.environ.get("HOST"),
    'user': os.environ.get("DATABASE_USERNAME"),
    'password': os.environ.get("DATABASE_PASSWORD"),
    'database': os.environ.get("DATABASE_NAME"),
}

def get_user_by_email(email):
    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Retrieve the user with the given email
    select_query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(select_query, (email,))
    user = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return user

def user_exists(email):
    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Check if the user with the given email already exists
    check_query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(check_query, (email,))
    existing_user = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return existing_user is not None

def add_user(name, email, password):

    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Insert the new user into the database
    insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    user_data = (name, email, password)
    cursor.execute(insert_query, user_data)
    connection.commit()
    
    # Close the cursor and connection
    cursor.close()
    connection.close()

def update_user(new_name, new_password, new_email, current_email):
    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Update the user's information
    update_query = "UPDATE users SET name = %s, password = %s, email = %s WHERE email = %s"
    cursor.execute(update_query, (new_name, new_password, new_email, current_email))
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()