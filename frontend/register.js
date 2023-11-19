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
    fetch('http://localhost:5000/receive_data', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the server
        console.log('Server Response:', data);
    })
    .catch(error => {
        console.error('Error sending data to the server:', error);
    });
}