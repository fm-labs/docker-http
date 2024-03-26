FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install any needed packages specified in poetry.lock
COPY ./pyproject.toml ./poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev

# Copy the current directory contents into the container at /app
COPY ./src /app/src
COPY ./docker-http.py /app/docker-http.py

CMD ["python", "/app/docker-http.py"]

EXPOSE 5050
