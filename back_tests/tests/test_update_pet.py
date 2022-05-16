import pytest

from back_tests.consts import PET_UPDATED_ONLY_ID, PET_UPDATED_FULL, ROOT_DIR


class TestUpdatePet:
    @pytest.mark.parametrize(
        'changed_pet', [
            pytest.param(PET_UPDATED_FULL, id='full updated'),
            pytest.param(PET_UPDATED_ONLY_ID, id='leave only id')
        ])
    def test_update_existing_pet_positive(self, petstore_client, petstore_checker, created_pet, changed_pet):
        assert created_pet.id == changed_pet.id
        update_response = petstore_client.update_pet(changed_pet)
        assert update_response.status_code == 200
        petstore_checker.check_pet(changed_pet)

    def test_update_existing_pet_negative(self, petstore_client, created_pet):
        petstore_client.delete_pet_by_id(created_pet.id)
        update_response = petstore_client.update_pet(created_pet)
        assert update_response.status_code == 404

    # @pytest.mark.parametrize(
    #     'name, status', [
    #         pytest.param(None, None, id='name and status are None'),
    #         pytest.param('Jack', None, id='only status is None'),
    #         pytest.param(None, 'sold', id='only name is None'),
    #         pytest.param('Jack', 'sold', id='name and status are filled'),
    #     ])
    # def test_update_pet_by_id_positive(self, petstore_client, petstore_checker, created_pet, name, status):
    #     update_response = petstore_client.update_pet_by_id(pet_id=created_pet.id, name=name, status=status)
    #     assert update_response.status_code == 200
    #     assert update_response.json().get('code') == 200
    #     assert update_response.json().get('type') == 'unknown'
    #     assert update_response.json().get('message') == str(created_pet.id)
    #     if name is not None:
    #         created_pet.name = name
    #     if status is not None:
    #         created_pet.status = status
    #     # petstore_client().find_pet_by_id(created_pet.id).json()
    #     petstore_checker.check_pet(created_pet)

    def test_upload_images(self, petstore_client, created_pet):
        upload_images_response = petstore_client.upload_images(created_pet.id, f'{ROOT_DIR}/2.png')
        assert upload_images_response.status_code == 200
        assert upload_images_response.json().get('code') == 200
        assert upload_images_response.json().get('type') == 'unknown'
        assert upload_images_response.json().get('message') != ''
