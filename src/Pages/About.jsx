import React from 'react';
import PageHeader from '../Components/Pageheader';
import Selection from '../Assets/about/selection.jpg';
import Secure from '../Assets/about/transaction.png';
import Delivery from '../Assets/about/delivery.avif';
import Commerce from '../Assets/about/about.png';

const subTitle = "About Our Online Store";
const title = "Discover the Best Shopping Experience Online";
const desc = "At Shopping Mall, we are dedicated to providing you with a seamless and enjoyable shopping experience. Our mission is to offer a wide range of high-quality products, excellent customer service, and convenient shopping options.";

const year = "5+";
const experience = "Years Of Online Retail Experience";

const aboutList = [
    {
        imgUrl: Selection,
        imgAlt: 'about icon 1',
        title: 'Wide Product Selection',
        desc: 'Discover thousands of products across various categories to suit your needs.',
    },
    {
        imgUrl: Secure,
        imgAlt: 'about icon 2',
        title: 'Secure Shopping',
        desc: 'Shop with confidence knowing your transactions are secure and protected.',
    },
    {
        imgUrl: Delivery,
        imgAlt: 'about icon 3',
        title: 'Fast Delivery',
        desc: 'Enjoy speedy delivery options to get your purchases in no time.',
    },
];

const About = () => {
  return (
    <div>
        <PageHeader title={'About Our Online Store'} curPage={'About'} />
        <div className="about-section style-3 padding-tb section-bg">
            <div className="container">
                <div className="row justify-content-center row-cols-xl-2 row-cols-1 align-items-center">
                    <div className="col">
                            <div className="abs-thumb">
                                <img src= {Commerce} alt="about" />
                            </div>
                            <div className="about-left-content">
                                <h3>{year}</h3>
                                <p>{experience}</p>
                            </div>
                        </div>
                    </div>
                    <div className="col">
                        <div className="about-right">
                            <div className="section-header">
                                <span className="subtitle">{subTitle}</span>
                                <h2 className="title">{title}</h2>
                                <p>{desc}</p>
                            </div>
                            <div className="section-wrapper">
                                <ul className="lab-ul">
                                    {aboutList.map((val, i) => (
                                        <li key={i}>
                                            <div className="sr-left">
                                                <img src={val.imgUrl} alt={val.imgAlt} />
                                            </div>
                                            <div className="sr-right">
                                                <h5>{val.title}</h5>
                                                <p>{val.desc}</p>
                                            </div>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
  );
};

export default About;
