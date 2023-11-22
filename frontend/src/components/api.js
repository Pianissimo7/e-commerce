export const login = () => {
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var loginError = document.getElementById('loginError');

    var loginData = {
        email: email,
        password: password
    };
    fetch('http://localhost:5000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(loginData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Login successful');
            // TODO add a login function call
        } else {
            loginError.textContent = 'Invalid email or password';
        }
    })
    .catch(error => {
        console.error('Error during login:', error);
    });
}


export const register = () => {
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

    var userData = {
        name: name,
        email: email,
        password: password
    };

    fetch('http://localhost:5000/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Registration successful');
            
            window.location.href = 'http://your-app-url/main_page';
        } else {
            console.error('Registration error:', data.message);
        }
    })
    .catch(error => {
        console.error('Error during registration:', error);
    });
}

export const edit_profile = () => {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Assuming you are using fetch to make a POST request to your edit profile endpoint
    fetch('http://localhost:5000/edit_profile', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            name,
            email,
            password,
        }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Profile updated successfully!');
        } else {
            console.error('Profile update failed:', data.message);
        }
    })
    .catch(error => {
        console.error('Error during profile update:', error);
    });
}