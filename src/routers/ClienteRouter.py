# Rafael Waltrick
from fastapi import APIRouter
from domain.entities.Cliente import Cliente

router = APIRouter()

@router.get("/cliente/", tags=["Cliente"], status_code=200)
def get_cliente():
    return {"msg": "cliente get todos executado"}

@router.get("/cliente/{id}", tags=["Cliente"], status_code=200)
def get_cliente_id(id: int):
    return {"msg": "cliente get um executado", "id": id}

@router.post("/cliente/", tags=["Cliente"], status_code=200)
def post_cliente(cliente: Cliente):
    return {
        "msg": "cliente post executado",
        "dados": cliente
    }

@router.put("/cliente/{id}", tags=["Cliente"], status_code=200)
def put_cliente(id: int, cliente: Cliente):
    return {
        "msg": "cliente put executado",
        "id": id,
        "dados": cliente
    }

@router.delete("/cliente/{id}", tags=["Cliente"], status_code=200)
def delete_cliente(id: int):
    return {"msg": "cliente delete executado", "id": id}