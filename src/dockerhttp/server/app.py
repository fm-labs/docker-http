import os

from flask import Flask, jsonify
from flask_cors import CORS

from dockerhttp.docker.client import DockerMgmtClient

# CLASSES
docker_host = os.getenv("DOCKER_HOST", "unix:///var/run/docker.sock")
dk = DockerMgmtClient(docker_host)

app = Flask(__name__)
CORS(app)


@app.route('/', methods=["GET"])
def index():
    data = {
        "message": "Welcome to docker-http!",
        "version": "1.0.0"
    }
    return jsonify(data)


# LIST IMAGES
@app.route('/images')
def list_images():
    return jsonify(dk.list_images())


# START CONTAINER
@app.route('/container/start/<string:key>')
def start_container(key):
    return jsonify(dk.start_container(key))


# STOP CONTAINER
@app.route('/container/stop/<string:key>')
def stop_container(key):
    return jsonify(dk.stop_container(key))


# REMOVE CONTAINER
@app.route('/container/remove/<string:key>')
def remove_container(key):
    return jsonify(dk.remove_container(key))


# LIST ALL CONTAINERS
@app.route('/containers')
def list_containers():
    return jsonify(dk.list_containers())


# GET CONTAINER
@app.route('/container/<string:key>')
def describe_container(key):
    return jsonify(dk.get_container(key))


# RESTARTING CONTAINER
@app.route('/container/restart/<string:key>')
def restart_container(key):
    return jsonify(dk.restart_container(key))


# RESTARTING ALL CONTAINERS
@app.route('/containers/restart')
def restart_all_containers():
    return jsonify(dk.restart_all_containers())