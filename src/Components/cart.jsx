import React, { useState, useEffect } from 'react';
import './Cart.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Elements } from '@stripe/react-stripe-js'; // Import Stripe Elements
import { loadStripe } from '@stripe/stripe-js'; // Import Stripe loader
import CheckoutForm from '../Components/Checkout';
import Modal from 'react-bootstrap/Modal';
import Button from 'react-bootstrap/Button';


const stripePromise = loadStripe('YOUR_STRIPE_PUBLIC_KEY'); // Replace with your Stripe public key

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
    return <div className="text-center">Loading...</div>;
  }

  if (error) {
    return <div className="text-center text-danger">Error: {error}</div>;
  }

  return (
    <div className="container cart-container">
      <h2 className="my-4">Cart</h2>
      {cartItems.length === 0 ? (
        <div className="text-center">Your cart is empty</div>
      ) : (
        cartItems.map(item => (
          <div key={item.id} className="d-flex align-items-center mb-3 cart-item">
            <img src={item.product.image_url} alt={item.product.name} className="cart-item-image" />
            <div className="cart-item-details ml-3">
              <h3 className="h5">{item.product.name}</h3>
              <p>Price: ${item.product.price.toFixed(2)}</p>
              <p>Quantity: {item.quantity}</p>
              <button onClick={() => handleDelete(item.id)} className="btn btn-danger">Delete</button>
            </div>
          </div>
        ))
      )}
      {cartItems.length > 0 && (
        <button onClick={handlePurchase} className="btn btn-success mt-3">Purchase</button>
      )}

      {isModalOpen && (
        <div className="modal fade show d-block" role="dialog">
          <div className="modal-dialog" role="document">
            <div className="modal-content">
              <div className="modal-header">
                <h5 className="modal-title">Payment Information</h5>
                <button type="button" className="close" onClick={() => setIsModalOpen(false)}>
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div className="modal-body">
                <p>Total Amount: ${paymentInfo.payment_amount.toFixed(2)}</p>
                <div className="form-group">
                  <label htmlFor="payment_method">Payment Method:</label>
                  <input
                    type="text"
                    id="payment_method"
                    name="payment_method"
                    className="form-control"
                    value={paymentInfo.payment_method}
                    onChange={handlePaymentChange}
                  />
                </div>
                <div className="footer">
                  <Elements stripe={stripePromise}>
                    <CheckoutForm />
                  </Elements>
                </div>
              </div>
              <div className="modal-footer">
                <button onClick={handlePaymentSubmit} className="btn btn-success">Submit Payment</button>
                <button type="button" className="btn btn-secondary" onClick={() => setIsModalOpen(false)}>Close</button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default Cart;
