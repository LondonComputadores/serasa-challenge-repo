# serasa-challenge-repo
This is a code challenge from Serasa and its main stack is Python

                        SERASA CHALLENGE

Nesse projeto criamos um CRUD de microserviços sendo um de cadastro de clientes e o outro de serviço de pedidos para comunicarem entre si para troca de informações.

O projeto tem como stack principal as seguintes tecnologias:

- Flask-Restful
- SQLAlchemy
- SQLite / Postgres
- Pytest
- Docker

Para o planejamento e execução das etapas foi utilizado o quadro Kanban do Trello como simulação de ambiente ágil, mantendo a organização e progresso do projeto.

- https://trello.com/b/B1GOF8cd/serasa-challenge

Relação de endpoints:

- api.add_resource(User, '/users/<string:name>/')
- api.add_resource(ListUsers, '/users/')
- api.add_resource(ListOrders, '/orders/')

Para montar e rodar/subir a aplicação com o Docker na sua virtualenv:

(1ª vez - Montar a imagem)
- docker-compose up --build -d
- export FLASK_APP=app.py
- flask run 
    ou
(2ª vez em diante - Rodar/Subir a aplicação) 
- docker-compose up

# Running on http://127.0.0.1:5000/users

O módulo user_api.py é o módulo principal e para rodá-lo basta descomentar esse bloco nele:

- @auth.verify_password
def acknowledge(login, password):
  """
      Esse método verifica login do usuário
  """
    # if not (login, password):
    #     return False
    # return Sign_In.query.filter_by(login=login, password=password).first()

Obs.: Esse bloco teve que ser comentado para que pudesse rodar no Docker, e será aberto uma issue no github para que esse bug possa ser sanado.

    A class ListUsers também foi comentada para rodar no Docker e precisará ser descomentada assi como o bloco verify_password, e usar o módulo utils.py para modificar e rodar o app e verificar sua comunicação entre Users, Orders e Logins.


Referências: 

- https://flask-restful.readthedocs.io/en/latest/index.html
- https://www.sqlalchemy.org/
- https://www.psycopg.org/docs/install.html#build-prerequisites
- https://www.python.pro.br
- https://web.digitalinnovation.one
- https://github.com/lucassimon/flask-api-users
- https://kite.com/blog/python/flask-sqlalchemy-tutorial/
- https://travis-ci.org/
- https://pyup.io/
- https://morioh.com/p/1d2afc550822
- https://www.freecodecamp.org/news/
- https://github.com/frol/flask-restplus-server-example/wiki/Using-PostgreSQL-instead-of-Sqlite
- https://pyliaorachel.github.io/tutorial/devops/docker/2017/08/04/getting-started-with-docker-running-flask-redisdb-and-nginx.html
- https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/
