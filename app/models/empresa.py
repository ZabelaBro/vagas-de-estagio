class Empresa:
    def __init__(self, id, nome, setor, **kwargs):
        self._id = id
        self.alterar_nome(nome)
        self.alterar_setor(setor)

    def mostrar_id(self):
        return self._id

    def mostrar_nome(self):
        return self._nome

    def mostrar_setor(self):
        return self._setor

    def alterar_nome(self, nome):
        if not nome or len(nome.strip()) == 0:
            raise ValueError("O nome da empresa é obrigatório.")
        self._nome = nome

    def alterar_setor(self, setor):
        if not setor or len(setor.strip()) == 0:
            raise ValueError("O setor da empresa é obrigatório.")
        self._setor = setor

    def __repr__(self):
        return f"<Empresa {self.mostrar_id()}: {self.mostrar_nome()}>"

def carregar_empresas(dados_mock):
    empresas = []
    for dado in dados_mock:
        empresas.append(Empresa(**dado))
    return empresas

