from dotenv import load_dotenv
import mysql.connector
from user import User
from consts import db_config

def get_user_by_email(email):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)

    select_query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(select_query, (email,))
    user = cursor.fetchone()

    cursor.close()
    connection.close()
    
    if user:
        # email is used for the id as it is the primary key
        return User(user["email"], user["name"], user["email"], user["password"])
    return None

def user_exists(email):
    return get_user_by_email(email) is not None

def add_user(name, email, password):

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    user_data = (name, email, password)
    cursor.execute(insert_query, user_data)
    connection.commit()
    
    cursor.close()
    connection.close()

def update_user(new_name, new_password, new_email, current_email):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    update_query = "UPDATE users SET name = %s, password = %s, email = %s WHERE email = %s"
    cursor.execute(update_query, (new_name, new_password, new_email, current_email))
    connection.commit()

    cursor.close()
    connection.close()