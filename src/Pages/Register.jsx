import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate from react-router-dom
import './Register.css'; // Import the CSS file for styling

const Register = () => {
  const [formData, setFormData] = useState({
    username: '',
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

    fetch('https://shopping-backend-wlu9.onrender.com/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(formData),
    })
      .then(response => response.json())
      .then(data => {
        if (data.message) {
          setMessage(data.message); // Set the registration message
          setTimeout(() => {
            navigate('/login'); // Redirect to login page after 2 seconds
          }, 2000);
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
        <h2 className='auth-heading'>Register</h2>
        <form onSubmit={handleSubmit}>
          <div className='input-group'>
            <label htmlFor='username'>Username</label>
            <input
              type='text'
              id='username'
              name='username'
              value={formData.username}
              onChange={handleChange}
              required
            />
          </div>
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
          <button type='submit' className='submit-btn'>Register</button>
        </form>
        {message && <p className='message'>{message}</p>} {/* Display the message */}
      </div>
    </div>
  );
};

export default Register;
