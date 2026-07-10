from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
despesas = []

@app.get("/")
def inicio():
    return{"mensagem": "conectado"}

class Despesa(BaseModel):
    nome:str
    valor:float
    descricao:str
@app.post("/despesas")
async def criar_despesa(despesa: Despesa):
    despesas.append(despesa)
    return {"mensagem":"Despesa cadastrada"}

@app.get("/despesas")
def lista_despesas():
    return despesas
