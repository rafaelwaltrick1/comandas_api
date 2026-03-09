# Rafael Waltrick
from fastapi import APIRouter
from domain.entities.Funcionario import Funcionario

router = APIRouter()

@router.get("/funcionario/", tags=["Funcionário"], status_code=200)
def get_funcionario():
    return {"msg": "funcionario get todos executado"}

@router.get("/funcionario/{id}", tags=["Funcionário"], status_code=200)
def get_funcionario_id(id: int):
    return {"msg": "funcionario get um executado", "id": id}

@router.post("/funcionario/", tags=["Funcionário"], status_code=200)
def post_funcionario(funcionario: Funcionario):
    return {
        "msg": "funcionario post executado",
        "dados": funcionario
    }

@router.put("/funcionario/{id}", tags=["Funcionário"], status_code=200)
def put_funcionario(id: int, funcionario: Funcionario):
    return {
        "msg": "funcionario put executado",
        "id": id,
        "dados": funcionario
    }

@router.delete("/funcionario/{id}", tags=["Funcionário"], status_code=200)
def delete_funcionario(id: int):
    return {"msg": "funcionario delete executado", "id": id}