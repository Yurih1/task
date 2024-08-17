# Projeto Task com Django e MySQL

Este projeto é uma aplicação rest utilizando Django configurada para rodar com Docker(ou não rs) e MySQL. Este guia fornece instruções sobre como configurar e executar o projeto.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Configuração do Ambiente

### 1. Clone o Repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone https://github.com/yurih1/task.git
cd task
```

### 2. Configure o Arquivo .env

Crie um arquivo chamado .env na raiz do projeto para definir variáveis de ambiente necessárias para o Django. Aqui estão as instruções para Windows e Linux:

No Linux
#### 1. Crie um arquivo chamado .env na raiz do projeto:

```bash
touch .env
cp env.example .env
```
Edite o arquivo .env com um editor de texto e adicione as seguintes variáveis:

DJANGO_DB_HOST=db
DJANGO_DB_PORT=3306
DJANGO_DB_NAME=dbname
DJANGO_DB_USER=user
DJANGO_DB_PASSWORD=password

### 3. Rodando o projeto

```bash
docker-compose up --build
```

Quando o container subir entrar no container **django_web** digitando os comandos abaixo:

```bash
docker ps
docker exec -it <nome-ou-id-do-container> bash
```
Ou
```bash
docker exec -it <nome-ou-id-do-container> sh
```

Agora execute esses comando abaixo dentro do container:

```bash
python manage.py migrate
python manage.py createsuperuser
```
Você será solicitado a fornecer um nome de usuário, e-mail e senha para o superusuário.


### 4. **Se chegou até aqui, o projeto estara disponível no seu localhost** [swagger](http://127.0.0.1:8000/swagger/)

### 5. Sem docker

#### Faça até o passo 3. Depois, abra o terminal e rode os comandos abaixo:

```bash
python -m venv env

source env/bin/activate  # No Windows use `env\Scripts\activate`
pip install django

cd taskmanager

pip install -r requirements.txt

python manage.py migrate # Será preciso criar um bd, abrar um novo terminal, mysql -u <usuario> -p CREATE DATABASE <nome que está na .env>;


python manage.py createsuperuser


python manage.py runserver

```
Pronto, pode voltar ao passo 4 agora. 

Caso queira rodar os testes:
```bash
python manage.py test
```
