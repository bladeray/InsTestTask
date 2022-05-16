from back_tests.consts import PET_TO_DELETE


class TestCreatePet:
    def test_delete_pet_positive(self, petstore_client):
        petstore_client.create_pet(PET_TO_DELETE)
        delete_response = petstore_client.delete_pet_by_id(PET_TO_DELETE.id)
        assert delete_response.status_code == 200
        assert delete_response.json().get('code') == 200
        assert delete_response.json().get('type') == 'unknown'
        assert delete_response.json().get('message') == str(PET_TO_DELETE.id)
        pet_by_id_response = petstore_client.find_pet_by_id(PET_TO_DELETE.id)
        assert pet_by_id_response.status_code == 404
        assert pet_by_id_response.json().get('code') == 1
        assert pet_by_id_response.json().get('type') == 'error'
        assert pet_by_id_response.json().get('message') == 'Pet not found'

    def test_delete_pet_negative(self, petstore_client):
        petstore_client.delete_pet_by_id(PET_TO_DELETE.id)
        delete_response = petstore_client.delete_pet_by_id(PET_TO_DELETE.id)
        assert delete_response.status_code == 404
