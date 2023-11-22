import './Forms.css';
import React, { Component } from 'react'
import { edit_profile } from './api.js';

class EditProfile extends Component {
    render() {
        return (
            <form id="editProfileForm">
                <label for="name">New Name:</label>
                <input type="text" id="name" name="name" required />

                <label for="email">New Email:</label>
                <input type="text" id="email" name="email" required />

                <label for="password">New Password:</label>
                <input type="password" id="password" name="password" />

                <button onClick={ edit_profile }>Update Profile</button>
            </form>
        )
    }    
}

export default EditProfile