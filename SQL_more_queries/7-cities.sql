-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT UNIQUE,
    state_id INT,
    name VARCHAR(256),
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);