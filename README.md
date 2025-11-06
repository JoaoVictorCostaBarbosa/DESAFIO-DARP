# DESAFIO-DARP

# Marketplace Agro — API RESTful

Pequenos produtores rurais enfrentam dificuldades para vender seus produtos diretamente aos consumidores.  
A ideia é criar uma **API RESTful** que permita a conexão entre **produtores**, **compradores** e **administradores**, formando um **marketplace agro**.

O sistema deve permitir o **cadastro de produtos agrícolas**, **pedidos de compra** e o **controle de estoque** — tudo de forma **automatizada e segura**.

---

## Objetivo
Desenvolver uma **API back-end** capaz de gerenciar:

- Cadastro e autenticação de usuários (**produtor**, **comprador**, **administrador**).  
- Catálogo de produtos.

---

## Tipos de Usuário e Funções

| Tipo de Usuário | Funções Essenciais |
|------------------|--------------------|
| **Produtor**     | Criar e gerenciar seus próprios produtos. |
| **Comprador**    | Apenas visualizar a lista de produtos (Catálogo). |
| **Administrador**| Gerenciar (listar, deletar) todos os usuários. |

---

## Principais Funcionalidades

### Autenticação
- Endpoints:
  - `POST /auth/register` — Cadastro de usuário.  
  - `POST /auth/login` — Login e geração de token JWT.
- Utilize **JWT (JSON Web Tokens)** para proteger rotas e identificar o usuário autenticado.

---

## Produto (CRUD Básico)

### Rotas

| Método | Rota | Descrição | Acesso |
|--------|------|------------|--------|
| **POST** | `/produtos` | Criar produto | Apenas **Produtor** |
| **GET** | `/produtos` | Listar todos os produtos | **Todos (autenticado ou não)** |
| **GET** | `/produtos/{id}` | Detalhar produto específico | **Todos** |
| **PUT** | `/produtos/{id}` | Atualizar produto | Apenas **Produtor dono** |
| **DELETE** | `/produtos/{id}` | Remover produto | Apenas **Produtor dono** |

---

## Requisitos e Validações

### Usuário

| Campo | Tipo | Requisitos / Validações |
|--------|------|--------------------------|
| **nome** | String | Obrigatório. Mínimo 3 caracteres. |
| **email** | String | Obrigatório. Deve ter formato válido e ser único. |
| **senha** | String | Obrigatório. Mínimo 8 caracteres, contendo letras e números. |
| **tipo** | String | Obrigatório. Deve ser um dos seguintes: `produtor`, `comprador`, `admin`. |
| **localizacao** | String | Opcional. Deve ter no máximo 100 caracteres. |

**Regras adicionais:**
- O e-mail não pode se repetir entre usuários.  
- A senha deve ser armazenada **com hashing seguro (ex: bcrypt)**.  
- Apenas **administradores** podem excluir outros usuários.  

---

### Produto

| Campo | Tipo | Requisitos / Validações |
|--------|------|--------------------------|
| **nome** | String | Obrigatório. Entre 3 e 100 caracteres. |
| **descricao** | String | Opcional. Máximo 500 caracteres. |
| **preco** | Float | Obrigatório. Deve ser maior que 0. |
| **quantidade** | Integer | Obrigatório. Deve ser maior ou igual a 0. |
| **categoria** | String | Obrigatório. Deve ser uma das categorias válidas (ex: `frutas`, `grãos`, `laticínios`, etc.). |
| **localizacao** | String | Opcional. Cidade ou região do produto. |
| **produtor_id** | Integer | Obrigatório. Referência ao usuário do tipo **produtor**. |

**Regras adicionais:**
- Apenas o **produtor dono do produto** pode alterá-lo ou removê-lo.  
- O campo **preço** deve aceitar até duas casas decimais.  
- Não é permitido cadastrar produtos com **quantidade negativa**.  
- Produtos devem ser automaticamente vinculados ao produtor autenticado no momento do cadastro.  

---

## Modelagem de Dados (Sugerida)

### Usuário

| Coluna | Tipo de Dado | Restrições | Descrição |
|--------|---------------|-------------|------------|
| `id` | Integer | **Primary Key** | Identificador único do usuário |
| `nome` | String | **NOT NULL** | Nome completo |
| `email` | String (Unique) | **NOT NULL** | Email usado para login |
| `senha_hash` | String | **NOT NULL** | Senha armazenada com hashing |
| `tipo` | String | **NOT NULL** | Perfil: `'produtor'`, `'comprador'` ou `'admin'` |
| `localizacao` | String | *Nullable* | Cidade/Região do usuário |

---

### Produto

| Coluna | Tipo de Dado | Restrições | Descrição |
|--------|---------------|-------------|------------|
| `id` | Integer | **Primary Key** | Identificador único do produto |
| `nome` | String | **NOT NULL** | Nome do produto (ex: "Tomate Orgânico") |
| `descricao` | String | *Nullable* | Descrição detalhada |
| `preco` | Float/Numeric | **NOT NULL** | Preço unitário |
| `quantidade` | Integer | **NOT NULL** | Quantidade em estoque |
| `categoria` | String | **NOT NULL** | Categoria (ex: "frutas", "laticínios") |
| `localizacao` | String | *Nullable* | Localização do produto |
| `produtor_id` | Integer | **Foreign Key (usuario.id)** | Dono do produto |

---

## Tecnologias Sugeridas

- **Linguagem:** Python  
  - Framework: **Django** ou **FastAPI**
- **Banco de Dados:** MySQL ou PostgreSQL  
- **Documentação:** Swagger / OpenAPI

---

## Critérios de Avaliação

| Critério | Descrição | Peso |
|-----------|------------|------|
| **Modelagem de Dados** | Estrutura correta das entidades e relacionamentos. | 15% |
| **Autenticação e Autorização** | Implementação funcional de login, JWT e controle de acesso. | 15% |
| **Endpoints RESTful** | Implementação correta dos endpoints CRUD e boas práticas HTTP. | 15% |
| **Lógica de Negócio e Validações** | Implementar a lógica de negócio descrita no documento, incluindo validações adequadas. | 15% |
| **Organização do Código** | Estrutura limpa, modular e bem documentada. | 15% |
| **Segurança** | Uso de boas práticas (hash de senha, proteção de rotas, etc.). | 15% |
| **Documentação (Swagger/OpenAPI)** | Clareza e completude da documentação da API. | 10% |
| **Docker (Extra)** | Implementação de um Dockerfile e Docker Compose funcional. | 5% |

---

## Observações

- O aluno deve **dar fork** no repositório oficial disponibilizado pela disciplina antes de iniciar o desenvolvimento.  
- No arquivo **README.md**, incluir as seguintes informações:
  - **Versão do Python** utilizada.  
  - **SGBD (Banco de Dados)** utilizado (ex: MySQL, PostgreSQL).  
  - **Principais bibliotecas** com suas versões (ex: FastAPI, SQLAlchemy, JWT, etc.).  
- O README também deve conter instruções de **instalação, execução e testes** da aplicação.



