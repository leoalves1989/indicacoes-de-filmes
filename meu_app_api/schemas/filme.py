from pydantic import BaseModel
from typing import Optional, List
from model.filme import Filme




class FilmeSchema(BaseModel):
    """ Define como um novo filme a ser inserido deve ser representado
    """
    nome: str = "Home Alone"
    streaming: str = "Netflix"
    indicacao: str = "Leo Alves"


class FilmeBuscaSchema(BaseModel):
    """ Define como deve ser a estrutura que representa a busca. Que será
        feita apenas com base no nome do filme.
    """
    nome: str = "Teste"


class ListagemFilmesSchema(BaseModel):
    """ Define como uma listagem de filmes será retornada.
    """
    filmes:List[FilmeSchema]


def apresenta_filmes(filmes: List[Filme]):
    """ Retorna uma representação do filme seguindo o schema definido em
        FilmeViewSchema.
    """
    result = []
    for filme in filmes:
        result.append({
            "nome": filme.nome,
            "streaming": filme.streaming,
            "indicacao": filme.indicacao,
        })

    return {"filmes": result}


class FilmeViewSchema(BaseModel):
   
    
    id: int = 1
    nome: str = "Home Alone"
    streaming: str = "Netflix"
    indicacao: str = "Leo Alves"
    
    


class FilmeDelSchema(BaseModel):
    """ Define como deve ser a estrutura do dado retornado após uma requisição
        de remoção.
    """
    mesage: str
    nome: str

def apresenta_filme(filme: Filme):
    """ Retorna uma representação do filme seguindo o schema definido em
        ProdutoViewSchema.
    """
    return {
        "id": filme.id,
        "nome": filme.nome,
        "streaming": filme.streaming,
        "indicacao": filme.indicacao,
       
       
    }
