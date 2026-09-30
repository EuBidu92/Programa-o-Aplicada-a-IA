# Sistema de Análise de Atendimentos

Projeto final da disciplina de Programação Aplicada a IA.

## Objetivo

Desenvolver uma API REST para cadastro, consulta, atualização, exclusão e análise de atendimentos.

## Tecnologias

- Python
- FastAPI
- MySQL
- SQLAlchemy
- PyMySQL
- Pandas
- Pydantic
- Uvicorn

## Funcionalidades

### CRUD

- Cadastro de atendimentos
- Consulta de atendimentos
- Consulta individual
- Atualização de registros
- Exclusão de registros

### Análises

- Resumo geral
- Atendimentos por categoria
- Atendimentos por status
- Atendimentos por atendente
- Atendente com maior quantidade
- Tempo médio de atendimento
- Satisfação média
- Maiores avaliações
- Menores avaliações
- Atendimentos por período
- Desempenho dos atendentes
- Demanda por categoria

## Estrutura

- `main.py` — API e endpoints
- `database.py` — conexão com MySQL
- `models.py` — modelo da tabela
- `schemas.py` — validação dos dados
- `analytics.py` — análises utilizando Pandas
- `banco.sql` — estrutura do banco
- `requirements.txt` — dependências

## Execução

Instale as dependências:

```bash
pip install -r requirements.txt