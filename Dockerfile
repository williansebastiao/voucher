FROM python:3.13-alpine

WORKDIR /code

RUN apk add --no-cache \
    make \
    curl \
    bash \
    nano \
    git

RUN adduser -D appuser

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry config virtualenvs.in-project false

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .

RUN chown -R appuser:appuser /code

USER appuser
