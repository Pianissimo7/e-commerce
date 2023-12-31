from flask import Flask, request, jsonify
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required
import mysql.connector

app = Flask(__name__)
app.secret_key = 'abcdefghijklmnopqrstuvwxyz'
login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
@login_manager.user_loader
def load_user(email):

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
    if user:
        return User(user[2], *user[1:])
    return None

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Edaniel7',
    'database': 'db'
}

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

def success_response(data=None, message=None):
    response = {'success': True}
    if data is not None:
        response['data'] = data
    if message is not None:
        response['message'] = message
    return jsonify(response), 200

def error_response(message, status_code):
    return jsonify({'success': False, 'message': message}), status_code

# Route for handling registration requests
@app.route('/register', methods=['POST'])
def register():
    user_data_json = request.get_json()
    
    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Check if the user with the given email already exists
    if user_exists(user_data_json['email']):
        print(f"User with email {user_data_json['email']} already exists.")
    else:
        # Insert the new user into the database
        insert_query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
        user_data = (user_data_json['name'], user_data_json['email'], user_data_json['password'])
        cursor.execute(insert_query, user_data)
        connection.commit()
        print(f"User {user_data_json['name']} registered successfully.")

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return success_response(message='Registration successful')

# Route for handling login requests
@app.route('/login', methods=['POST'])
def login():
    
    login_data_json = request.get_json()

    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Retrieve the user with the given email
    select_query = "SELECT * FROM users WHERE email = %s"
    cursor.execute(select_query, (login_data_json['email'],))
    user = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    # Check if the user exists and the password is correct
    if user and user[3] == login_data_json['password']:
        login_user(User(user[2], *user[1:]))
        return success_response(message='Login successful')
    else:
        return error_response('Invalid email or password', 401)

@app.route('/edit_profile', methods=['POST'])
@login_required
def edit_profile():
    user_data_json = request.get_json()

    # Check if the user with the given email already exists
    if current_user.email != user_data_json['email'] and user_exists(user_data_json['email']):
        print(f"User with email {user_data_json['email']} already exists.")
        return error_response('email is already in use', 401)

    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Update the user's information
    update_query = "UPDATE users SET name = %s, password = %s WHERE email = %s"
    cursor.execute(update_query, (user_data_json['name'], user_data_json['password'], current_user.email))
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return success_response(message='Profile updated successfully')

if __name__ == '__main__':
    app.run(debug=True)
