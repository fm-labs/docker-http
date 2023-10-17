# docker-http

A docker mgmt http server


Related project:
- [docker-http-client](https://github.com/fm-labs/docker-http-client) - A web client for docker-http


## Development

Uses [poetry](https://python-poetry.org/) for dependency management.

```bash
poetry install
poetry run python -m docker_http
# or 
python ./docker-http.py
```

The docker-http webserver is served at `http://localhost:5000/` by default.

### Local development


```bash
# Start multiple containers with docker-compose for local development:
docker compose up
```

Starts following containers:
- hello-world (single command)
- cowsay (single command)
- whalesay (single command)
- redis (service)
- mariadb (service)


## Useful links

- [Docker Reference](https://docs.docker.com/reference/)
- [Docker SDK for Python](https://docker-py.readthedocs.io/en/stable/)
- [Docker SDK for Python API Reference](https://docker-py.readthedocs.io/en/stable/api.html)
