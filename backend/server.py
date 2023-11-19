from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data (replace this with your user data or connect to a database)
users = []

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
    user_data = request.get_json()

    # Check if the email is already registered
    if any(user['email'] == user_data['email'] for user in users):
        return error_response('Email is already registered', 400)

    # Add the new user to the list
    users.append(user_data)

    return success_response(message='Registration successful')

# Route for handling login requests
@app.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()

    # Find the user based on the provided email
    user = next((user for user in users if user['email'] == login_data['email']), None)

    if user and user['password'] == login_data['password']:
        # Login successful
        return success_response(message='Login successful')
    else:
        # Invalid email or password
        return error_response('Invalid email or password', 401)

if __name__ == '__main__':
    app.run(debug=True)
