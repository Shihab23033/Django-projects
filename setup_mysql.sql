-- MySQL setup script for Django To-Do List app
CREATE DATABASE todolist_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'root'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON todolist_db.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
