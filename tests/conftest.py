import pytest
from petstore_client import PetClient

@pytest.fixture(scope="session")
def client():
    client = PetClient()
    return client


@pytest.fixture(scope="session", autouse=True)
def prepare_environment():
    print("Подготовка тестовой среды")
    yield
    print("\nОчистка тестовой среды")

pet_data1 = {
            "id": 9606,
            "name": "Octavian",
            "status": "available",
            "category": {
                "id": 1,
                "name": "cat"
            }
        }

pet_data2 = {
            "id": 6854,
            "name": "Bark",
            "category": {
                "id": 1,
                "name": "dog"
            }
}

