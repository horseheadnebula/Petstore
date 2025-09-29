import pytest
from petstore_client import PetClient, UserClient

@pytest.fixture(scope="session")
def pet_client():
    pet_client = PetClient()
    return pet_client

@pytest.fixture(scope="session")
def user_client():
    user_client = UserClient()
    return user_client

@pytest.fixture(scope="session", autouse=True)
def prepare_environment():
    print("Подготовка тестовой среды")
    yield
    print("\nОчистка тестовой среды")

pet_data_1, pet_data_2, pet_data_3, pet_data_4 = {
            "id": 9606,
            "name": "Octavian",
            "status": "available",
            "category": {
                "id": 1,
                "name": "cat"
            }
        }, {
            "id": 6854,
            "name": "Barky",
            "category": {
                "id": 1,
                "name": "dog"
            }
        }, {
            "id": 9606,
            "name": "Octavian",
            "status": "sold",
            "category": {
                "id": 1,
                "name": "cat"
            }
        }, {
            "id": 6854,
            "name": "Howly",
            "category": {
                "id": 1,
                "name": "dog"
            }
        }

bad_pet_data_1 , bad_pet_data_2 = {
            "id": 9606,
            "name": '',
            "status": "available",
            "category": {
                "id": 1,
                "name": "cat"
            }
        }, {
            "id": "ghj",
            "name": "Barky",
            "category": {
                "id": 1,
                "name": "dog"
            }
        }

pet_id_1, pet_id_2 = 9606, 6854
bad_pet_id_1, bad_pet_id_2, bad_pet_id_3 = 9999999, 0, -1

user_data_1, user_data_2, user_data_3, user_data_4 = {
            "id": 9101,
            "username": "horsehead",
            "firstName": "John",
            "lastName": "Doe",
            "email": "example@email.com",
            "password": "1234567890",
            "userStatus": 1
        }, {
            "id": 7854,
            "username": "joknio",
            "firstName": "Jane",
            "lastName": "Doe",
            "email": "example@email.com",
            "password": "1234567890",
            "phone": "+123456789",
            "userStatus": 1
        }, {
            "id": 9101,
            "username": "horsehead",
            "firstName": "John",
            "lastName": "Doe",
            "email": "example@email.com",
            "password": "1234567890",
            "userStatus": 1
        }, {
            "id": 7854,
            "username": "joknio",
            "firstName": "Jane",
            "lastName": "Doe",
            "email": "example@email.com",
            "password": "1234567890",
            "phone": "+123456789",
            "userStatus": 1
        }

bad_user_data_1, bad_user_data_2 = {
            "id": 9101,
            "username": "9827878",
            "firstName": "John",
            "lastName": "Doe",
            "email": "example@email.com",
            "password": "1234567890",
            "userStatus": 1
        }, {
            "id": 7854,
            "username": "!@#$%^&^%$#@!",
            "firstName": "Jane",
            "lastName": "Doe",
            "email": "example@email.com",
            "password": "1234567890",
            "phone": "+123456789",
            "userStatus": 1
        }
bad_user_name_1, bad_user_name_2 = "9827878", "!@#$%^&^%$#@!"
user_id_1, user_id_2 = 9101, 7854

