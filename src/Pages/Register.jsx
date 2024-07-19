import React from 'react'
import './Signup.css'

const Register = () => {
  return (
    <div className='register'>
      <h1>Register</h1>
      <form id='form'>
        <div className="input-group">
        <label htmlFor="name">Name</label>
        <input  type='text' id='name' className='input'></input>
        </div>
        <div className="input-group">
        <label htmlFor="email">Email</label>
        <input  type='text' id='email' className='input'></input>
        </div>
        <div className="input-group">
        <label htmlFor="pass">Password</label>
        <input  type='password' id='pass' className='input'></input>
        </div>
        <div className="input-group">
          <button type="submit">Register</button>
        </div>
      </form>
    </div>
  )
}

export default Register
