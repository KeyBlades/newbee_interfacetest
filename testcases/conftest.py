import pytest
import requests
from utils.read_write import rw
from data.test_data import login_request_id


@pytest.fixture(scope='session')
def handler():
    rw.init()
    return rw


@pytest.fixture(scope='session')
def login():
    method, url, data, header, expect = rw.get_params(login_request_id)
    req_txt = requests.request(method, url, data=data, headers=header)
    actual_response = eval(req_txt.text)
    token = actual_response['data']
    return token
