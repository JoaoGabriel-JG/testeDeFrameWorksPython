from fastapi import FastAPI

app = FastAPI()

@app.get("/files/{file_path}:path")     # :path diz que o parâmetro deve coincidir com qualquer rota
async def read_file(file_path: str):
    return { "file_path": file_path }
