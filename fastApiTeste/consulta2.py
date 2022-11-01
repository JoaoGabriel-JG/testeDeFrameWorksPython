from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):    # None é o padrão
    item = { "item_id": item_id }
    if q:                         # Parâmetro "q" é opcional
        item.update({ "q": q })
    if not short:
        item.update(
            { "description": "This is an amazing item that has a long description" }
        )
    return item
