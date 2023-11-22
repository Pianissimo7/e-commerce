import React, { useState } from 'react';
import Login from './Login'; 
import Register from './Register'; 
import EditProfile from './EditProfile'; 

const Home = () => {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentPage, setCurrentPage] = useState('home');

  const login = () => {
    setIsLoggedIn(true);
    setCurrentPage('home');
    console.log('User logged in');
  };

  const logout = () => {
    setIsLoggedIn(false);
    setCurrentPage('home');
    console.log('User logged out');
  };

  return (
    <div>
      <h1>Welcome to My App</h1>
      {isLoggedIn ? (
        <div>
          <button onClick={logout}>Logout</button>
          <button onClick={() => setCurrentPage('edit-profile')}>Edit Profile</button>
          {currentPage === 'edit-profile' && <EditProfile />}
        </div>
      ) : (
        <div>
          <button onClick={() => setCurrentPage('login')}>Login</button>
          <button onClick={() => setCurrentPage('register')}>Register</button>
          {currentPage === 'login' && <Login onLogin={login} />}
          {currentPage === 'register' && <Register />}
        </div>
      )}
    </div>
  );
};

export default Home;