from fastapi import FastAPI

endpoint = FastAPI()

usuarios = [
    {"id": 1, "nome": "Igor"},
    {"id": 2, "nome": "Ketly"},
]

grupos = [
    {"id": 1, "nome": "Admin"},
    {"id": 1, "nome": "Usuarios"},
]

@endpoint.get("/grupos", grupos)
async def get_grupos():
    return grupos

@endpoint.get("/usuarios" usuarios)
async def get_users():
    return usuarios
