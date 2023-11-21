from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, login_required
import os
from dotenv import load_dotenv
from user import User
from database import *

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY")
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(email):

    user = get_user_by_email(email)
    
    return user

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

    if user_exists(user_data_json['email']):
        print(f"User with email {user_data_json['email']} already exists.")
        return error_response('Email already taken', 401)
    else:
        add_user(user_data_json['name'], user_data_json['email'], user_data_json['password'])
        print(f"User {user_data_json['name']} registered successfully.")

    return success_response(message='Registration successful')

# Route for handling login requests
@app.route('/login', methods=['POST'])
def login():
    login_data_json = request.get_json()
    user = get_user_by_email(login_data_json['email'])

    if user and user.password == login_data_json['password']:
        login_user(user)
        return success_response(message='Login successful')
    else:
        return error_response('Invalid email or password', 401)

# Route for handling edit_profile requests
@app.route('/edit_profile', methods=['POST'])
@login_required
def edit_profile():
    user_data_json = request.get_json()
    # user_data_json = request.json()

    if current_user.email != user_data_json['email'] and user_exists(user_data_json['email']):
        print(f"User with email {user_data_json['email']} already exists.")
        return error_response('email is already in use', 401)

    update_user(user_data_json['name'], user_data_json['password'], user_data_json['email'], current_user.email)

    return success_response(message='Profile updated successfully')

if __name__ == '__main__':
    app.run(debug=True)
