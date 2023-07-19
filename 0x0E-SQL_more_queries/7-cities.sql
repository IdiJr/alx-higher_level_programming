-- create a db hbtn_0d_usa and the table cities with unique id
-- as primary key and state_id as foreign key that reference id
-- from state table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
  PRIMARY KEY(id), id INT NOT NULL AUTO_INCREMENT,
  state_id INT NOT NULL,
  name VARCHAR(256) NOT NULL,
  FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id));
