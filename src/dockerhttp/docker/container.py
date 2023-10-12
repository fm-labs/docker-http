# IMPORTS
import docker

# DOCKER CLIENT CLASS
class DKClient:
    """
    A Class to manage Docker

    '''
    Attributes
    ----------
    self.docker : DockerClient
        DockerClient to execute Commands with Docker

    Methods
    -------
    startContainer(key)
        start container from docker
    stopContainer(key)
        stop container from docker
    getImages()
        get images from docker
    getContainer(key)
        get container from docker
    restartContainer(key)
        restart container from docker
    restartAll()
        restart all containers from docker


    """
    def __init__(self):
        self.docker = docker.from_env()


    # START CONTAINER
    def startContainer(self, key):
        """
        Start Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, status]

        """
        container = self.docker.containers.get(key)
        container.start()
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}


    # STOP CONTAINER
    def stopContainer(self, key):
        """
        Stop Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, status]

        """
        container = self.docker.containers.get(key)
        container.stop()
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}


    # GET IMAGES
    def getImages(self):
        """
        Get Images from Docker

        :return: Dictionary [id, tags, labels]

        """
        for image in self.docker.images.list():
            return {'id': image.id, 'tags': str(image.tags).replace('docker/', ''), 'labels': image.labels}


    # GET CONTAINER
    def getContainer(self, key):
        """
        Get Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, status]

        """
        container = self.docker.containers.get(key)
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}


    # GET CONTAINERS
    def getContainers(self):
        """
        Get All Containers from Docker

        :return: Dictionary [id, name, status]

        """
        for container in self.docker.containers.list():
            container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
            return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}


    # RESTARTING CONTAINER
    def restartContainer(self, key):
        """
        Restart Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, status]

        """
        container = self.docker.containers.get(key)
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}


    # RESTARTING ALL CONTAINERS
    def restartAll(self):
        """
        Restart All Containers from Docker

        :return: Dictionary [id, name, status]

        """
        for container in self.docker.containers.list():
            container.restart()
            container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
            return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}