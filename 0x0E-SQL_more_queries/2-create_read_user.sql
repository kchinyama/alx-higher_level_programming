-- demo of creation of database and user
-- new user must have select priviledge only
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT, INSERT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
