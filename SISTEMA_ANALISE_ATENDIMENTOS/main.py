from datetime import date

from fastapi import (
    FastAPI,
    Depends,
    HTTPException,
    Query
)

from sqlalchemy.orm import Session

from database import get_db

from models import Atendimento

from schemas import (
    AtendimentoCreate,
    AtendimentoUpdate,
    AtendimentoResponse
)

import analytics


# ==========================================
# CONFIGURAÇÃO DA API
# ==========================================

app = FastAPI(
    title="Sistema de Análise de Atendimentos",
    description="""
    API REST para cadastro, consulta, atualização,
    exclusão e análise de atendimentos.
    """,
    version="1.0.0"
)


# ==========================================
# ENDPOINT INICIAL
# ==========================================

@app.get("/")
def inicio():

    return {
        "mensagem": "Sistema de Análise de Atendimentos funcionando!",
        "documentacao": "/docs"
    }


# ==========================================
# GET - LISTAR TODOS
# ==========================================

@app.get(
    "/atendimentos",
    response_model=list[AtendimentoResponse]
)
def listar_atendimentos(
    db: Session = Depends(get_db)
):

    atendimentos = (
        db.query(Atendimento)
        .order_by(Atendimento.id)
        .all()
    )

    return atendimentos


# ==========================================
# GET - BUSCAR POR ID
# ==========================================

@app.get(
    "/atendimentos/{atendimento_id}",
    response_model=AtendimentoResponse
)
def buscar_atendimento(
    atendimento_id: int,
    db: Session = Depends(get_db)
):

    atendimento = (
        db.query(Atendimento)
        .filter(
            Atendimento.id == atendimento_id
        )
        .first()
    )

    if atendimento is None:

        raise HTTPException(
            status_code=404,
            detail="Atendimento não encontrado"
        )

    return atendimento


# ==========================================
# POST - CRIAR
# ==========================================

@app.post(
    "/atendimentos",
    response_model=AtendimentoResponse,
    status_code=201
)
def criar_atendimento(
    atendimento: AtendimentoCreate,
    db: Session = Depends(get_db)
):

    novo_atendimento = Atendimento(
        cliente=atendimento.cliente,
        categoria=atendimento.categoria,
        atendente=atendimento.atendente,
        data_atendimento=atendimento.data_atendimento,
        status=atendimento.status,
        descricao=atendimento.descricao,
        tempo_atendimento=atendimento.tempo_atendimento,
        satisfacao=atendimento.satisfacao
    )

    db.add(novo_atendimento)

    db.commit()

    db.refresh(novo_atendimento)

    return novo_atendimento


# ==========================================
# PUT - ATUALIZAR
# ==========================================

@app.put(
    "/atendimentos/{atendimento_id}",
    response_model=AtendimentoResponse
)
def atualizar_atendimento(
    atendimento_id: int,
    dados: AtendimentoUpdate,
    db: Session = Depends(get_db)
):

    atendimento = (
        db.query(Atendimento)
        .filter(
            Atendimento.id == atendimento_id
        )
        .first()
    )

    if atendimento is None:

        raise HTTPException(
            status_code=404,
            detail="Atendimento não encontrado"
        )

    dados_atualizados = dados.model_dump(
        exclude_unset=True
    )

    for campo, valor in dados_atualizados.items():

        setattr(
            atendimento,
            campo,
            valor
        )

    db.commit()

    db.refresh(atendimento)

    return atendimento


# ==========================================
# DELETE - EXCLUIR
# ==========================================

@app.delete(
    "/atendimentos/{atendimento_id}"
)
def excluir_atendimento(
    atendimento_id: int,
    db: Session = Depends(get_db)
):

    atendimento = (
        db.query(Atendimento)
        .filter(
            Atendimento.id == atendimento_id
        )
        .first()
    )

    if atendimento is None:

        raise HTTPException(
            status_code=404,
            detail="Atendimento não encontrado"
        )

    db.delete(atendimento)

    db.commit()

    return {
        "mensagem": "Atendimento excluído com sucesso",
        "id": atendimento_id
    }


# ==========================================
# ANÁLISE - RESUMO
# ==========================================

@app.get(
    "/analises/resumo"
)
def analise_resumo():

    return analytics.resumo_geral()


# ==========================================
# ANÁLISE - CATEGORIAS
# ==========================================

@app.get(
    "/analises/categorias"
)
def analise_categorias():

    return analytics.por_categoria()


# ==========================================
# ANÁLISE - STATUS
# ==========================================

@app.get(
    "/analises/status"
)
def analise_status():

    return analytics.por_status()


# ==========================================
# ANÁLISE - ATENDENTES
# ==========================================

@app.get(
    "/analises/atendentes"
)
def analise_atendentes():

    return analytics.por_atendente()


# ==========================================
# ANÁLISE - ATENDENTE COM MAIS ATENDIMENTOS
# ==========================================

@app.get(
    "/analises/atendente-destaque"
)
def analise_atendente_destaque():

    return analytics.atendente_maior_numero()


# ==========================================
# ANÁLISE - TEMPO MÉDIO
# ==========================================

@app.get(
    "/analises/tempo-medio"
)
def analise_tempo_medio():

    return analytics.tempo_medio()


# ==========================================
# ANÁLISE - SATISFAÇÃO
# ==========================================

@app.get(
    "/analises/satisfacao"
)
def analise_satisfacao():

    return analytics.satisfacao_media()


# ==========================================
# ANÁLISE - MAIORES AVALIAÇÕES
# ==========================================

@app.get(
    "/analises/avaliacoes/maiores"
)
def analise_maiores_avaliacoes():

    return analytics.maiores_avaliacoes()


# ==========================================
# ANÁLISE - MENORES AVALIAÇÕES
# ==========================================

@app.get(
    "/analises/avaliacoes/menores"
)
def analise_menores_avaliacoes():

    return analytics.menores_avaliacoes()


# ==========================================
# ANÁLISE - POR PERÍODO
# ==========================================

@app.get(
    "/analises/periodo"
)
def analise_periodo(

    data_inicio: date = Query(
        ...,
        description="Data inicial no formato YYYY-MM-DD"
    ),

    data_fim: date = Query(
        ...,
        description="Data final no formato YYYY-MM-DD"
    )
):

    if data_inicio > data_fim:

        raise HTTPException(
            status_code=400,
            detail="A data inicial não pode ser maior que a data final"
        )

    return analytics.por_periodo(
        data_inicio,
        data_fim
    )


# ==========================================
# ANÁLISE ADICIONAL - DESEMPENHO
# ==========================================

@app.get(
    "/analises/desempenho-atendentes"
)
def analise_desempenho():

    return analytics.desempenho_atendentes()


# ==========================================
# ANÁLISE ADICIONAL - CATEGORIAS
# ==========================================

@app.get(
    "/analises/demanda-categorias"
)
def analise_demanda_categorias():

    return analytics.categorias_com_maior_demanda()