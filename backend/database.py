from dotenv import load_dotenv
import mysql.connector
from user import User
from consts import db_config

class Database:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls, *args, **kwargs)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor()

    def get_user_by_id(self, id):
        select_query = "SELECT * FROM users WHERE id = %s"
        self.cursor.execute(select_query, (id,))
        user = self.cursor.fetchone()
        
        if user:
            return User(*user)
        return None

    def user_exists(self, id):
        return self.get_user_by_id(id) is not None

    def get_user_by_email_pass(self, email, password):
        select_query = "SELECT * FROM users WHERE email = %s AND password = %s"
        self.cursor.execute(select_query, (email, password))
        user = self.cursor.fetchone()

        if user:
            return User(*user)
        return None

    def user_exists(self, email, password):
        return self.get_user_by_email_pass(email, password) is not None
            
    def add_user(self, name, email, password):
        insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        user_data = (name, email, password)
        self.cursor.execute(insert_query, user_data)
        self.connection.commit()

    def update_user(self, new_name, new_password, new_email, id):
        update_query = "UPDATE users SET name = %s, password = %s, email = %s WHERE id = %s"
        self.cursor.execute(update_query, (new_name, new_password, new_email, id))
        self.connection.commit()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()
