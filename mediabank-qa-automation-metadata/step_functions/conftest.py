import pytest
import logging
from docker_steps import *
from utils.datautils import data_utils
from python_on_whales import docker as docker_whales
import os
from dotenv import load_dotenv
from ofbl_integration.ofbl_steps import *
from database_steps import*
from xfl_integration.xfl_steps import *
from general_steps import*

logging.getLogger().setLevel(logging.INFO)


def pytest_bdd_before_scenario(request, feature, scenario):
    data_utils.resources['ENV'] = os.getenv('ENV', 'local')
    logging.info("Working on %s environment...", data_utils.resources['ENV'])
    data_utils.resources['docker_running'] = False


#def pytest_bdd_after_scenario(request, feature, scenario):
#    client = docker.from_env()
#    running_container = client.containers.list()
#    for container in running_container:
#        container.stop()


def pytest_bdd_before_scenario(request, feature, scenario):
    data_utils.resources['ENV'] = os.getenv('ENV', 'local')
    load_dotenv()
#    data_utils.resources['GITHUB_TOKEN'] = os.getenv('GITHUB_TOKEN')
