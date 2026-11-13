CREATE DATABASE inglesdb;

USE inglesdb;

CREATE TABLE product (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    product_price DECIMAL,
    product_category VARCHAR(100),
    product_ratings DECIMAL,
    description VARCHAR(255),
    date DATE
)
