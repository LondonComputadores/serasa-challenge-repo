FROM python:3.8-alpine
WORKDIR /code
ENV FLASK_APP user_api.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache postgresql-dev gcc musl-dev linux-headers
COPY requirements-dev.txt requirements-dev.txt
CMD sudo apt install postgresql-server-dev-all \
    export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH
RUN pip install -r requirements-dev.txt
COPY . .
CMD ["flask", "run"]


#CMD sudo apt install postgresql-server-dev-all \

########################################################################
# Abaixo seria uma opção para iniciar corretamente o virtualenv
# FROM python:3.8.2-slim
# # Set up and activate virtual environment
# ENV VIRTUAL_ENV "/venv3"
# RUN python -m venv $VIRTUAL_ENV
# ENV PATH "$VIRTUAL_ENV/bin:$PATH"
# # Python commands run inside the virtual environment
# RUN python -m pip install \
# parse \
# serasa-challenge-repo
########################################################################