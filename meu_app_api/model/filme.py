from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base


class Filme(Base):
    __tablename__ = 'filme'

    id = Column("pk_filme", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    streaming = Column(String(140))
    indicacao = Column(String(140))
    data_insercao = Column(DateTime, default=datetime.now())

    

    
    # Essa relação é implicita, não está salva na tabela 'filme',
    # mas aqui estou deixando para SQLAlchemy a responsabilidade
    # de reconstruir esse relacionamento.
    

    def __init__(self, nome:str, streaming:str, indicacao:str,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Filme

        Arguments:
            nome: nome do filme.
            streaming: streaming que passa o filme
            indicacao: quem indicou o filme
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.streaming = streaming
        self.indicacao = indicacao

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    

