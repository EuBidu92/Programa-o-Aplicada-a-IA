# API de Vendas

## Descrição

Este projeto consiste em uma API REST desenvolvida em Python utilizando **FastAPI** e **Pandas**.

A aplicação permite consultar informações de vendas armazenadas em um arquivo CSV, além de realizar análises sobre os dados, como faturamento total, quantidade de produtos vendidos e produto mais vendido.

O projeto foi desenvolvido como atividade prática do curso do SENAI, com o objetivo de aplicar conceitos de desenvolvimento de APIs, manipulação de dados com Pandas e criação de endpoints REST.

---

## Tecnologias utilizadas

* Python
* FastAPI
* Uvicorn
* Pandas
* CSV
* Swagger / OpenAPI

---

## Estrutura do projeto

```text
projeto_vendas/
│
├── main.py
├── vendas.csv
├── requirements.txt
├── README.md
└── .venv/
```

A pasta `.venv` contém o ambiente virtual utilizado durante o desenvolvimento e não é necessária para o envio do código-fonte, caso o instrutor não a solicite.

---

## Arquivo de dados

Os dados utilizados pela API estão armazenados no arquivo `vendas.csv`.

O arquivo possui as seguintes colunas:

| Campo        | Descrição                       |
| ------------ | ------------------------------- |
| `id`         | Identificador da venda          |
| `data`       | Data da venda                   |
| `produto`    | Produto vendido                 |
| `quantidade` | Quantidade de unidades vendidas |
| `preco`      | Preço unitário do produto       |
| `cliente`    | Nome do cliente                 |

---

## Instalação

É recomendado utilizar um ambiente virtual Python.

No PowerShell, dentro da pasta do projeto:

```powershell
python -m venv .venv
```

Ative o ambiente virtual:

```powershell
.\.venv\Scripts\Activate.ps1
```

Caso o PowerShell bloqueie a ativação do ambiente virtual, pode ser utilizado:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Depois, ative novamente:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
python -m pip install -r requirements.txt
```

---

## Executando a API

Com o ambiente virtual ativado, execute:

```powershell
python -m uvicorn main:app --reload
```

A API será disponibilizada em:

```text
http://127.0.0.1:8000
```

---

## Documentação da API

O FastAPI disponibiliza automaticamente uma interface Swagger para testar os endpoints.

Acesse:

```text
http://127.0.0.1:8000/docs
```

Também é possível consultar a documentação OpenAPI em:

```text
http://127.0.0.1:8000/openapi.json
```

---

## Endpoints disponíveis

### 1. Verificar funcionamento da API

```http
GET /
```

Retorna uma mensagem informando que a API está funcionando.

Exemplo:

```json
{
    "mensagem": "API de Vendas funcionando!",
    "documentacao": "/docs"
}
```

---

### 2. Listar todas as vendas

```http
GET /vendas
```

Retorna todas as vendas cadastradas no arquivo `vendas.csv`.

---

### 3. Consultar uma venda pelo ID

```http
GET /vendas/{id}
```

Exemplo:

```http
GET /vendas/1
```

Retorna os dados da venda correspondente ao ID informado.

Caso o ID não exista, a API retorna erro HTTP `404`.

---

### 4. Consultar vendas por produto

```http
GET /vendas/produto/{produto}
```

Exemplo:

```http
GET /vendas/produto/Notebook
```

Retorna todas as vendas relacionadas ao produto informado.

A consulta não diferencia letras maiúsculas e minúsculas.

---

### 5. Consultar vendas por cliente

```http
GET /vendas/cliente/{cliente}
```

Exemplo:

```http
GET /vendas/cliente/Joao
```

Retorna todas as vendas realizadas para o cliente informado.

A consulta não diferencia letras maiúsculas e minúsculas.

---

## Endpoints de análise

### 6. Faturamento total

```http
GET /analise/total
```

Calcula o faturamento total utilizando:

```text
quantidade × preço
```

Com os dados atuais do projeto, o faturamento total é:

```text
R$ 27.390,00
```

---

### 7. Análise por produto

```http
GET /analise/produtos
```

Agrupa as vendas por produto e apresenta:

* quantidade total vendida;
* faturamento de cada produto.

Exemplo de resultado:

```json
[
    {
        "produto": "Monitor",
        "quantidade_vendida": 5,
        "faturamento": 6000.0
    },
    {
        "produto": "Mouse",
        "quantidade_vendida": 23,
        "faturamento": 1840.0
    }
]
```

---

### 8. Resumo geral

```http
GET /analise/resumo
```

Apresenta um resumo dos dados de vendas, incluindo:

* quantidade de registros de vendas;
* quantidade total de produtos vendidos;
* faturamento total;
* produto mais vendido.

Com os dados atuais:

```json
{
    "quantidade_de_vendas": 10,
    "quantidade_de_produtos_vendidos": 39,
    "faturamento_total": 27390.0,
    "produto_mais_vendido": "Mouse"
}
```

---

## Tratamento de erros

A API utiliza respostas HTTP adequadas quando uma consulta não encontra resultados.

Por exemplo, ao consultar uma venda inexistente:

```http
GET /vendas/999
```

A API retorna:

```json
{
    "detail": "Venda não encontrada"
}
```

com status HTTP:

```text
404 Not Found
```

O mesmo princípio é utilizado nas consultas por produto e cliente.

---

## Principais conceitos utilizados

O projeto aplica os seguintes conceitos:

* criação de uma API REST;
* criação de rotas com FastAPI;
* utilização de métodos HTTP `GET`;
* leitura de arquivos CSV;
* manipulação de dados com Pandas;
* filtragem de dados;
* agrupamento de informações;
* cálculo de valores;
* geração de respostas JSON;
* tratamento de erros HTTP;
* documentação automática com Swagger/OpenAPI.

---

## Autor

Projeto desenvolvido como atividade prática do curso do SENAI.

**Tecnologias:** Python, FastAPI e Pandas.
