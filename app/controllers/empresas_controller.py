from app.models.empresa import carregar_empresas
from app.data.empresas_mock import EMPRESAS_MOCK

class EmpresasController:
    def __init__(self):
        self.empresas = carregar_empresas(EMPRESAS_MOCK)

    def _para_dicionario(self, empresa):
        return {
            "id": empresa.mostrar_id(),
            "nome": empresa.mostrar_nome(),
            "setor": empresa.mostrar_setor()
        }

    def listar(self):
        return [self._para_dicionario(e) for e in self.empresas]

    def buscar_por_id(self, id):
        for e in self.empresas:
            if e.mostrar_id() == id:
                return self._para_dicionario(e)
        return None

