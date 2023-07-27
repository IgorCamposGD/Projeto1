from fastapi import FastAPI
from typing import List
import pymongo

#Diretorio do log
log = 'D:/DEV/ProjetoEndpoints/endpoints.log'

#criando uma instância do objeto Framework FastAPI
endpoint = FastAPI()

#Conexão do banco MONGODB
c = "mongodb+srv://fortics:nXyjK0kp8Uyxs4Xv@mongodb.a46kimi.mongodb.net/?retryWrites=true&w=majority"

try:
    mongo_client = pymongo.MongoClient(c)
    db = mongo_client["fortics"]
    usuarios_collection = db["usuarios"]
    grupos_collection = db["grupos"]
except pymongo.errors.ConnectionFailure:
    log("Não foi possível conectar ao MongoDB."+str(pymongo.errors.ConnectionFailure), log)

#Endpoints
@endpoint.get("/grupos", response_model=List[dict])
async def get_grupos():
    grupos = list(grupos_collection.find())
    return grupos

@endpoint.get("/usuarios", response_model=List[dict])
async def get_usuarios():
    usuarios = list(usuarios_collection.find())
    return usuarios


