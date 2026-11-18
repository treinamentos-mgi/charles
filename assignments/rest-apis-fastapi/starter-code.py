# Código Inicial para a Tarefa de APIs REST com FastAPI
# Instale as dependências com: pip install fastapi uvicorn
# Execute o servidor com: uvicorn main:app --reload

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()


# Tarefa 1: Criar a Primeira Rota
@app.get("/")
def read_root():
    # Retornar a mensagem de boas-vindas
    pass


# Tarefa 2: Modelar Dados com Pydantic
class Task(BaseModel):
    # Definir os campos id, title e done
    pass


tasks: list[Task] = []


# Tarefa 3: Buscar, Atualizar e Remover Tarefas
# Tarefa 4: Filtrar Tarefas com Query Parameters
