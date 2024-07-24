import React from 'react';
import "./Home.css";
import { BiCar } from "react-icons/bi";
import { BsEmojiSmile } from "react-icons/bs";
import { AiOutlineHeart } from "react-icons/ai";

export default function Home() {
  return (
    <div className="background-image">
      <div className="container py-5">
        <div className="text-center">
          <h1 className="display-3 welcome-heading">Welcome to QIQA Mall!</h1>
          <p className="lead welcome-subheading">
            Step into the world of QIQA Mall, where style meets elegance. Explore our exquisite collection of classic shoes that blend timeless design with modern comfort.
          </p>
          <h2 className="display-4">Elegance Redefined</h2>
          <p className="lead">
            At QIQA Mall, we pride ourselves on offering a curated selection of classic footwear that caters to your every need. From sophisticated dress shoes to comfortable casuals, our collection is crafted with the finest materials to ensure quality and style. Experience shopping like never before with our dedicated customer service and exclusive offers.
          </p>
          <p className="lead">Call Now <a href="tel:+254790909090">(07)+254748288593</a></p>
          <button className="btn btn-primary btn-lg">Request a Quote</button>
        </div>
      </div>

      <div className="bg-light py-5">
        <div className="container text-center">
          <h1 className="display-4">Why Choose Us</h1>
          <p className="lead">Discover the excellence in every step</p>
          <div className="row justify-content-center">
            <div className="col-md-4">
              <div className="card border-0">
                <BiCar className="display-1 text-primary mb-3" />
                <h3>Variety of Classic Styles</h3>
                <p className="lead">
                  Explore a diverse range of classic shoe designs that combine elegance and comfort. Whether you need a pair for a formal event or casual wear, we have something for every occasion.
                </p>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card border-0">
                <BsEmojiSmile className="display-1 text-primary mb-3" />
                <h3>Unbeatable Prices</h3>
                <p className="lead">
                  Enjoy premium quality shoes at prices that fit your budget. We offer competitive pricing without compromising on style or comfort.
                </p>
              </div>
            </div>
            <div className="col-md-4">
              <div className="card border-0">
                <AiOutlineHeart className="display-1 text-primary mb-3" />
                <h3>Exceptional Customer Service</h3>
                <p className="lead">
                  Our friendly and knowledgeable team is here to assist you every step of the way. From finding the perfect fit to handling returns, we ensure a seamless shopping experience.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
