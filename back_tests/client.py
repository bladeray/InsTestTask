import allure
import requests

from back_tests.models import Pet


class PetstoreClient:
    base_url = 'https://petstore.swagger.io/v2/pet'

    headers_default = {'accept': 'application/json'}

    client = requests.session()

    def __init__(self):
        self.client.headers = self.headers_default

    @allure.step('POST /pet/{pet_id}/uploadImage')
    def upload_images(self, pet_id: int, file_path):
        with open(file_path, 'rb') as f:
            return self.client.post(
                url=f'{self.base_url}/{pet_id}/uploadImage',
                files={'file': f, 'type': 'image/png'}
            )

    @allure.step('POST /pet')
    def create_pet(self, pet: Pet):
        return self.client.post(
            url=self.base_url,
            json=pet.__dict__
        )

    @allure.step('PUT /pet')
    def update_pet(self, pet: Pet):
        return self.client.put(
            url=self.base_url,
            json=pet.__dict__
        )

    @allure.step('GET /pet/findByStatus?status={status}')
    def find_pet_by_status(self, status: str):
        return self.client.get(url=f'{self.base_url}/findByStatus?status={status}')

    @allure.step("GET /pet/{pet_id}")
    def find_pet_by_id(self, pet_id: int):
        return self.client.get(url=f'{self.base_url}/{pet_id}')

    @allure.step('POST /pet/{pet_id}')
    def update_pet_by_id(self, pet_id: int, name: str = None, status: str = None):
        self.headers_default['Content-Type'] = 'application/x-www-form-urlencoded'
        if name is None and status is None:
            data = ''
        elif name is None:
            data = f'status={status}'
        elif status is None:
            data = f'name={name}'
        else:
            data = f'name={name}&status={status}'
        response = self.client.post(url=f'{self.base_url}/{pet_id}',
                                    json=data)
        self.headers_default['Content-Type'] = 'application/json'
        return response

    @allure.step('DELETE /pet/{pet_id}')
    def delete_pet_by_id(self, pet_id: int):
        return self.client.delete(url=f'{self.base_url}/{pet_id}')
