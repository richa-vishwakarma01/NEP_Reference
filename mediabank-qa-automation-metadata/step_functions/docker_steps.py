import pytest
from docker_steps import *
import os
from pytest_bdd import given, then
import docker
from python_on_whales import docker as docker_whales
from python_on_whales import DockerClient
from pytest_bdd import parsers
from utils.datautils import data_utils
import time
import subprocess



@given(parsers.cfparse("I do the {option:Char} run", extra_types={"Char": str}))
def docker_compose_up(option):
    script_path = './docker-build-and-run-thirdparty-stubs.sh'
    subprocess.run(['bash', script_path], check=True)
    if data_utils.resources['ENV'] == "local":
        container = docker_compose(option)
        data_utils.resources['docker_compose_running'] = True
        data_utils.resources['container'] = container
        time.sleep(60)
    else:
        logging.info("Working in dev. Docker compose is not necessary")


def docker_compose(option):
    if option == "docker_compose":
        return docker_whales.compose.up(detach=True)
    elif option == "docker compose for ofbl":
        docker_client = DockerClient(compose_files=["./docker-compose-ofbl.yml"])
        return docker_client.compose.up(detach=True)
    else:
        fileName = f'./docker-compose-{option}.yml'
        docker_client = DockerClient(compose_files=fileName)
        return docker_client.compose.up(detach=True)
