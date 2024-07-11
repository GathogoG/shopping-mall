import React from 'react'

const Register = () => {
  return (
    <div>
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
        </form>
    </div>
  )
}

export default Register
