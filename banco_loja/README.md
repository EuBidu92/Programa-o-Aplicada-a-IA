# Banco de Dados - Loja

Projeto desenvolvido na disciplina Introdução a Programação IA como atividade prática de Banco de Dados.

## Objetivo

Criar um banco de dados para uma loja virtual utilizando MySQL,
realizando operações de criação, inserção, consulta, atualização,
exclusão e ordenação de dados.

## Tecnologias utilizadas

- MySQL
- SQL
- Visual Studio Code
- Git
- GitHub

## Estrutura do banco

O banco de dados possui duas tabelas:

### categorias

Armazena as categorias dos produtos.

Campos:

- `id`
- `nome`

### produtos

Armazena os produtos da loja.

Campos:

- `id`
- `nome`
- `categoria_id`
- `preco`
- `estoque`

A tabela `produtos` possui uma chave estrangeira
(`categoria_id`) relacionada à tabela `categorias`.

## Operações realizadas

- Criação do banco `loja`
- Criação da tabela `categorias`
- Criação da tabela `produtos`
- Inserção de categorias
- Inserção de produtos
- Consulta de todos os produtos
- Consulta de produtos com preço superior a R$ 100
- Atualização de preço
- Atualização de estoque
- Exclusão de produto
- Ordenação por preço
- Relacionamento entre tabelas utilizando `FOREIGN KEY`
- Consulta utilizando `INNER JOIN`

## Como executar

1. Instalar o MySQL.
2. Abrir o MySQL Workbench ou outro cliente SQL.
3. Abrir o arquivo `loja.sql`.
4. Executar os comandos SQL.
5. Consultar os resultados no banco de dados.

## Relacionamento

```text
categorias
    |
    | id
    |
    |< 
produtos
    |
    | categoria_id