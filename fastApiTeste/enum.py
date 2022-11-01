from enum import Enum

from fastapi import FastAPI

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"       # Nomes de modelos Machine Learning
    lenet = "lenet"

app = FastAPI()

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):     # Declarando um padrão de rota com a classe ENUM ModelName

    if model_name is ModelName.alexnet:                                         # Comparando o membro de enumeration
        return { "model_name": model_name, "message": "Deep Learning FTW!" }

    if ModelName.lenet.value:                                             # Pegando o valor exato do enumerate (um str)
        return { "model_name": model_name, "message": "LeCNN all the images" }

    return { "model_name": model_name, "message": "Have some residuals" }   # Retornando membros do enumeration

# Eles serão convertidos para os seus valores correspondentes (uma str) antes de retornar ao cliente
