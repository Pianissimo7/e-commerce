from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy user data (replace this with your user data or connect to a database)
users = []

# Route for handling registration requests
@app.route('/register', methods=['POST'])
def register():
    user_data = request.get_json()

    # Check if the email is already registered
    if any(user['email'] == user_data['email'] for user in users):
        return jsonify({'success': False, 'message': 'Email is already registered'})

    # Add the new user to the list
    users.append(user_data)

    return jsonify({'success': True, 'message': 'Registration successful'})

# Route for handling login requests
@app.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()

    # Find the user based on the provided email
    user = next((user for user in users if user['email'] == login_data['email']), None)

    if user and user['password'] == login_data['password']:
        # Login successful
        return jsonify({'success': True, 'message': 'Login successful'})
    else:
        # Invalid email or password
        return jsonify({'success': False, 'message': 'Invalid email or password'})

if __name__ == '__main__':
    app.run(debug=True)