-- Write a script that prepares a MySQL server for the project

CREATE DATABASE IF NOT EXIST hbnb_dev_db;

CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
