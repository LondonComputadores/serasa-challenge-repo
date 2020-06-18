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

Para rodar com o Docker:

- docker-compose up --build -d
- export FLASK_APP=app.py
flask run
# Running on http://127.0.0.1:5000


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
- https://pyliaorachel.github.io/tutorial/devops/docker/2017/08/04/getting-started-with-docker-running-flask-redisdb-and-nginx.html
- https://github.com/frol/flask-restplus-server-example/wiki/Using-PostgreSQL-instead-of-Sqlite
- https://linuxize.com/post/how-to-build-docker-images-with-dockerfile/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/
