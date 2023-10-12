from flask import Flask, jsonify
from flask_cors import CORS

from dockerhttp.docker.container import get_container_detail

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def index():
    data = {
        "message": "Welcome to docker-http!",
        "version": "1.0.0"
    }
    return jsonify(data)


@app.route('/containers', methods=["GET"])
def containers_index():
    # example response
    containers = [
        {
            "id": "1234567890",
            "name": "container1",
            "image": "image1",
            # ...
        }
    ]
    return jsonify(containers)


@app.route('/containers/detail/<string:key>', methods=["GET"])
def container_detail(key):
    # example of getting container details
    # TODO implement this
    result = get_container_detail(key)
    return jsonify(result)


