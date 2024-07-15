import React from 'react'

const Login = () => {
  return (
    <div className='login'>
        <h1 id=''>login</h1>
      <form id='form'>
        <div class="input-group">
        <label for="name">name</label>
        <input  type='text' id='name' className='input'></input>
        </div>
        <br></br>
        <div class="input-group">
        <label for="email">email</label>
        <input  type='text' id='email' className='input'></input>
        </div>
        <br></br>
        <div class="input-group">
        <label for="pass">password</label>
        <input  type='text' id='pass' className='input'></input>
        </div>
        <div>
            <h3>don't have an account?</h3><button ><a href='./Register'>sign in</a></button>
        </div>
      </form>
    </div>
  )
}

export default Login
