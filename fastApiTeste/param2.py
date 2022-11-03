from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Union[str, None] = None):    # Corpo da requisição, parâmetro de rota e parâmetro de consulta
    result = { "item_id": item_id,  **item.dict() }
    if q:
        result.update({ "q":q })
    return result

"""
Se o parâmetro também é declarado na rota, será utilizado como um parâmetro de rota.
Se o parâmetro é de um tipo único (como int, float, str, bool, etc) será interpretado 
como um parâmetro de consulta.
Se o parâmetro é declarado como um modelo Pydantic, será interpretado como o corpo da requisição.
"""
