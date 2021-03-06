from back_tests.client import PetstoreClient
from back_tests.models import Pet


class PetstoreChecker:
    def check_pet(self, expected_data: Pet):
        pet_by_id = PetstoreClient().find_pet_by_id(expected_data.id).json()
        assert pet_by_id.get('id') == expected_data.id
        assert pet_by_id.get('category') == expected_data.category
        assert pet_by_id.get('name') == expected_data.name
        assert pet_by_id.get('photoUrls') == expected_data.photoUrls
        assert pet_by_id.get('tags') == expected_data.tags
        assert pet_by_id.get('status') == expected_data.status

    def check_update_response(self, response, expected_code: int, message: str):
        assert response.status_code == expected_code, response.status_code
        assert response.json().get('code') == expected_code
        assert response.json().get('type') == 'unknown'
        assert message in response.json().get('message')
