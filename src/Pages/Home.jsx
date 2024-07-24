import React from 'react';
import "./Home.css";
import { BiCar } from "react-icons/bi";
import { BsEmojiSmile } from "react-icons/bs";
import { AiOutlineHeart } from "react-icons/ai";

export default function Home() {
  return (
    <>
      <div className="container py-5">
        <div className="text-center">
          <h1 className="display-3 welcome-heading">Welcome to Our Shopping Mall!</h1>
          <p className="lead welcome-subheading">
            Discover an amazing variety of products at unbeatable prices. Enjoy your shopping experience!
          </p>
          <h2 className="display-4">Shop More, For Less</h2>
          <p className="lead">
            We know the difference is in the details and that’s why our Online Shopping
            Mall, in the tourism and business industry, stands out for its
            quality and good taste, offering you a unique experience.
          </p>
          <p className="lead">Call Now <a href="tel:+254790909090">(07)-9090-909-0</a></p>
          <button className="btn btn-primary btn-lg">Request a Quote</button>
        </div>
      </div>

      <div className="bg-light py-5">
        <div className="container text-center">
          <h1 className="display-4">Why Choose Us</h1>
          <p className="lead">Explore our first-class goods</p>
          <div className="row justify-content-center">
            <div className="col-md-4">
              <div className="card border-0">
                <BiCar className="display-1 text-primary mb-3" />
                <h3>Variety of Goods</h3>
                <p className="lead">
                  Lorem ipsum dolor sit amet, consectadipiscing elit. Aenean commodo
                  ligula eget dolor.
                </p>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card border-0">
                <BsEmojiSmile className="display-1 text-primary mb-3" />
                <h3>Best Rate Guarantee</h3>
                <p className="lead">
                  Lorem ipsum dolor sit amet, consectadipiscing elit. Aenean commodo
                  ligula eget dolor.
                </p>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card border-0">
                <AiOutlineHeart className="display-1 text-primary mb-3" />
                <h3>Awesome Customer Support</h3>
                <p className="lead">
                  Lorem ipsum dolor sit amet, consectadipiscing elit. Aenean commodo
                  ligula eget dolor.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}
