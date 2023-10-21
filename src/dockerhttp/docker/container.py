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
    removeContainer(key)
        remove container from docker
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
    existContainer(key)
        return true if container exist else false


    """
    def __init__(self):
        self.docker = docker.from_env()


    # START CONTAINER
    def startContainer(self, key):
        """
        Start Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]

        """


        if not self.existContainer(key):
            return


        container = self.docker.containers.get(key)
        container.start()
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}


    # REMOVE CONTAINER
    def removeContainer(self, key):
        """
        Remove Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]
        """


        if not self.existContainer(key):
            return


        all_containers = self.docker.containers.list()
        return_list = []


        target_container = self.docker.containers.get(key)
        target_container.stop()
        target_container.remove()


        for container in all_containers:
            container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
            return_list.append({'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status})
        return return_list


    # STOP CONTAINER
    def stopContainer(self, key):
        """
        Stop Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]

        """


        if not self.existContainer(key):
            return


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
        all_containers = self.docker.images.list(all=True)
        return_list = []
        for image in all_containers:
            return_list.append({'id': image.id, 'tags': str(image.tags).replace('docker/', ''), 'labels': image.labels})
        return return_list


    # GET CONTAINER
    def getContainer(self, key):
        """
        Get Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]

        """


        if not self.existContainer(key):
            return


        container = self.docker.containers.get(key)
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}


    # GET CONTAINERS
    def getContainers(self):
        """
        Get All Containers from Docker

        :return: Dictionary [id, name, image, status]

        """
        all_containers = self.docker.containers.list(all=True)
        return_list = []
        for container in all_containers:
            container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
            return_list.append({'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status})
        return return_list


    # RESTARTING CONTAINER
    def restartContainer(self, key):
        """
        Restart Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]

        """


        if not self.existContainer(key):
            return


        container = self.docker.containers.get(key)
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}


    # RESTARTING ALL CONTAINERS
    def restartAll(self):
        """
        Restart All Containers from Docker

        :return: Dictionary [id, name, image, status]

        """
        all_containers = self.docker.containers.list(filters={'status':'running'})
        return_list = []
        for container in all_containers:
            container.restart()
            container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
            list.append({'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status})
        return return_list


    def existContainer(self, key):
        return True if self.docker.containers.get(key) else False