import pytest
from tests.conftest import pet_data1, pet_data2


class TestPetClient:

    @pytest.mark.parametrize("pet_data, expected", [
        (pet_data1, pet_data1),
        (pet_data2, pet_data2)
    ])
    def test_add_pet(self, client, pet_data, expected):
        add_pet_response = client.add_pet(pet_data)
        data = add_pet_response.json()
        headers = add_pet_response.headers

        assert add_pet_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        # result = {}
        # for k in data:
        #     if k in expected:
        #         result[k] = data[k]
        result = {k:v for k, v in data.items() if k in expected}
        assert result == expected

    def test_get_pet(self, client):
        # client.add_pet({
        #     "id": 9606,
        #     "name": "Octavian",
        #     "status": "available",
        #     "category": {
        #         "id": 1,
        #         "name": "cat"
        #     }
        # })
        get_pet_response = client.get_pet(9606)
        data = get_pet_response.json()
        headers = get_pet_response.headers

        assert get_pet_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        assert data["id"] == 9606
        assert data["name"] == "Octavian"
        assert data["status"] == "available"
        assert data["category"]["id"] == 1
        assert data["category"]["name"] == "cat"

#     def test_update_pet(self):
#         client = PetClient()
#         client.add_pet({
#             "id": 9606,
#             "name": "Octavian",
#             "status": "available",
#             "category": {
#                 "id": 1,
#                 "name": "cat"
#             }
#         })
#         update_pet_response = client.update_pet({
#             "id": 9606,
#             "name": "Octavian",
#             "status": "sold"
#         })
#         data = update_pet_response.json()
#         headers = update_pet_response.headers
#
#         assert update_pet_response.status_code == 200
#         assert headers["Content-Type"] == "application/json"
#         assert data["id"] == 9606
#         assert data["name"] == "Octavian"
#         assert data["status"] == "sold"
#
#     def test_delete_pet(self):
#         client = PetClient()
#         client.add_pet({
#             "id": 9606,
#             "name": "Octavian",
#             "status": "available",
#             "category": {
#                 "id": 1,
#                 "name": "cat"
#             }
#         })
#         delete_pet_response = client.delete_pet(9606)
#         data = delete_pet_response.json()
#         headers = delete_pet_response.headers
#
#         assert delete_pet_response.status_code == 200
#         assert headers["Content-Type"] == "application/json"
#         assert data.get("code") == 200
#         assert data.get("message") == "9606"
#
# class TestUserClient:
#     def test_add_user(self):
#         client = UserClient()
#         add_user_response = client.add_user({
#             "id": 9101,
#             "username": "horsehead",
#             "firstName": "John",
#             "lastName": "Doe",
#             "email": "example@email.com",
#             "password": "1234567890",
#             "userStatus": 1
#         })
#         data = add_user_response.json()
#         headers = add_user_response.headers
#
#         assert add_user_response.status_code == 200
#         assert headers["Content-Type"] == "application/json"
#         assert data.get("code") == 200
#         assert data.get("message") == '9101'
#
#
#     def test_get_user(self):
#         client = UserClient()
#         client.add_user({
#             "id": 9101,
#             "username": "horsehead",
#             "firstName": "John",
#             "lastName": "Doe",
#             "email": "example@email.com",
#             "password": "1234567890",
#             "userStatus": 1
#         })
#         get_user_response = client.get_user("horsehead")
#         data = get_user_response.json()
#         headers = get_user_response.headers
#
#         assert get_user_response.status_code == 200
#         assert headers["Content-Type"] == "application/json"
#         assert data["id"] == 9101
#         assert data["username"] == "horsehead"
#         assert data["userStatus"] == 1
#
#     def test_update_user(self):
#         client = UserClient()
#         client.add_user({
#             "id": 9101,
#             "username": "horsehead",
#             "firstName": "John",
#             "lastName": "Doe",
#             "email": "example@email.com",
#             "password": "1234567890",
#             "userStatus": 1
#         })
#         update_user_response = client.update_user("horsehead", {
#             "id": 9101,
#             "username": "horsehead",
#
#             "firstName": "John",
#             "lastName": "Doe",
#             "email": "example@email.com",
#             "password": "1234567890",
#             "phone": "+1234567890",
#             "userStatus": 1
#
#         })
#         data = update_user_response.json()
#         headers = update_user_response.headers
#
#         assert update_user_response.status_code == 200
#         assert headers["Content-Type"] == "application/json"
#         assert data.get("message") == '9101'
#
#     def test_delete_user(self):
#         client = UserClient()
#         client.add_user({
#             "id": 9101,
#             "username": "horsehead",
#             "firstName": "John",
#             "lastName": "Doe",
#             "email": "example@email.com",
#             "password": "1234567890",
#             "userStatus": 1
#         })
#         delete_user_response = client.delete_user("horsehead")
#         data = delete_user_response.json()
#         headers = delete_user_response.headers
#
#         assert delete_user_response.status_code == 200
#         assert headers["Content-Type"] == "application/json"
#         assert data.get("code") == 200
#         assert data.get("message") == "horsehead"