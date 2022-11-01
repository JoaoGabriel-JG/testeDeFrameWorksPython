# As operações de rota são avaliadas pela ordem

from fastapi import FastAPI

app = FastAPI()

@app.get("/users/me")       # Rota para pegar dados do usuário atual
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")         # Rota para pegar dados de um usuário específico
async def read_user(user_id: str):
    return {"user_id": user_id}