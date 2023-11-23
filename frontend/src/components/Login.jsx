import './Forms.css';
import React, { Component } from 'react'
import { login } from './api.js';

class Login extends Component {
    render() {
        return (
            <form id="loginForm">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required />

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required />

                <p id="loginError" className="error"></p>

                <button onClick={login}>Submit</button>
            </form>
        )
    }    
}

export default Login