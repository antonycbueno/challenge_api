# challenge_api


## Instalação

### Siga essa ordem de comandos para instalação:

```
# Clonar projeto CHALLENGE API
git clone https://github.com/antonycbueno/challenge_api

# Entrar na pasta do projeto
cd challenge_api

# Criar ambiente virtual
python -m venv venv .

# Ativando ambiente virtual
cd venv
cd Scripts
activate

# Retorne para a pasta raiz "challenge_api"
cd..
cd..

# Instalando requisitos
pip install django djangorestframework

# Subindo tabelas para banco de dados
python manage.py makemigrations
python manage.py migrate

# Criando um super usuário
python manage.py createsuperuser

# Iniciando servidor
python manage.py runserver
```


## URLS
```
# Direciona para local administrativo
http://127.0.0.1:8000/admin/

# Direciona para local onde pode cadastrar clientes, produtos e listas de favoritos
http://127.0.0.1:8000/

# Direciona para visualizar todos os produtos cadastrados na API.
http://127.0.0.1:8000/api/
```


## Desenvolvedor
* **Antony Bueno** - *Projeto Inicial*
