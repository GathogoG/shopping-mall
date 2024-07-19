import React from 'react'
import './Signup.css'

const Login = () => {
  return (
    <div className='login'>
        <h1>Login</h1>
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
          <button type="submit">Login</button>
        </div>
        <div>
            <h3>Don't have an account?</h3>
            <button><a href='./Register'>Sign Up</a></button>
        </div>
      </form>
    </div>
  )
}

export default Login
