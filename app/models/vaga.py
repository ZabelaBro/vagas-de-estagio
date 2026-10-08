class Vaga:
    TIPO_VAGA = "Indefinido"

    def __init__(self, id, titulo, descricao, bolsa, id_empresa, **kwargs):
        self._id = id
        self.alterar_titulo(titulo)
        self.alterar_descricao(descricao)
        self.alterar_bolsa(bolsa)
        self._id_empresa = id_empresa

    def mostrar_id(self):
        return self._id

    def mostrar_titulo(self):
        return self._titulo

    def mostrar_descricao(self):
        return self._descricao

    def mostrar_bolsa(self):
        return self._bolsa

    def mostrar_id_empresa(self):
        return self._id_empresa

    def mostrar_tipo(self):
        return self.TIPO_VAGA

    def alterar_titulo(self, titulo):
        if not titulo or len(titulo.strip()) == 0:
            raise ValueError("O título da vaga é obrigatório.")
        self._titulo = titulo

    def alterar_descricao(self, descricao):
        if not descricao or len(descricao.strip()) == 0:
            raise ValueError("A descrição da vaga é obrigatória.")
        self._descricao = descricao

    def alterar_bolsa(self, bolsa):
        if bolsa < 500.0:
            raise ValueError("O valor da bolsa não pode ser menor que R$ 500,00.")
        self._bolsa = bolsa

    def resumo_beneficios(self):
        return f"Bolsa: R$ {self._bolsa:.2f}"

    def para_dicionario(self):
        return {
            "id": self.mostrar_id(),
            "titulo": self.mostrar_titulo(),
            "descricao": self.mostrar_descricao(),
            "bolsa": self.mostrar_bolsa(),
            "tipo": self.mostrar_tipo(),
            "id_empresa": self.mostrar_id_empresa(),
            "resumo_beneficios": self.resumo_beneficios()
        }

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.mostrar_id()}: {self.mostrar_titulo()}>"


class VagaPresencial(Vaga):
    TIPO_VAGA = "Presencial"

    def __init__(self, id, titulo, descricao, bolsa, id_empresa, local, vale_transporte, **kwargs):
        super().__init__(id, titulo, descricao, bolsa, id_empresa, **kwargs)
        self.alterar_local(local)
        self.alterar_vale_transporte(vale_transporte)

    def mostrar_local(self):
        return self._local

    def mostrar_vale_transporte(self):
        return self._vale_transporte

    def alterar_local(self, local):
        if not local or len(local.strip()) == 0:
            raise ValueError("O local é obrigatório para vagas presenciais.")
        self._local = local

    def alterar_vale_transporte(self, vale_transporte):
        if vale_transporte < 0.0:
            raise ValueError("O vale transporte não pode ser negativo.")
        self._vale_transporte = vale_transporte

    def resumo_beneficios(self):
        base = super().resumo_beneficios()
        return f"{base} + VT: R$ {self._vale_transporte:.2f}"

    def para_dicionario(self):
        dicionario = super().para_dicionario()
        dicionario["local"] = self.mostrar_local()
        dicionario["vale_transporte"] = self.mostrar_vale_transporte()
        return dicionario


class VagaRemota(Vaga):
    TIPO_VAGA = "Remota"

    def __init__(self, id, titulo, descricao, bolsa, id_empresa, auxilio_internet, **kwargs):
        super().__init__(id, titulo, descricao, bolsa, id_empresa, **kwargs)
        self.alterar_auxilio_internet(auxilio_internet)

    def mostrar_auxilio_internet(self):
        return self._auxilio_internet

    def alterar_auxilio_internet(self, auxilio):
        if auxilio < 50.0:
            raise ValueError("O auxílio internet deve ser de no mínimo R$ 50,00.")
        self._auxilio_internet = auxilio

    def resumo_beneficios(self):
        base = super().resumo_beneficios()
        return f"{base} + Auxílio Internet: R$ {self._auxilio_internet:.2f}"

    def para_dicionario(self):
        dicionario = super().para_dicionario()
        dicionario["auxilio_internet"] = self.mostrar_auxilio_internet()
        return dicionario


TIPOS_VAGA = {
    "presencial": VagaPresencial,
    "remota": VagaRemota
}

def carregar_vagas(dados_mock):
    vagas = []
    for dado in dados_mock:
        dado_copia = dado.copy()
        tipo = dado_copia.pop("tipo")
        classe_vaga = TIPOS_VAGA[tipo.lower()]
        vagas.append(classe_vaga(**dado_copia))
    return vagas

