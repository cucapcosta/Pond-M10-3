from datetime import datetime, timezone

from sqlmodel import select

from inf.connection import get_session
from domain.entities.figurinha import Figurinha


class FigurinhaRepository:
    def save(self, fig: Figurinha) -> Figurinha:
        with get_session() as s:
            s.add(fig)
            s.commit()
            s.refresh(fig)
            return fig
    def getAll(self):
        with get_session() as s:
            statement = select(Figurinha)
            results = s.exec(statement)
            return results.all()
    def getById(self, id: int):
        with get_session() as s:
            statement = select(Figurinha).where(Figurinha.id == id)
            result = s.exec(statement).first()
            return result
    def update(self, id: int, fig: Figurinha):
        with get_session() as s:
            statement = select(Figurinha).where(Figurinha.id == id)
            result = s.exec(statement).first()
            if not result:
                return None
            result.nome = fig.nome
            result.numero = fig.numero
            result.tipo = fig.tipo
            result.posicao = fig.posicao
            result.updated_at = datetime.now(timezone.utc)
            s.add(result)
            s.commit()
            s.refresh(result)
            return result
    def delete(self, id: int):
        with get_session() as s:
            statement = select(Figurinha).where(Figurinha.id == id)
            result = s.exec(statement).first()
            if not result:
                return None
            s.delete(result)
            s.commit()
            return result
    
