from sqlmodel import SQLModel, Field
from datetime import datetime, timezone
from enum import Enum


class TipoFigurinha(str, Enum):
    comum = "comum"
    brilhante = "brilhante"
    legends_ouro = "legends_ouro"
    legends_bronze = "legends_bronze"


class Figurinha(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nome: str
    numero: int = Field(gt=0)
    tipo: TipoFigurinha
    posicao: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    #Obrigado https://github.com/fastapi/sqlmodel/issues/252 