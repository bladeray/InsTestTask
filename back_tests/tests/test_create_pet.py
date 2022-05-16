from back_tests.consts import PET_TOO_BIG_ID


class TestCreatePet:
    def test_create_pet_positive(self, petstore_client, petstore_checker, valid_params):
        response = petstore_client.create_pet(valid_params['pet'])
        assert response.status_code == 200
        assert response.json().get('id')
        petstore_checker.check_pet(valid_params['pet'])

    def test_create_pet_negative(self, petstore_client):
        response = petstore_client.create_pet(PET_TOO_BIG_ID)
        assert response.status_code == 500
        assert response.json().get('code') == 500
        assert response.json().get('type') == 'unknown'
        assert response.json().get('message') == 'something bad happened'

