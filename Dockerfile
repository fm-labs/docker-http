FROM python:3.11-slim

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

COPY ./src /app/src
COPY ./docker-http.py /app/docker-http.py

CMD ["python", "/app/docker-http.py"]

EXPOSE 5050