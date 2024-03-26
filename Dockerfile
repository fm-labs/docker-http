FROM python:3.11-slim

WORKDIR /app

COPY ./README.md /app/README.md
COPY ./src /app/src
COPY ./docker-http.py /app/docker-http.py
COPY ./pyproject.toml ./poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --only main --no-root

CMD ["python", "/app/docker-http.py"]

EXPOSE 5050