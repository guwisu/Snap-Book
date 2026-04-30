FROM python:3.11-slim

ENV POETRY_VERSION=2.2.1

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

RUN poetry config virtualenvs.create false

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

CMD alembic upgrade head; python src/main.py