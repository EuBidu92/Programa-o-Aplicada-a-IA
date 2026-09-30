import pandas as pd

from sqlalchemy import text

from database import engine


def carregar_dados():

    query = text("""
        SELECT
            id,
            cliente,
            categoria,
            atendente,
            data_atendimento,
            status,
            descricao,
            tempo_atendimento,
            satisfacao
        FROM atendimentos
    """)

    with engine.connect() as connection:

        df = pd.read_sql(
            query,
            connection
        )

    return df


def resumo_geral():

    df = carregar_dados()

    total = len(df)

    return {
        "total_atendimentos": int(total),

        "clientes_unicos": int(
            df["cliente"].nunique()
        ),

        "categorias": int(
            df["categoria"].nunique()
        ),

        "atendentes": int(
            df["atendente"].nunique()
        ),

        "atendimentos_concluidos": int(
            (df["status"] == "Concluído").sum()
        ),

        "atendimentos_em_andamento": int(
            (df["status"] == "Em andamento").sum()
        ),

        "atendimentos_pendentes": int(
            (df["status"] == "Pendente").sum()
        )
    }


def por_categoria():

    df = carregar_dados()

    resultado = (
        df.groupby("categoria")
        .size()
        .reset_index(name="quantidade")
    )

    return resultado.to_dict(
        orient="records"
    )


def por_status():

    df = carregar_dados()

    resultado = (
        df.groupby("status")
        .size()
        .reset_index(name="quantidade")
    )

    return resultado.to_dict(
        orient="records"
    )


def por_atendente():

    df = carregar_dados()

    resultado = (
        df.groupby("atendente")
        .size()
        .reset_index(name="quantidade")
        .sort_values(
            "quantidade",
            ascending=False
        )
    )

    return resultado.to_dict(
        orient="records"
    )


def atendente_maior_numero():

    df = carregar_dados()

    resultado = (
        df.groupby("atendente")
        .size()
        .reset_index(name="quantidade")
        .sort_values(
            "quantidade",
            ascending=False
        )
    )

    primeiro = resultado.iloc[0]

    return {
        "atendente": primeiro["atendente"],
        "quantidade": int(primeiro["quantidade"])
    }


def tempo_medio():

    df = carregar_dados()

    media = df["tempo_atendimento"].mean()

    return {
        "tempo_medio_minutos": round(
            float(media),
            2
        )
    }


def satisfacao_media():

    df = carregar_dados()

    media = df["satisfacao"].mean()

    return {
        "satisfacao_media": round(
            float(media),
            2
        )
    }


def maiores_avaliacoes():

    df = carregar_dados()

    dados = df.dropna(
        subset=["satisfacao"]
    )

    resultado = dados[
        dados["satisfacao"]
        == dados["satisfacao"].max()
    ]

    return resultado[
        [
            "id",
            "cliente",
            "atendente",
            "satisfacao"
        ]
    ].to_dict(
        orient="records"
    )


def menores_avaliacoes():

    df = carregar_dados()

    dados = df.dropna(
        subset=["satisfacao"]
    )

    resultado = dados[
        dados["satisfacao"]
        == dados["satisfacao"].min()
    ]

    return resultado[
        [
            "id",
            "cliente",
            "atendente",
            "satisfacao"
        ]
    ].to_dict(
        orient="records"
    )


def por_periodo(
    data_inicio,
    data_fim
):

    df = carregar_dados()

    df["data_atendimento"] = pd.to_datetime(
        df["data_atendimento"]
    )

    inicio = pd.to_datetime(data_inicio)
    fim = pd.to_datetime(data_fim)

    filtrado = df[
        (df["data_atendimento"] >= inicio)
        &
        (df["data_atendimento"] <= fim)
    ]

    resultado = (
        filtrado
        .groupby(
            df.loc[
                filtrado.index,
                "data_atendimento"
            ].dt.strftime("%Y-%m-%d")
        )
        .size()
        .reset_index(
            name="quantidade"
        )
    )

    resultado.columns = [
        "data",
        "quantidade"
    ]

    return resultado.to_dict(
        orient="records"
    )


# ==========================================
# ANÁLISE ADICIONAL
# ==========================================

def desempenho_atendentes():

    df = carregar_dados()

    resultado = (
        df.groupby("atendente")
        .agg(
            quantidade_atendimentos=(
                "id",
                "count"
            ),

            tempo_medio_minutos=(
                "tempo_atendimento",
                "mean"
            ),

            satisfacao_media=(
                "satisfacao",
                "mean"
            )
        )
        .reset_index()
    )

    resultado[
        "tempo_medio_minutos"
    ] = resultado[
        "tempo_medio_minutos"
    ].round(2)

    resultado[
        "satisfacao_media"
    ] = resultado[
        "satisfacao_media"
    ].round(2)

    return resultado.to_dict(
        orient="records"
    )


def categorias_com_maior_demanda():

    df = carregar_dados()

    resultado = (
        df.groupby("categoria")
        .agg(
            quantidade=(
                "id",
                "count"
            ),

            tempo_medio=(
                "tempo_atendimento",
                "mean"
            ),

            satisfacao_media=(
                "satisfacao",
                "mean"
            )
        )
        .reset_index()
        .sort_values(
            "quantidade",
            ascending=False
        )
    )

    resultado["tempo_medio"] = (
        resultado["tempo_medio"]
        .round(2)
    )

    resultado["satisfacao_media"] = (
        resultado["satisfacao_media"]
        .round(2)
    )

    return resultado.to_dict(
        orient="records"
    )