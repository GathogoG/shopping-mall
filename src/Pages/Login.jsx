import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom'; // Import useNavigate from react-router-dom
import './Login.css'; // Import the CSS file for styling

const Login = () => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
  });
  const [message, setMessage] = useState('');
  const navigate = useNavigate(); // Initialize useNavigate

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    fetch('https://shopping-backend-wlu9.onrender.com/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(data => {
        if (data.access_token) {
          localStorage.setItem('token', data.access_token);
          setMessage(data.message); // Set the personalized welcome message
          setTimeout(() => {
            navigate('/'); // Redirect to home page after 2 seconds
          }, 2000);
        } else {
          setMessage(data.message); // Set the error message
        }
      })
      .catch(error => {
        setMessage('An error occurred. Please try again later.');
        console.error('Error:', error);
      });
  };

  return (
    <div className='auth-container'>
      <div className='auth-box'>
        <h2 className='auth-heading'>Login</h2>
        <form onSubmit={handleSubmit}>
          <div className='input-group'>
            <label htmlFor='email'>Email</label>
            <input
              type='email'
              id='email'
              name='email'
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>
          <div className='input-group'>
            <label htmlFor='password'>Password</label>
            <input
              type='password'
              id='password'
              name='password'
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>
          <button type='submit' className='submit-btn'>Login</button>
        </form>
        {message && <p className='message'>{message}</p>} {/* Display the message */}
        <p className='register-link'>
          Don't have an account? <Link to='/register'>Register here</Link>
        </p>
      </div>
    </div>
  );
};

export default Login;
