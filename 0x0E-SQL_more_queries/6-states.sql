-- creates the db hbtn_usa with a table of states in it
-- with id being auto generated and is a primary key
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
  PRIMARY KEY(id), id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(256) NOT NULL);
