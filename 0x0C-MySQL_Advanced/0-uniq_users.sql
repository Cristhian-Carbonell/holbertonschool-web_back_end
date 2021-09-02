--- We are all unique!
--- SQL script that creates a table users
CREATE DATABASE IF NOT EXISTS holberton;
USE holberton;
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL,
    name VARCHAR(255),
    PRIMARY KEY (id),
    UNIQUE (email)
);
