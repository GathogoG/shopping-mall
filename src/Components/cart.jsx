import React, { useState, useEffect } from 'react';
import './Cart.css';

function Cart() {
  const [cartItems, setCartItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [paymentInfo, setPaymentInfo] = useState({
    payment_method: '',
    payment_amount: 0,
  });

  useEffect(() => {
    fetch('https://shopping-backend-wlu9.onrender.com/cart')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        if (data && Array.isArray(data.cart_items)) {
          setCartItems(data.cart_items);
        } else {
          setError('Data is not in the expected format');
        }
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching cart items:', error);
        setError(error.message);
        setLoading(false);
      });
  }, []);

  const handlePurchase = () => {
    const totalAmount = cartItems.reduce((acc, item) => acc + item.product.price * item.quantity, 0);
    setPaymentInfo({ ...paymentInfo, payment_amount: totalAmount });
    setIsModalOpen(true);
  };

  const handlePaymentChange = (e) => {
    setPaymentInfo({ ...paymentInfo, [e.target.name]: e.target.value });
  };

  const handlePaymentSubmit = () => {
    const purchaseData = {
      cartItems,
      paymentInfo,
    };

    fetch('https://shopping-backend-wlu9.onrender.com/purchase', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(purchaseData),
    })
      .then(response => {
        if (!response.ok) {
          return response.json().then(data => {
            throw new Error(data.message || 'Failed to complete purchase');
          });
        }
        return response.json();
      })
      .then(data => {
        console.log(data.message);
        setIsModalOpen(false);
        setCartItems([]); // Clear cart items after purchase
      })
      .catch(error => {
        console.error('Error completing purchase:', error.message);
      });
  };

  const handleDelete = (cartItemId) => {
    fetch(`https://shopping-backend-wlu9.onrender.com/cart/remove/${cartItemId}`, {
      method: 'DELETE',
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to delete item');
        }
        return response.json();
      })
      .then(() => {
        setCartItems(cartItems.filter(item => item.id !== cartItemId));
      })
      .catch(error => {
        console.error('Error deleting item:', error.message);
        setError(error.message);
      });
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error}</div>;
  }

  return (
    <div className="cart-container">
      <h2>Cart</h2>
      {cartItems.length === 0 ? (
        <div>Your cart is empty</div>
      ) : (
        cartItems.map(item => (
          <div key={item.id} className="cart-item">
            <img src={item.product.image_url} alt={item.product.name} className="cart-item-image" />
            <div className="cart-item-details">
              <h3>{item.product.name}</h3>
              <p>Price: ${item.product.price.toFixed(2)}</p>
              <p>Quantity: {item.quantity}</p>
              <button onClick={() => handleDelete(item.id)} className="delete-button">Delete</button>
            </div>
          </div>
        ))
      )}
      {cartItems.length > 0 && (
        <button onClick={handlePurchase} className="purchase-button">Purchase</button>
      )}

      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <h2>Payment Information</h2>
            <p>Total Amount: ${paymentInfo.payment_amount.toFixed(2)}</p>
            <label>
              Payment Method:
              <input
                type="text"
                name="payment_method"
                value={paymentInfo.payment_method}
                onChange={handlePaymentChange}
              />
            </label>
            <button onClick={handlePaymentSubmit} className="submit-button">Submit Payment</button>
            <button onClick={() => setIsModalOpen(false)} className="close-button">Close</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Cart;
