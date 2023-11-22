import './Forms.css';
import React, { Component } from 'react'
import { register } from './api.js';

class Register extends Component {
    render() {
        return (
            <form id="registrationForm">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required />

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required />

                <label for="password">Password:</label>
                <input type="password" id="password" name="password" required />

                <label for="repassword">Re-enter Password:</label>
                <input type="password" id="repassword" name="repassword" required />

                <p id="passwordError" class="error"></p>

                <button onclick={register}>Submit</button>
            </form>
        )
    }    
}

export default Register