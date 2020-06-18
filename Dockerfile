FROM python:3.8-alpine
WORKDIR /code
ENV FLASK_APP user_api.py
ENV FLASK_RUN_HOST 0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements-dev.txt requirements-dev.txt
RUN pip install libpq-dev | pip install -r requirements-dev.txt
COPY . .
CMD ["flask", "run"]


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