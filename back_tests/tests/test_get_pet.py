import uuid

import pytest

from back_tests.consts import ID_FIND_BY_ID, ID_FIND_BY_STATUS
from back_tests.models import Pet


class TestGetPet:
    def test_get_pet_by_id_positive(self, petstore_client, petstore_checker, created_pet):
        pet_by_id_response = petstore_client.find_pet_by_id(created_pet.id)
        assert pet_by_id_response.status_code == 200
        petstore_checker.check_pet(created_pet)

    def test_get_pet_by_id_negative(self, petstore_client):
        petstore_client.delete_pet_by_id(ID_FIND_BY_ID)
        pet_by_id_response = petstore_client.find_pet_by_id(ID_FIND_BY_ID)
        assert pet_by_id_response.status_code == 404
        assert pet_by_id_response.json().get('code') == 1
        assert pet_by_id_response.json().get('type') == 'error'
        assert pet_by_id_response.json().get('message') == 'Pet not found'

    @pytest.mark.parametrize(
        'status', [
            pytest.param('available', id='\"available\" status'),
            pytest.param('pending', id='\"pending\" status'),
            pytest.param('sold', id='\"sold\" status'),
            pytest.param(str(uuid.uuid4()), id='random uuid4 status')
        ])
    def test_get_pet_by_status_positive(self, petstore_client, status):
        petstore_client.delete_pet_by_id(ID_FIND_BY_STATUS)
        petstore_client.create_pet(Pet(pet_id=ID_FIND_BY_STATUS, status=status))
        pet_by_status_response = petstore_client.find_pet_by_status(status)
        assert pet_by_status_response.status_code == 200
        added_pet = [pet for pet in pet_by_status_response.json() if pet.get('id') == ID_FIND_BY_STATUS]
        assert len(added_pet) == 1
        assert added_pet[0].get('id') == ID_FIND_BY_STATUS
        assert added_pet[0].get('status') == status

