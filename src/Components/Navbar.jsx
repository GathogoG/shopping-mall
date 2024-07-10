import React, {useState} from 'react'
import cart_icon from '../Assets/cart_icon.png'
import logo from '../Assets/logo.png'

const Navbar =() => {

    const[menu,setMenu] = useState("home")
    return (
        <div className='navbar'>
         <div classNmae="nav-logo">
           <img src={logo} alt=""/>
           <p>Shopping Mall</p>
         </div>
         
         <ul className ="nav-menu">
         <li onClick={()=> {setMenu("home")}}>Home{menu==="home"?<hr/>:<></>}</li>
            <li onClick={()=> {setMenu("shop")}}>Shop{menu==="shop"?<hr/>:<></>}</li>
            <li onClick={()=> {setMenu("blog")}}>Blog{menu==="blog"?<hr/>:<></>}</li>
            <li onClick={()=>{setMenu("about")}}>About{menu==="about"?<hr/>:<></>}</li>
            <li onClick={()=>{setMenu("contact")}}>Contact{menu==="contact"?<hr/>:<></>}</li> 
         </ul>
         <div className="nav-login-cart">
            <button>Login</button>
            <button>Register</button>
            <img src={cart_icon} alt=""/>
            <div className="nav-cart-count">0</div>
         </div>
        </div>
    )
}

export default Navbar