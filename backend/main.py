from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def inicio():
    return{"mensagem": "conectado"}

@app.post("/despesas")
def cria_despesas(nome: str, descricao:str, valor:float):
    nova_despesa = {
        "nome": nome,
        "descricao": descricao,
        "valor": valor
    }

@app.get("/despesas")
def lista_despesas():
    return [
         {"nome":"parcela", "descricao": "casa", "valor": 1000.00},
        {"nome":"parcela","descricao": "cabelo", "valor": 30.00}
    ]

@app.post("/receitas")
class receitas(BaseModel):
    descricao:str
    valor : float
@app.get("/receitas")
def lista_recitas():
    return   [
        {"descricao": "salario", "valor": 2000.00},
        {"descricao": "freelancer", "valor": 150.00}

    ]
