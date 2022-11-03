from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Declara um JSON Object 

class Item(BaseModel):          # Declarando modelo de dados com uma classe herdada BaseModel
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):      # Declarando um parâmetro
    return item
