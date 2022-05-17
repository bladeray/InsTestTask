import allure
import pytest

from back_tests.consts import PET_UPDATED_ONLY_ID, PET_UPDATED_FULL, ROOT_DIR


@allure.story('Update pet')
class TestUpdatePet:
    @pytest.mark.parametrize(
        'changed_pet', [
            pytest.param(PET_UPDATED_FULL, id='full updated'),
            pytest.param(PET_UPDATED_ONLY_ID, id='leave only id')
        ])
    def test_update_existing_pet_positive(self, petstore_client, petstore_checker, created_pet, changed_pet):
        with allure.step('Check that created pet and pet for changing ids are same'):
            assert created_pet.id == changed_pet.id
        with allure.step('Send requests'):
            update_response = petstore_client.update_pet(changed_pet)
        with allure.step('Check response code'):
            assert update_response.status_code == 200
        with allure.step('Check that pet is changed'):
            petstore_checker.check_pet(changed_pet)

    @pytest.mark.parametrize(
        'name, status', [
            pytest.param(None, None, id='name and status are None'),
            pytest.param('Jack', None, id='only status is None'),
            pytest.param(None, 'sold', id='only name is None'),
            pytest.param('Jack', 'sold', id='name and status are filled'),
        ])
    def test_update_pet_by_id(self, petstore_client, petstore_checker, created_pet, name, status):
        with allure.step('Send requests'):
            update_response = petstore_client.update_pet_by_id(pet_id=created_pet.id, name=name, status=status)
        with allure.step('Check response structure'):
            petstore_checker.check_update_response(update_response, 200, str(created_pet.id))
        with allure.step('Check that pet is changed'):
            if name is not None:
                created_pet.name = name
            if status is not None:
                created_pet.status = status
            petstore_checker.check_pet(created_pet)

    @pytest.mark.parametrize(
        'metadata, file_path, expected_code, message', [
            pytest.param(None, None, 400, 'org.jvnet.mimepull.MIMEParsingException: Missing start boundary',
                         id='(negative) metadata and file is None'),
            pytest.param(None, f'{ROOT_DIR}/small_image.png', 200,
                         'additionalMetadata: null\nFile uploaded to ./small_image.png,', id='only file request'),
            pytest.param('Some data for full test', f'{ROOT_DIR}/big_image.png', 200,
                         'additionalMetadata: Some data for full test\nFile uploaded to ./big_image.png,',
                         id='metadata and big file request')
        ])
    def test_upload_images(self, petstore_client, petstore_checker, created_pet, metadata, file_path, expected_code,
                           message):
        with allure.step('Send requests'):
            upload_images_response = petstore_client.upload_images(created_pet.id, metadata, file_path)
        with allure.step('Check response structure'):
            petstore_checker.check_update_response(upload_images_response, expected_code, message)
