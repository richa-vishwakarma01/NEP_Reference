from pytest_bdd import given, when, then, parsers
import requests
from utils.datautils import data_utils
import os


@then("Run importData request to import competition with Matcheswith bad user and password")
def import_file_bad_cred():
    url = "http://localhost:8103/import/competitionsWithMatches"
    response = requests.post(url, headers={'Content-Type': 'application/json;charset=UTF-8'})
    data_utils.last_response = response
    print(response)


@then("Run importData request to import competition with Matches")
def import_data():
    url = "http://localhost:8103/import/competitionsWithMatches"
    response = requests.post(url, headers={'Content-Type': 'application/json;charset=UTF-8'},
                             auth=(os.environ['USERNAME'], os.environ['PASSWORD']))
    data_utils.last_response = response
    print(response)
