from fastapi import FastAPI
from typing import List

endpoint = FastAPI()

usuarios = [
    {"id": 1, "nome": "Igor"},
    {"id": 2, "nome": "Ketly"},
]

grupos = [
    {"id": 1, "nome": "Admin"},
    {"id": 1, "nome": "Usuarios"},
]

@endpoint.get("/grupos", response_model=List[dict])
async def get_grupos():
    return grupos

@endpoint.get("/usuarios", response_model=List[dict])
async def get_usuarios():
    return usuarios
