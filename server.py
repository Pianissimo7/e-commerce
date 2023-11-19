from flask import Flask, request, jsonify
from flask_cors import CORS  # Import the CORS extension

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define a route for handling HTTP GET requests
@app.route('/hello', methods=['GET'])
def hello():
    return 'Hello, World!'

# Define a route for handling HTTP POST requests
@app.route('/receive_data', methods=['POST'])
def receive_data():
    # Access data from the request body
    data = request.get_json()
    
    # Process the data (replace this with your logic)
    processed_data = {'received_data': data['message'] + " data had been processed"}
    
    # Return a JSON response
    return jsonify(processed_data)

if __name__ == '__main__':
    # Run the Flask app on localhost and port 5000
    app.run(debug=True)