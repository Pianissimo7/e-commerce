// register.js
function register() {
    var name = document.getElementById('name').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var repassword = document.getElementById('repassword').value;
    var passwordError = document.getElementById('passwordError');

    if (password !== repassword) {
        passwordError.textContent = 'Passwords do not match';
        return;
    } else {
        passwordError.textContent = '';
    }

    // Create a JSON object
    var userData = {
        name: name,
        email: email,
        password: password
    };

    // Send the JSON object to the server using the Fetch API
    fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        if (data.success) {
            console.log('Registration successful');
            // Redirect or perform other actions for a successful registration
        } else {
            // Display the error message
            console.error('Registration error:', data.message);
        }
    })
    .catch(error => {
        console.error('Error during registration:', error);
    });
}