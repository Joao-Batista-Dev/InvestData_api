# InvestData API

Bem-vindo ao Sistema InvestData. API do Projeto que faz buscar automaticamente dos valores de ações na bolsa de valores.

## 🛠 Tecnologias
- Python 3.11
- Django 5
- Django REST Framework
- PostgreSQL
- Celery + RabbitMQ
- Docker & Docker Compose

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Docker
- Python
- Django
- PostgreSQL
- Celery
- Outras dependências listadas no arquivo `requirements.txt`

## Instalação das Dependências

Git clone:
```bash
https://github.com/Joao-Batista-Dev/InvestData
```

Entre no diretório do projeto
```bash
cd investdata
```

Crie e ative um ambiente virtual
```bash
python3 -m venv venv

source venv/bin/activate
```

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```

## Rodar o projeto

Execute o docker:
```bash
docker-compose up --build
```

Criando um usuário admin:
```bash
docker-compose exec investdata_web python manage.py createsuperuser
```

Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000](http://localhost:8000)

## Endpoint de Autenticação
### **POST** `/api/v1/auth/token/`
```json
{
    "username": "",
    "password": ""
}
```

### Todos os Endpoints precisam de autenticação, adicione o Token no Header da requisição
```json
{
   "Authorization": "Token {token}"
}
```

### Endpoints Stocks
### **GET** `api/v1/actions/`
#### Request Schema
```json
{
    "name": "Nome da ação da bolsa",
    "price": "Valor da Ação da bolsa",
	"created_at": "Atualização da ação da bolsa",
}
```

### **POST** `api/v1/actions/`
#### Request Schema
```json
{
    "name": "Nome da ação da bolsa",
}
```

### **PATH** `api/v1/actions/id/`
#### Request Schema
```json
{
    "name": "Nome da ação da bolsa",
    "price": "Valor da Ação da bolsa",
	"created_at": "Atualização da ação da bolsa",
}
```

### **DELETE** `api/v1/actions/id/`
#### Request Schema
```json
{
    "name": "Nome da ação da bolsa",
    "price": "Valor da Ação da bolsa",
	"created_at": "Atualização da ação da bolsa",
}
```


## 🎥 Demonstração

![Tela 1](./docs-gif/foto01.png)