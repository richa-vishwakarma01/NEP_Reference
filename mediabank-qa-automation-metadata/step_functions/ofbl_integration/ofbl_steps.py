from pytest_bdd import given, when, then, parsers
import xml.etree.ElementTree as ET
import requests
from utils.datautils import data_utils
import os
import logging
import time


@then("I import the data")
def import_file():
    url = "http://localhost:8095/importData/"
    content_file = open(f"./resources/ofbl/ofbl.xml", 'rb').read()
    response = requests.post(url, data=content_file, headers={'Content-Type': 'application/xml;charset=UTF-8'},
                             auth=(os.environ['USERNAME'], os.environ['PASSWORD']))
    data_utils.last_response = response
    print(response)


@then("I verify the Tags")
def verify_tags():
    url = "http://localhost:8040/__admin/requests"
    response = requests.get(url)
    data_utils.last_response = response
    assert response.status_code == 200
    response = requests.get('http://localhost:8040/__admin/requests')
    response_body = response.text
#    json_response = response.json()
#    domain_id = json_response["\"domain_id\""]
#    assert domain_id != ''


@when("A second import is requested with updated Data")
def import_data_with_update():
    url = "http://localhost:8095/importData/"
    content_file = open(f"./resources/ofbl/ofbl_updated.xml", 'rb').read()
    response = requests.post(url, data=content_file, headers={'Content-Type': 'application/xml;charset=UTF-8'})
    data_utils.last_response = response
    assert response.status_code == 200
