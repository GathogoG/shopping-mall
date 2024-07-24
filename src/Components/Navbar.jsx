import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import cart_icon from '../Assets/cart_icon.png';
import logo from '../Assets/logo.png';

const Navbar = () => {
  const [menu, setMenu] = useState("home");

  return (
    <div className='navbar'>
      <div className="nav-logo">
        <img src={logo} alt="logo" />
        <p>QIQA Mall</p>
      </div>

      <ul className="nav-menu">
        <li onClick={() => setMenu("home")}>
          <Link to="/">Home</Link>
          {menu === "home" ? <hr /> : <></>}
        </li>
        <li onClick={() => setMenu("shop")}>
          <Link to="/shop">Shop</Link>
          {menu === "shop" ? <hr /> : <></>}
        </li>
        <li onClick={() => setMenu("about")}>
          <Link to="/about"> About</Link>
          {menu === "about" ? <hr /> : <></>}
        </li>
        <li onClick={() => setMenu("contact")}>
          <Link to="/contact">Contact</Link>
          {menu === "contact" ? <hr /> : <></>}
        </li>
      </ul>

      <div className="nav-login-cart">
        <Link to="/login">
        <button>Login</button>
        </Link>
        {/* <Link to="/register">
        <button>Register</button>
        </Link> */}
        <Link to="/cart">
          <img src={cart_icon} alt="cart icon" />
        </Link>
        
      </div>
    </div>
  );
};

export default Navbar;
