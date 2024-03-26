# IMPORTS
import docker


# DOCKER CLIENT CLASS
class DockerMgmtClient:
    """
    A Class to manage Docker Containers
    """

    def __init__(self):
        # self.docker = docker.from_env()
        self.docker = docker.DockerClient(base_url='unix://var/run/docker.sock')

    # START CONTAINER
    def start_container(self, key):
        """
        Start Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]
        """

        if not self.container_exists(key):
            return

        container = self.docker.containers.get(key)
        container.start()
        return container

    # REMOVE CONTAINER
    def remove_container(self, key):
        """
        Remove Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]
        """

        if not self.container_exists(key):
            return

        container = self.docker.containers.get(key)
        container.stop()
        container.remove()

        return container

    # STOP CONTAINER
    def stop_container(self, key):
        """
        Stop Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]
        """

        if not self.container_exists(key):
            return

        container = self.docker.containers.get(key)
        container.stop()

        return container

    # GET IMAGES
    def list_images(self):
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
    def get_container(self, key):
        """
        Get Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]

        """

        if not self.container_exists(key):
            return

        container = self.docker.containers.get(key)
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}

    # GET CONTAINERS
    def list_containers(self):
        """
        Get All Containers from Docker

        :return: Dictionary [id, name, image, status]

        """
        all_containers = self.docker.containers.list(all=True)
        return_list = []
        for container in all_containers:
            container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
            return_list.append(
                {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status})
        return return_list

    # RESTARTING CONTAINER
    def restart_container(self, key):
        """
        Restart Container from Docker

        :param key: id from Container on Docker
        :return: Dictionary [id, name, image, status]

        """

        if not self.container_exists(key):
            return

        container = self.docker.containers.get(key)
        container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
        return {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status}

    # RESTARTING ALL CONTAINERS
    def restart_all_containers(self):
        """
        Restart All Containers from Docker

        :return: Dictionary [id, name, image, status]

        """
        all_containers = self.docker.containers.list(filters={'status': 'running'})
        return_list = []
        for container in all_containers:
            container.restart()
            container_image = str(container.attrs['Config']['Image']).replace('docker/', '')
            list.append(
                {'id': container.id, 'name': container.name, 'image': container_image, 'status': container.status})
        return return_list

    def container_exists(self, key):
        return True if self.docker.containers.get(key) else False
