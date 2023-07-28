import os
from fastapi import FastAPI
from typing import List
import pymongo
from varivaveisAmbiente import *
import logging

#log
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('log_main')
console_handler = logging.StreamHandler()
logger.addHandler(console_handler)

#criando uma instância do objeto Framework FastAPI
endpoint = FastAPI()

#Conexão do banco MONGODB
c = os.getenv('DB_PROTOCOL')+ "://" + os.getenv('DB_USER') + ":" + os.getenv('DB_PASSWORD') + "@" +os.getenv('DB_HOST')+ "/?retryWrites=true&w=majority"

try:
    mongo_client = pymongo.MongoClient(c, serverSelectionTimeoutMS=5000)
    mongo_client.server_info()
    db = mongo_client["fortics"]
    usuarios_collection = db["usuarios"]
    grupos_collection = db["grupos"]
    logging.debug("Banco conectado com sucesso")
except pymongo.errors.ConnectionFailure:
    logging.error("Não foi possível conectar ao MongoDB.")

#Endpoints
@endpoint.get("/grupos", response_model=List[dict])
async def get_grupos():
    grupos = list(grupos_collection.find())
    return grupos

@endpoint.get("/usuarios", response_model=List[dict])
async def get_usuarios():
    usuarios = list(usuarios_collection.find())
    return usuarios


