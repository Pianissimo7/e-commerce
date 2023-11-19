// login.js
function login() {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var loginError = document.getElementById('loginError');

    // Create a JSON object for login data
    var loginData = {
        email: email,
        password: password
    };

    // Send the login data to the server using the Fetch API
    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        if (data.success) {
            console.log('Login successful');
            // Redirect or perform other actions for a successful login
        } else {
            loginError.textContent = 'Invalid email or password';
        }
    })
    .catch(error => {
        console.error('Error during login:', error);
    });
}