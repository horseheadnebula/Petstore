from api_client import BaseApiClient

class PetStoreClient(BaseApiClient):
    def __init__(self):
        super().__init__("https://petstore.swagger.io/v2")

class PetClient(PetStoreClient):
    def add_pet(self, body):
        response = self.post("/pet", body=body)
        return response

    def get_pet(self, pet_id):
        path = f"/pet/{pet_id}"
        response = self.get(path)
        return response

    def update_pet(self, body):
        response = self.put("/pet", body=body)
        return response

    def delete_pet(self, pet_id):
        path = f"/pet/{pet_id}"
        response = self.delete(path)
        return response

class UserClient(PetStoreClient):
    def add_user(self, body):
        response = self.post("/user", body=body)
        return response

    def get_user(self, username):
        path = f"/user/{username}"
        response = self.get(path)
        return response

    def update_user(self, username, body):
        response = self.put(f"/user/{username}", body=body)
        return response

    def delete_user(self, username):
        path = f"/user/{username}"
        response = self.delete(path)
        return response


