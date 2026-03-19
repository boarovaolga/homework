import pytest
from api_client import ApiClient
from project_api import ProjectApi

YOUGILE_TOKEN = "rNTOoIjVCYvOyfGGTiZ1X+cZ2EaHYpbBFiOIUEbQxvfKEwW4SGzSqU6e5linVY3V"

@pytest.fixture(scope='session')
def base_url():
    return 'https://ru.yougile.com'

@pytest.fixture(scope='session')
def token():
    return YOUGILE_TOKEN

@pytest.fixture(scope='session')
def api_client(base_url, token):
    return ApiClient(base_url, token)

@pytest.fixture
def project_api(api_client):
    return ProjectApi(api_client)