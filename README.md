# CNAB parser API
É uma api-rest com um CRUD totalmente feito, para uma aplicação full-stack onde trata, parseia e guarda dados de arquivos CNAB com os dados das movimentações financeiras de várias lojas.

### Com ela é possivel:
- Guardar esses dados parseados (CREATE) utilizando POST
- Recuperar os dados (LIST & RETRIEVE) utilizando GET
- Atualizá-los (UPDATE) utiizando PUT e PATCH
- Deletar os dados (DESTROY) utilizando DELETE

# Tecnologias utilizadas

- Django
- Python
- Django-rest-framework
- Pytest (pytest-testdox & pytest-django)
- Psycopg-binary2
- Drf-spectacular
- Python-dotenv
- PostgreSQL

# Como utilizar a aplicação

## Local
1. Clone este repositório
2. Crie o ambiente virtual com o comando ``python -m venv venv``, inicie o ambiente virtual com o ``source venv/bin/activate`` e instale os pacotes requeridos pelo projeto com o comando ``pip install -r requirements.txt``
3. Crie as variavéis de ambiente com o .env assim como estão no .env-example
4. Para rodar a aplicação no insomnia rode as migrations com o comando ``python manage.py migrate``
5. Rode a aplicação com o comando ``python manage.py runserver`` ou os testes com o comando ``pytest --testdox -vvs``
- Caso queira rodar no docker utilizar o comando ``docker compose up`` (lemnbre-se de mudar a variavel POSTGRES_HOST para db, para poder rodar o docker)

## Remoto
- Utilize o link do deploy da API: ``https://cnab-parser-api.onrender.com/api/transactions`` para utilizar o CRUD
- Para documentação pode acessar: ``https://cnab-parser-api.onrender.com/docs/swagger-ui/`` ou ``https://cnab-parser-api.onrender.com/docs/redoc/``
