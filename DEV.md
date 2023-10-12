# Development

Create a (flask) web server that can be used to manage docker containers.

The communication with the webserver is done using HTTP requests with JSON payloads

The web server should be able to:

- List containers 
- Start containers
- Stop containers
- Restart containers
- Remove containers
- List images


Example:

HTTP request:

```bash
curl -v http://localhost:5000/containers
```

HTTP response:
    
```json
[
    {
        "id": "1234567890",
        "name": "my-container",
        "image": "my-image",
        "status": "running"
    },
    {
        "id": "0987654321",
        "name": "my-container-2",
        "image": "my-image-2",
        "status": "stopped"
    }
]
```


## More features (Phase 2)

- Pull images
- Remove images
- List networks
- Create networks
- Remove networks
- List volumes
- Create volumes
- Remove volumes
- List docker-compose files
- Start docker-compose files
- Stop docker-compose files
- Restart docker-compose files
- Remove docker-compose files


## Advanced features (Phase 3)

- Webserver authentication using JWT / AuthToken
- SSH Tunneling
- SSL / TLS
