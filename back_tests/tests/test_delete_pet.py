import allure

from back_tests.consts import PET_TO_DELETE


@allure.story('Delete pet')
class TestDeletePet:
    def test_delete_pet_positive(self, petstore_client):
        with allure.step('Create pet for deleting'):
            petstore_client.create_pet(PET_TO_DELETE)
        with allure.step('Send requests'):
            delete_response = petstore_client.delete_pet_by_id(PET_TO_DELETE.id)
        with allure.step('Check response structure'):
            assert delete_response.status_code == 200
            assert delete_response.json().get('code') == 200
            assert delete_response.json().get('type') == 'unknown'
            assert delete_response.json().get('message') == str(PET_TO_DELETE.id)
        with allure.step('Check that pet is deleted'):
            pet_by_id_response = petstore_client.find_pet_by_id(PET_TO_DELETE.id)
            assert pet_by_id_response.status_code == 404
            assert pet_by_id_response.json().get('code') == 1
            assert pet_by_id_response.json().get('type') == 'error'
            assert pet_by_id_response.json().get('message') == 'Pet not found'

    def test_delete_pet_negative(self, petstore_client):
        with allure.step('Send requests twice to make sure that the last request was with a non-existent pet'):
            petstore_client.delete_pet_by_id(PET_TO_DELETE.id)
            delete_response = petstore_client.delete_pet_by_id(PET_TO_DELETE.id)
        with allure.step('Check response code'):
            assert delete_response.status_code == 404
