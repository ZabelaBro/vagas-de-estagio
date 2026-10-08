from app.models.vaga import carregar_vagas, TIPOS_VAGA
from app.data.vagas_mock import VAGAS_MOCK

class VagasController:
    def __init__(self):
        self.vagas = carregar_vagas(VAGAS_MOCK)

    def _para_dicionario(self, vaga):
        return vaga.para_dicionario()

    def listar(self):
        return [self._para_dicionario(v) for v in self.vagas]

    def listar_por_empresa(self, id_empresa):
        filtradas = [v for v in self.vagas if v.mostrar_id_empresa() == id_empresa]
        return [self._para_dicionario(v) for v in filtradas]

    def buscar_por_id(self, id):
        for v in self.vagas:
            if v.mostrar_id() == id:
                return self._para_dicionario(v)
        return None

    def adicionar(self, dados):
        if self.buscar_por_id(dados["id"]) is not None:
            raise KeyError("Vaga já existe com este ID")
            
        dados_copia = dados.copy()
        tipo = dados_copia.pop("tipo")
        classe_vaga = TIPOS_VAGA[tipo.lower()]
        nova_vaga = classe_vaga(**dados_copia)
        self.vagas.append(nova_vaga)
        return self._para_dicionario(nova_vaga)

