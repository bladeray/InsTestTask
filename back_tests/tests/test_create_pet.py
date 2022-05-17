import allure

from back_tests.consts import PET_TOO_BIG_ID


@allure.story('Create pet')
class TestCreatePet:
    def test_create_pet_positive(self, petstore_client, petstore_checker, valid_params):
        with allure.step('Send requests'):
            response = petstore_client.create_pet(valid_params['pet'])
        with allure.step('Check response structure'):
            assert response.status_code == 200
            assert response.json().get('id')
        with allure.step('Check that pet is created'):
            petstore_checker.check_pet(valid_params['pet'])

    def test_create_pet_negative(self, petstore_client):
        with allure.step('Send requests'):
            response = petstore_client.create_pet(PET_TOO_BIG_ID)
        with allure.step('Check response structure'):
            assert response.status_code == 500
            assert response.json().get('code') == 500
            assert response.json().get('type') == 'unknown'
            assert response.json().get('message') == 'something bad happened'

