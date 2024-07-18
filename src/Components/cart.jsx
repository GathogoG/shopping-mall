import React from 'react';
import { useLocation } from 'react-router-dom';

function Cart() {
  const location = useLocation();
  const item = location.state?.item;

  return (
    <div>
      {item ? (
        <div>
          <h2>{item.name}</h2>
          <img src={item.image_url} alt={item.description} />
          <p>{item.description}</p>
          <p>${item.price.toFixed(2)}</p>
          <p>Stock: {item.stock_quantity}</p>
        </div>
      ) : (
        <p>No item in cart.</p>
      )}
    </div>
  );
}

export default Cart;
