from fastapi import FastAPI, HTTPException
import pandas as pd

app = FastAPI(
    title="API de Vendas",
    description="API REST para consulta e análise de vendas utilizando FastAPI e Pandas",
    version="1.0.0"
)

# Carrega o arquivo CSV
df = pd.read_csv("vendas.csv")


# --------------------------------------------------
# ROTA PRINCIPAL
# --------------------------------------------------

@app.get("/")
def inicio():
    return {
        "mensagem": "API de Vendas funcionando!",
        "documentacao": "/docs"
    }


# --------------------------------------------------
# LISTAR TODAS AS VENDAS
# --------------------------------------------------

@app.get("/vendas")
def listar_vendas():
    return df.to_dict(orient="records")


# --------------------------------------------------
# CONSULTAR UMA VENDA PELO ID
# --------------------------------------------------

@app.get("/vendas/{id}")
def consultar_venda(id: int):

    venda = df[df["id"] == id]

    if venda.empty:
        raise HTTPException(
            status_code=404,
            detail="Venda não encontrada"
        )

    return venda.to_dict(orient="records")[0]


# --------------------------------------------------
# FILTRAR VENDAS POR PRODUTO
# --------------------------------------------------

@app.get("/vendas/produto/{produto}")
def vendas_por_produto(produto: str):

    vendas = df[
        df["produto"].str.lower() == produto.lower()
    ]

    if vendas.empty:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma venda encontrada para esse produto"
        )

    return vendas.to_dict(orient="records")


# --------------------------------------------------
# FILTRAR VENDAS POR CLIENTE
# --------------------------------------------------

@app.get("/vendas/cliente/{cliente}")
def vendas_por_cliente(cliente: str):

    vendas = df[
        df["cliente"].str.lower() == cliente.lower()
    ]

    if vendas.empty:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma venda encontrada para esse cliente"
        )

    return vendas.to_dict(orient="records")


# --------------------------------------------------
# ANÁLISE DO TOTAL DE VENDAS
# --------------------------------------------------

@app.get("/analise/total")
def total_vendas():

    total = (df["quantidade"] * df["preco"]).sum()

    return {
        "total_vendas": round(float(total), 2)
    }


# --------------------------------------------------
# ANÁLISE POR PRODUTO
# --------------------------------------------------

@app.get("/analise/produtos")
def analise_produtos():

    df_analise = df.copy()

    df_analise["valor_total"] = (
        df_analise["quantidade"] * df_analise["preco"]
    )

    resultado = (
        df_analise
        .groupby("produto")
        .agg(
            quantidade_vendida=("quantidade", "sum"),
            faturamento=("valor_total", "sum")
        )
        .reset_index()
    )

    resultado["faturamento"] = resultado["faturamento"].round(2)

    return resultado.to_dict(orient="records")


# --------------------------------------------------
# RESUMO GERAL
# --------------------------------------------------

@app.get("/analise/resumo")
def resumo():

    df_analise = df.copy()

    df_analise["valor_total"] = (
        df_analise["quantidade"] * df_analise["preco"]
    )

    total_vendas = df_analise["valor_total"].sum()
    quantidade_produtos = df_analise["quantidade"].sum()
    quantidade_registros = len(df_analise)

    produto_mais_vendido = (
        df_analise
        .groupby("produto")["quantidade"]
        .sum()
        .idxmax()
    )

    return {
        "quantidade_de_vendas": quantidade_registros,
        "quantidade_de_produtos_vendidos": int(quantidade_produtos),
        "faturamento_total": round(float(total_vendas), 2),
        "produto_mais_vendido": produto_mais_vendido
    }