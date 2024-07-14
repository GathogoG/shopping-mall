import React from 'react';

const ShoppingCart = ({ cart, removeFromCart, updateQuantity }) => {
  const handleRemove = (item) => {
    removeFromCart(item);
  };

  const handleQuantityChange = (event, item) => {
    const quantity = parseInt(event.target.value);
    updateQuantity(item, quantity);
  };

  return (
    <div className="shopping-cart">
      <h2>Shopping Cart</h2>
      {cart.length === 0 ? (
        <p>Your cart is empty</p>
      ) : (
        <ul>
          {cart.map(item => (
            <li key={item.idDrink}>
              <div className="cart-item">
                <span>{item.strDrink} - Quantity: </span>
                <input
                  type="number"
                  value={item.quantity}
                  onChange={(event) => handleQuantityChange(event, item)}
                  min="1"
                />
                <button onClick={() => handleRemove(item)}>Remove</button>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ShoppingCart;
