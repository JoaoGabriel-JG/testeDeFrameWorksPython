# Parâmetros de consulta podem ser opcionais e ter valores padrão skip = 0 e limit = 10

from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{ "item_name": "Foo" }, { "item_name": "Bar" }, { "item_name": "Baz" }]

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):    # A consulta é o conjunto de pares chave-valor depois do ? separados por &
    return fake_items_db[skip : skip + limit]
