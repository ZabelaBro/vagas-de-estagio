from fastapi import APIRouter, HTTPException
from app.controllers.vagas_controller import VagasController
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/vagas", tags=["Vagas"])
controller = VagasController()

class VagaInput(BaseModel):
    id: int
    titulo: str
    descricao: str
    bolsa: float
    id_empresa: int
    tipo: str
    local: Optional[str] = None
    vale_transporte: Optional[float] = None
    auxilio_internet: Optional[float] = None

@router.get("/")
def listar_vagas():
    return controller.listar()

@router.get("/{id}")
def buscar_vaga(id: int):
    resultado = controller.buscar_por_id(id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")
    return resultado

@router.get("/empresa/{id_empresa}")
def listar_vagas_empresa(id_empresa: int):
    return controller.listar_por_empresa(id_empresa)

@router.post("/", status_code=201)
def criar_vaga(vaga_input: VagaInput):
    dados = vaga_input.dict(exclude_none=True)
    try:
        resultado = controller.adicionar(dados)
        return resultado
    except KeyError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))

