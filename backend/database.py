from dotenv import load_dotenv
import mysql.connector
from user import User
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
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    select_query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(select_query, (email,))
    user = cursor.fetchone()

    if user:
        column_names = [column[0] for column in cursor.description]
        user_dict = {column: value for column, value in zip(column_names, user)}

        cursor.close()
        connection.close()

        # email is used for the id as it is the primary key
        return User(user_dict["email"], user_dict["name"], user_dict["email"], user_dict["password"])
    else:
        return None

def user_exists(email):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    check_query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(check_query, (email,))
    existing_user = cursor.fetchone()

    cursor.close()
    connection.close()

    return existing_user is not None

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

def add_product(sku, name, description, price, image):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    insert_query = "INSERT INTO products (sku, name, description, price, image) VALUES (%s, %s, %s, %s, %s)"
    product_data = (sku, name, description, price, image)
    cursor.execute(insert_query, product_data)
    connection.commit()
    
    cursor.close()
    connection.close()

def update_product(sku, new_name, new_description, new_price, image):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    update_query = "UPDATE products SET name = %s, description = %s, price = %s, image = %s WHERE sku = %s"
    cursor.execute(update_query, (new_name, new_description, new_price, image, current_sku))
    connection.commit()

    cursor.close()
    connection.close()

def remove_product(sku):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    update_query = "DELETE FROM products WHERE sku = %s"
    cursor.execute(update_query, (sku))
    connection.commit()

    cursor.close()
    connection.close()
