from fastapi import APIRouter, HTTPException
from app.controllers.empresas_controller import EmpresasController

router = APIRouter(prefix="/empresas", tags=["Empresas"])
controller = EmpresasController()

@router.get("/")
def listar_empresas():
    return controller.listar()

@router.get("/{id}")
def buscar_empresa(id: int):
    resultado = controller.buscar_por_id(id)
    if not resultado:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return resultado

