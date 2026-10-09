# Vagas de Estágio API

Este é o backend de um sistema para gerenciar vagas de estágio e empresas. O projeto segue a arquitetura em 4 camadas: `data`, `models`, `controllers` e `routes`.

## Como rodar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
2. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```
3. Acesse a documentação interativa:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Diagrama de Classes

```mermaid
classDiagram
    class Empresa {
        -_id: int
        -_nome: str
        -_setor: str
        +__init__(id, nome, setor)
        +mostrar_id() int
        +mostrar_nome() str
        +mostrar_setor() str
        +alterar_nome(nome: str)
        +alterar_setor(setor: str)
        +__repr__() str
    }

    class Vaga {
        -_id: int
        -_titulo: str
        -_descricao: str
        -_bolsa: float
        -_id_empresa: int
        +TIPO_VAGA: str
        +__init__(id, titulo, descricao, bolsa, id_empresa)
        +mostrar_id() int
        +mostrar_titulo() str
        +mostrar_descricao() str
        +mostrar_bolsa() float
        +mostrar_id_empresa() int
        +mostrar_tipo() str
        +alterar_titulo(titulo: str)
        +alterar_descricao(descricao: str)
        +alterar_bolsa(bolsa: float)
        +resumo_beneficios() str
        +detalhes() dict
        +__repr__() str
    }

    class VagaPresencial {
        -_local: str
        -_vale_transporte: float
        +TIPO_VAGA: str
        +__init__(id, titulo, descricao, bolsa, id_empresa, local, vale_transporte)
        +mostrar_local() str
        +mostrar_vale_transporte() float
        +alterar_local(local: str)
        +alterar_vale_transporte(vt: float)
        +resumo_beneficios() str
        +detalhes() dict
    }

    class VagaRemota {
        -_auxilio_internet: float
        +TIPO_VAGA: str
        +__init__(id, titulo, descricao, bolsa, id_empresa, auxilio_internet)
        +mostrar_auxilio_internet() float
        +alterar_auxilio_internet(auxilio: float)
        +resumo_beneficios() str
        +detalhes() dict
    }

    Vaga <|-- VagaPresencial
    Vaga <|-- VagaRemota
    Empresa "1" -- "*" Vaga : anuncia
```

## Tabela de Rotas

| Verbo | Rota | Descrição |
|-------|------|-----------|
| GET | `/empresas/` | Lista todas as empresas |
| GET | `/empresas/{id}` | Busca uma empresa pelo ID (404 se não achar) |
| GET | `/vagas/` | Lista todas as vagas |
| GET | `/vagas/{id}` | Busca uma vaga pelo ID (404 se não achar) |
| GET | `/vagas/empresa/{id_empresa}` | Lista vagas de uma empresa específica |
| POST | `/vagas/` | Cria uma nova vaga (201 sucesso, 409 conflito, 422 erro de negócio) |

## Quem fez o quê

- **Aluno 1**: Estruturação do projeto
- **Aluno 2**: Models e `verificar.py`
- **Aluno 2**: Controladores, rotas FastAPI
- **Aluno 4**: `README.md` com diagrama

