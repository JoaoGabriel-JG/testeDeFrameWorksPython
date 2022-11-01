from fastapi import FastAPI

app = FastAPI()     # Cria uma instancia de classe FastAPI

@app.get("/")       # Informa a rota "/" usando o operador get      A sintaxe @alguma_coisa é chamado de decorador
async def root():                               # Função de rota assíncrona 
    return { "menssage": "Hello World" }        # Retorne o conteúdo



"""
Comandos:

@app.post()
@app.put()
@app.delete()
"""
