import allure
import requests

from back_tests.models import Pet


class PetstoreClient:
    base_url = 'https://petstore.swagger.io/v2/pet'

    headers_default = {'accept': 'application/json'}

    client = requests.session()

    def __init__(self):
        self.client.headers = self.headers_default

    def upload_images(self, pet_id: int, additional_metadata: str, file_path):
        if file_path is None:
            self.headers_default['Content-Type'] = 'multipart/form-data'
            response = self.client.post(
                url=f'{self.base_url}/{pet_id}/uploadImage',
                data={'additionalMetadata': additional_metadata}
            )
            self.headers_default['Content-Type'] = 'application/json'
            return response
        else:
            if self.client.headers.get('Content-Type') is not None:
                self.client.headers.pop('Content-Type')
            return self.client.post(
                url=f'{self.base_url}/{pet_id}/uploadImage',
                data={'additionalMetadata': additional_metadata},
                files={'file': open(file_path, 'rb')}
            )

    def create_pet(self, pet: Pet):
        return self.client.post(
            url=self.base_url,
            json=pet.__dict__
        )

    def update_pet(self, pet: Pet):
        return self.client.put(
            url=self.base_url,
            json=pet.__dict__
        )

    def find_pet_by_status(self, status: str):
        return self.client.get(url=f'{self.base_url}/findByStatus?status={status}')

    def find_pet_by_id(self, pet_id: int):
        return self.client.get(url=f'{self.base_url}/{pet_id}')

    def update_pet_by_id(self, pet_id: int, name: str = None, status: str = None):
        self.headers_default['Content-Type'] = 'application/x-www-form-urlencoded'
        data = {'name': name,
                'status': status}
        response = self.client.post(url=f'{self.base_url}/{pet_id}',
                                    data=data)
        self.headers_default['Content-Type'] = 'application/json'
        return response

    def delete_pet_by_id(self, pet_id: int):
        return self.client.delete(url=f'{self.base_url}/{pet_id}')
