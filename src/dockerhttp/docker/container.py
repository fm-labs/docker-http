

def get_container_detail(container_id: str):
    """
    Get container details via Docker API

    :param container_id: The container ID
    :return:
    """
    details: dict = {}

    # TODO: Implement this
    details.update({
        "id": container_id,
        "name": "container1",
        # ...
    })
    return details
