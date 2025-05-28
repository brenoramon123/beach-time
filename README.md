# 🏖️ Beach Time API

Beach Time é uma API desenvolvida com Django e Django Ninja para facilitar o **agendamento de quadras de beach tennis**, com foco inicial na cidade de **Parnaíba – PI**.


## ⚙️ Tecnologias Utilizadas

- **Python 3.11+**
- **Django 5.2.1**
- **Django Ninja**
- **ninja-extra + ninja-jwt**
- **PostgreSQL**
- **Poetry** (gerenciamento de dependências)
- **Pillow** (upload de imagens)
- **python-dotenv**

---

## ▶️ Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/brenoramon123/beach-time.git
cd beach-time
````

### 2. Instalar as dependências com Poetry

```bash
poetry install
poetry shell
```

### 3. Criar o arquivo `.env`
ww

```env
DJANGO_SECRET_KEY=^b3jgeg90d+s2c#2z2(@$=%dma8d&5q5$y_(4dopp8ld6tw1)
DEBUG=True
DB_NAME=beach_time_db
DB_USER=postgres
DB_PASS=postgres
DB_HOST=localhost
DB_PORT=5432
```

### 4. Criar o banco de dados

```sql
CREATE DATABASE beach_time_db;
```

### 5. Rodar as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Rodar o servidor

```bash
python manage.py runserver
```

Acesse a documentação Swagger em:
📚 [`http://localhost:8000/api/v1/docs`](http://localhost:8000/api/v1/docs)

---

## 🔐 Autenticação

A API utiliza **JWT** como mecanismo de autenticação.

### 🔸 Endpoint de login

```http
POST /api/v1/core/token
```

#### Exemplo de resposta

```json
{
  "token": "<access_token>",
  "user": {
    "full_name": "Breno Ramon",
    "email": "breno@example.com",
    "username": "breno",
    "is_admin": true
  }
}
```

Para acessar rotas protegidas, clique em **"Authorize"** na Swagger UI e insira:

```text
Bearer <access_token>
```

---

## 🧱 Arquitetura Modular em Camadas

O projeto segue uma arquitetura em camadas, com separação por domínio. Cada módulo possui:

* `controllers.py` – Entrada de requisições (rotas Ninja)
* `services.py` – Lógica de negócio
* `repository.py` – Acesso ao banco de dados
* `schemas.py` – Validação e serialização com Pydantic
* `models.py` – Definição das tabelas (ORM)

📁 Exemplo de estrutura de módulo:

```
modules/
└── tokens/
    ├── controllers.py
    ├── services.py
    ├── repository.py
    ├── schemas.py
    ├── models.py
```

Além disso, o comando customizado `python manage.py create_module_app nome-do-app` gera essa estrutura e registra o módulo automaticamente no `settings.py`.

---

## 📌 Funcionalidades atuais

* ✅ Setup com Django + Django Ninja
* ✅ Modelo `CustomUser` com upload de imagem
* ✅ Autenticação via JWT (`ninja_jwt`)
* ✅ Integração com PostgreSQL
* ✅ Estrutura pronta para modularização
* ✅ Criação de módulos automatizada com comando customizado

---

## 📍 Próximos passos

* [ ] Módulo de agendamento de quadras
* [ ] Gerenciamento de horários disponíveis
* [ ] Validação de regras de reserva
* [ ] Conexão com aplicativo mobile
* [ ] Painel de administração customizado

---

## 👥 Desenvolvedores

* **Breno Ramon**
* **Houston Barros**
* **Carlos Seixas**
* **Bruno Binga**

📍 Parnaíba – PI
