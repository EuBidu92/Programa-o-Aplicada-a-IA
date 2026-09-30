from datetime import date
from typing import Literal

from pydantic import BaseModel, Field, ConfigDict


StatusAtendimento = Literal[
    "Concluído",
    "Em andamento",
    "Pendente"
]


class AtendimentoCreate(BaseModel):

    cliente: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    categoria: str = Field(
        ...,
        min_length=1,
        max_length=50
    )

    atendente: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    data_atendimento: date

    status: StatusAtendimento

    descricao: str | None = None

    tempo_atendimento: int | None = Field(
        default=None,
        ge=0
    )

    satisfacao: float | None = Field(
        default=None,
        ge=0,
        le=5
    )


class AtendimentoUpdate(BaseModel):

    cliente: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    categoria: str | None = Field(
        default=None,
        min_length=1,
        max_length=50
    )

    atendente: str | None = Field(
        default=None,
        min_length=1,
        max_length=100
    )

    data_atendimento: date | None = None

    status: StatusAtendimento | None = None

    descricao: str | None = None

    tempo_atendimento: int | None = Field(
        default=None,
        ge=0
    )

    satisfacao: float | None = Field(
        default=None,
        ge=0,
        le=5
    )


class AtendimentoResponse(BaseModel):

    model_config = ConfigDict(
        from_attributes=True
    )

    id: int
    cliente: str
    categoria: str
    atendente: str
    data_atendimento: date
    status: str
    descricao: str | None
    tempo_atendimento: int | None
    satisfacao: float | None