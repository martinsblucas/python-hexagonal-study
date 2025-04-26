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
│   ├── domain -->> Camada de Domínio (Core)
│   │   ├── exceptions.py
│   │   ├── models -->> Entidades/Objetos de Valor do domínio
│   │   │   └── student.py
│   │   └── ports -->> Definição de como o domínio interage com o exterior
│   │       └── repositories
│   │           └── student.py
│   └── use_cases -->> Camada de Casos de Uso
│       └── student.py
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

1.  **Centro (Core):** `app/domain` contém a lógica pura de negócio (entidades, objetos de valor) e as interfaces (`ports`) que definem como o domínio interage com o mundo exterior (ex: `ports/repositories`). Ele não depende de detalhes de infraestrutura como web frameworks ou bancos de dados.
2.  **Camada de Casos de Uso:** `app/use_cases` orquestra os fluxos da aplicação. Cada caso de uso implementa uma funcionalidade específica (ex: criar um estudante, buscar estudantes), utilizando as entidades do domínio e interagindo com o exterior através das portas do domínio (ex: chamando métodos da porta de repositório). É chamado pelos adaptadores *inbound*.
3.  **Adaptadores Inbound:** `app/adapters/inbound/rest` (neste exemplo, uma API REST com FastAPI) recebe comandos externos (requisições HTTP), valida e converte os dados de entrada (usando `v1/models`), e **chama os casos de uso apropriados (`app/use_cases`)** para executar a lógica da aplicação.
4.  **Adaptadores Outbound:** `app/adapters/outbound/repositories/student.py` implementa a interface de repositório (`Port`) definida em `app/domain/ports/repositories/student.py`. Ele usa tecnologias específicas (como SQLAlchemy em `app/adapters/outbound/orm`) para interagir com sistemas externos (como o banco de dados). **É chamado pelos casos de uso através das portas do domínio.**
5.  **Configuração e Injeção de Dependência:** `app/configs` configura a aplicação e gerencia a injeção de dependências, conectando as implementações concretas (adaptadores) às abstrações (portas) usadas pelos casos de uso e pelo domínio.
6.  **Infraestrutura:** `infrastructure` contém código de suporte não relacionado diretamente à lógica da aplicação, como configurações de migração (`alembic`) e scripts para execução (`run_dev.py`).
