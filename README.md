# Estudo de Arquitetura Hexagonal com Python

Esse projeto é um simples CRUD de uma entidade chamada `Student`, cujo propósito é estudar uma forma de utilizar a Arquitetura Hexagonal com Python. Neste exemplo, há uma API para receber os comandos do cliente e um repositório para acessar e manipular os dados persistentes. Este estudo se baseou bastante no artigo ["Arquitetura Hexagonal no Python"](https://medium.com/@augustomarinho/arquitetura-hexagonal-no-python-ae08b108ac12) e a [aplicação de exemplo utilizada por ele](https://github.com/augustomarinho/python-fastapi).

```
├── alembic.ini
├── app -->> Diretório raiz da aplicação principal
│   ├── adapters
│   │   ├── inbound -->> Recebem comandos externos
│   │   │   └── rest
│   │   │       ├── dependencies
│   │   │       │   └── core.py
│   │   │       ├── main.py
│   │   │       └── v1
│   │   │           ├── models -->> Schemas específicos da API REST
│   │   │           │   └── student.py
│   │   │           └── students.py
│   │   └── outbound -->> Interagem com sistemas externos
│   │       ├── orm
│   │       │   ├── models -->> Modelos específicos do ORM
│   │       │   │   ├── base_model.py
│   │       │   │   └── student.py
│   │       │   └── session_manager.py
│   │       └── repositories -->> Implementações das Portas de Repositório
│   │           └── student.py
│   ├── configs -->>  Configurações da aplicação
│   │   ├── dependency_injection.py
│   │   └── settings.py
│   └── domain -->> Camada de Domínio (Core)
│       ├── exceptions.py
│       ├── models -->> Entidades/Objetos de Valor do domínio
│       │   └── student.py
│       └── ports -->> Definição de como o domínio interage com o exterior
│           └── repositories
│               └── student.py
├── infrastructure -->> Código e configurações de infraestrutura
│   ├── alembic
│   │   ├── env.py
│   │   ├── script.py.mako
│   │   └── versions
│   │       ├── 6190b3b6be7b_create_students_table.py
│   └── run_dev.py
├── poetry.lock
├── pyproject.toml
└── tests -->> Diretório de testes automatizados
    └── unit
```


**Resumo da Aplicação da Arquitetura Hexagonal**

1.  **Centro (Hexágono):** `app/domain` contém a lógica pura e as interfaces (`ports`). Ele não sabe sobre FastAPI, SQLAlchemy ou qualquer detalhe externo.
2.  **Adaptadores Inbound:** `app/adapters/inbound/rest` recebe requisições HTTP, usa os schemas (`v1/models`) para validar/formatar dados, e chama a lógica através das portas injetadas via `configs/dependency_injection.py`.
3.  **Adaptadores Outbound:** `app/adapters/outbound/repositories/student.py` implementa a interface definida em `app/domain/ports/repositories/student.py`, usando o ORM (`app/adapters/outbound/orm`) para de fato interagir com o banco de dados.
4.  **Configuração:** `app/configs` cuida de configurar tudo, inclusive a injeção das dependências.
5. **Infraestrutura**: `infrastructure/alembic` contém as migrações do banco de dados e `infrastructure/run_dev.py` é um script para rodar a aplicação em modo de desenvolvimento.
