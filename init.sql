CREATE DATABASE db_poo;
USE db_poo;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(255) NOT NULL
);

INSERT INTO usuarios (nombre, telefono, email)
VALUES
  ('Amit Khanna', '123456789', 'amit@example.com'),
  ('Anjali Gupta', '987654321', 'anjali@example.com');
