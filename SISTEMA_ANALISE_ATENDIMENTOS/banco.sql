CREATE DATABASE IF NOT EXISTS atendimentos_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE atendimentos_db;

CREATE TABLE IF NOT EXISTS atendimentos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    atendente VARCHAR(100) NOT NULL,
    data_atendimento DATE NOT NULL,
    status VARCHAR(30) NOT NULL,
    descricao TEXT NULL,
    tempo_atendimento INT NULL,
    satisfacao DECIMAL(2,1) NULL
);