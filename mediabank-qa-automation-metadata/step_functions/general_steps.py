import logging
from pytest_bdd import given, when, then, parsers
from utils.datautils import data_utils

@then(parsers.cfparse("I verify the HTTP response {code:Number}",
                      extra_types=dict(Number=int)))
def check_status_response(code):
    logging.info('CURRENT RESPONSE STATUS CODE: %s', data_utils.last_response.status_code)
    logging.info('EXPECTED RESPONSE STATUS CODE: %s', code)
    assert data_utils.last_response.status_code == code

@then(parsers.cfparse("The response contains the text '{text:Char}'",
                      extra_types=dict(Char=str)))
def check_text_in_response(text):
    logging.info('RESPONSE: %s', data_utils.last_response.text)
    assert text in data_utils.last_response.text