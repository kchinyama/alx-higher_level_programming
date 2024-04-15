-- creates taable and database to connect with previous table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	state_id INT NOT NULL,
	name VARCHAR(256)NOT NULL,
	PRIMARY KEY(id),
	FOREIGN KEY (id)
REFERENCES states(id));
