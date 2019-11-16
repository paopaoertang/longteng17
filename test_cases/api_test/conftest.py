import pytest

from utils.data import Data
from utils.db import DB
from utils.api import Api


@pytest.fixture(scope='session')
def data(request):
    data = Data('api_data.yaml').from_yaml()
    case_name = request.function.__name__
    return data.get(case_name)


@pytest.fixture(scope='session')
def db():
    db = DB()
    yield db
    db.close()


@pytest.fixture(scope='session')
def api():
    api = Api()
    return api
