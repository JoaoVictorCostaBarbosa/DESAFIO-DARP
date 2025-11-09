# Marketplace Agro — API RESTful

> Projeto desenvolvido como parte do **Desafio DARP**, com o objetivo de criar uma API RESTful que conecte produtores rurais e consumidores, simulando um marketplace agrícola simples e funcional.

---

## Descrição do Projeto

Pequenos produtores rurais enfrentam dificuldades para vender diretamente ao consumidor.  
Este sistema propõe uma **API** que gerencia o cadastro de usuários, produtos e pedidos, com controle de autenticação e permissões por tipo de usuário.

A aplicação foi desenvolvida com **FastAPI**, **SQLAlchemy (assíncrono)** e **PostgreSQL**, seguindo boas práticas RESTful.

---

## Funcionalidades Principais

### Usuários
- Cadastro e autenticação (com JWT);
- Tipos de usuário: `produtor`, `comprador`, `admin`;
- Apenas **administradores** podem deletar usuários.

### Produtos
- CRUD completo de produtos;
- Apenas o **produtor dono** pode alterar ou remover seus produtos;
- Listagem pública dos produtos disponíveis.

---

## Estrutura de Usuários

| Tipo de Usuário | Permissões |
|------------------|-------------|
| **Produtor** | Criar, atualizar e excluir seus produtos. |
| **Comprador** | Visualizar produtos disponíveis. |
| **Administrador** | Gerenciar todos os usuários. |

---

## Endpoints Principais

### Autenticação
| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/auth/register` | Cadastro de novo usuário |
| `POST` | `/auth/login` | Login e geração de token JWT |

### Produtos
| Método | Rota | Descrição | Permissão |
|--------|------|------------|------------|
| `POST` | `/produtos` | Criar novo produto | Produtor |
| `GET` | `/produtos` | Listar todos os produtos | Público |
| `GET` | `/produtos/{id}` | Detalhar produto específico | Público |
| `PUT` | `/produtos/{id}` | Atualizar produto | Produtor dono |
| `DELETE` | `/produtos/{id}` | Remover produto | Produtor dono |

---

## Tecnologias Utilizadas

| Categoria | Ferramenta |
|------------|-------------|
| **Linguagem** | Python 3.12 |
| **Framework Web** | FastAPI |
| **Banco de Dados** | PostgreSQL 16 |
| **ORM Assíncrono** | SQLAlchemy + asyncpg |
| **Migrações** | Alembic |
| **Autenticação** | JWT (via python-jose) |
| **Containerização** | Docker e Docker Compose |

---

## Principais Bibliotecas (requirements.txt)

- fastapi==0.121.0  
- SQLAlchemy==2.0.44  
- asyncpg==0.30.0  
- alembic==1.17.1  
- python-jose==3.5.0  
- passlib==1.7.4  
- pydantic==2.12.4  
- pydantic-settings==2.11.0  
- uvicorn==0.38.0  

---

## Como Executar o Projeto

### 1. Clonar o Repositório
```bash
git clone git@github.com:JoaoVictorCostaBarbosa/DESAFIO-DARP.git
cd DESAFIO-DARP
```

---

### 2. Crie o arquivo .env
Siga o .env.example e coloque suas credenciais postgres
```bash
DATABASE_URL=postgresql+asyncpg://SEU-USUARIO:SUA-SENHA@db:5432/marketplace_agro
SECRET_KEY=SENHA-SECRETA-PARA-CRIPTOGRAFIA-DO-JWT
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
POSTGRES_USER=SEU-USUARIO
POSTGRES_PASSWORD=SUA-SENHA
POSTGRES_DB=marketplace_agro
```

---

### 3. Corrigir permissão do entrypoint (caso necessário)
```bash
chmod +x entrypoint.sh
```

---

### 4. Contrua e rode o docker
```bash
docker-compose up --build
```


#### API disponivel em 'http://localhost:8000'
#### Documentação automática (Swagger) disponivel em 'http://localhost:8000/docs'
