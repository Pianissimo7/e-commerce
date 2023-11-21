from dotenv import load_dotenv
import mysql.connector
from user import User
from consts import db_config

def get_user_by_id(id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    select_query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(select_query, (id,))
    user = cursor.fetchone()

    cursor.close()
    connection.close()
    
    if user:
        return User(*user)
    return None

def user_exists(id):
    return get_user_by_id(id) is not None

def get_user_by_email_pass(email, password):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    select_query = "SELECT * FROM users WHERE email = %s AND password = %s"
    cursor.execute(select_query, (email, password))
    user = cursor.fetchone()

    cursor.close()
    connection.close()
    
    if user:
        return User(*user)
    return None

def user_exists(email, password):
    
    return get_user_by_email_pass(email, password) is not None
        
def add_user(name, email, password):

    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    user_data = (name, email, password)
    cursor.execute(insert_query, user_data)
    connection.commit()
    
    cursor.close()
    connection.close()

def update_user(new_name, new_password, new_email, id):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    update_query = "UPDATE users SET name = %s, password = %s, email = %s WHERE id = %s"
    cursor.execute(update_query, (new_name, new_password, new_email, id))
    connection.commit()

    cursor.close()
    connection.close()
