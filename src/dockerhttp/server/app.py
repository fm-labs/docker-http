from flask import Flask, jsonify
from flask_cors import CORS
from src.dockerhttp.docker.container import DKClient


# CLASSES
app, dk = Flask(__name__), DKClient()
CORS(app)


@app.route('/', methods=["GET"])
def index():
    data = {
        "message": "Welcome to docker-http!",
        "version": "1.0.0"
    }
    return jsonify(data)


# START CONTAINER
@app.route('/container/start/<string:key>')
def startContainer(key):
    return jsonify(dk.startContainer(key))


# STOP CONTAINER
@app.route('/container/stop/<string:key>')
def stopContainer(key):
    return jsonify(dk.stopContainer(key))


# REMOVE CONTAINER
@app.route('/container/remove/<string:key>')
def removeContainer(key):
    return jsonify(dk.removeContainer(key))


# GET IMAGES
@app.route('/images')
def getImages():
    return jsonify(dk.getImages())


# LIST ALL CONTAINERS
@app.route('/containers')
def containers():
    return jsonify(dk.getContainers())


# GET CONTAINER
@app.route('/container/<string:key>')
def getContainer(key):
    return jsonify(dk.getContainer(key))


# RESTARTING CONTAINER
@app.route('/container/restart/<string:key>')
def restartContainer(key):
    return jsonify(dk.restartContainer(key))


# RESTARTING ALL CONTAINERS
@app.route('/containers/restart')
def restartAll():
    return jsonify(dk.restartAll())