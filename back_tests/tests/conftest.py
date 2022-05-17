import allure
import pytest

from back_tests.checker import PetstoreChecker
from back_tests.client import PetstoreClient
from back_tests.consts import PET_ONLY_ID, PET_FULL

create_params = [
    {'pet': PET_ONLY_ID, 'type': 'only id'},
    {'pet': PET_FULL, 'type': 'full data'}
]


@pytest.fixture(params=create_params, ids=[x["type"] for x in create_params])
def valid_params(request):
    yield request.param
    PetstoreClient().delete_pet_by_id(request.param['pet'].id)
    assert PetstoreClient().find_pet_by_id(request.param['pet'].id).status_code == 404


@pytest.fixture
def created_pet():
    with allure.step('Create a pet'):
        PetstoreClient().create_pet(PET_FULL)
    yield PET_FULL
    with allure.step('Delete a pet after test'):
        PetstoreClient().delete_pet_by_id(PET_FULL.id)
    with allure.step('Check that pet is deleted'):
        assert PetstoreClient().find_pet_by_id(PET_FULL.id).status_code == 404


@pytest.fixture
def petstore_client():
    return PetstoreClient()


@pytest.fixture
def petstore_checker():
    return PetstoreChecker()
