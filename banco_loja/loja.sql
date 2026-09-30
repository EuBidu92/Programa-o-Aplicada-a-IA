-- =====================================================
-- BANCO DE DADOS: LOJA
-- Atividade Prática - Banco de uma Loja
-- =====================================================

-- 1. Criar o banco de dados
CREATE DATABASE loja;

-- Selecionar o banco
USE loja;


-- =====================================================
-- 2. Criar tabela de categorias
-- =====================================================

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);


-- Inserir categorias
INSERT INTO categorias (nome)
VALUES
('Informática'),
('Acessórios'),
('Eletrônicos');


-- =====================================================
-- 3. Criar tabela de produtos
-- =====================================================

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria_id INT,
    preco DECIMAL(10,2),
    estoque INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);


-- =====================================================
-- 4. Inserir produtos
-- =====================================================

INSERT INTO produtos
(nome, categoria_id, preco, estoque)
VALUES
('Notebook Lenovo', 1, 3500.00, 10),
('Mouse Logitech', 2, 80.00, 30),
('Teclado Mecânico', 2, 250.00, 15),
('Monitor LG 24', 1, 900.00, 12),
('Caixa de Som JBL', 3, 450.00, 8);


-- =====================================================
-- 5. Listar todos os produtos
-- =====================================================

SELECT * FROM produtos;


-- =====================================================
-- 6. Buscar produtos com preço maior que R$ 100
-- =====================================================

SELECT *
FROM produtos
WHERE preco > 100;


-- =====================================================
-- 7. Atualizar o preço de um produto
-- =====================================================

UPDATE produtos
SET preco = 95.00
WHERE id = 2;


-- =====================================================
-- 8. Atualizar o estoque de um produto
-- =====================================================

UPDATE produtos
SET estoque = 8
WHERE id = 1;


-- =====================================================
-- 9. Excluir um produto
-- =====================================================

-- Exemplo de exclusão:
-- DELETE FROM produtos
-- WHERE id = 5;


-- =====================================================
-- 10. Ordenar produtos pelo preço
-- =====================================================

SELECT *
FROM produtos
ORDER BY preco ASC;


-- =====================================================
-- 11. Ordenar produtos do maior para o menor preço
-- =====================================================

SELECT *
FROM produtos
ORDER BY preco DESC;


-- =====================================================
-- 12. Consultar produtos com suas categorias
-- =====================================================

SELECT
    produtos.id,
    produtos.nome,
    categorias.nome AS categoria,
    produtos.preco,
    produtos.estoque
FROM produtos
INNER JOIN categorias
    ON produtos.categoria_id = categorias.id;