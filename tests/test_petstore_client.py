import pytest

from petstore_client import PetClient
from tests.conftest import *


class TestPetClient:

    @pytest.mark.parametrize("pet_data, expected_data", [
        (pet_data_1, pet_data_1),
        (pet_data_2, pet_data_2)
    ])
    def test_add_pet(self, pet_client, pet_data, expected_data):

        add_pet_response = pet_client.add_pet(pet_data)
        data = add_pet_response.json()
        headers = add_pet_response.headers

        assert add_pet_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        result = {k:v for k, v in data.items() if k in expected_data}
        assert result == expected_data

    @pytest.mark.parametrize("bad_pet_data", [
        bad_pet_data_1, bad_pet_data_2
    ])
    def test_add_pet_negative(self, pet_client, bad_pet_data):

        add_pet_response = pet_client.add_pet(bad_pet_data)
        data = add_pet_response.json()

        assert add_pet_response.status_code == 405
        assert data.get("type") == 'error'

    @pytest.mark.parametrize("pet_id, expected_data", [
        (pet_id_1, pet_data_1),
        (pet_id_2, pet_data_2)
    ])
    def test_get_pet(self, pet_client, pet_id, expected_data):

        get_pet_response = pet_client.get_pet(pet_id)
        data = get_pet_response.json()
        headers = get_pet_response.headers

        assert get_pet_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        result = {k:v for k, v in data.items() if k in expected_data}
        assert result == expected_data

    @pytest.mark.parametrize("bad_pet_id", [
        bad_pet_id_1, bad_pet_id_2, bad_pet_id_3
    ])
    def test_get_pet_negative(self, pet_client, bad_pet_id):

        get_pet_response = pet_client.get_pet(bad_pet_id)
        data = get_pet_response.json()
        assert get_pet_response.status_code in (400, 404)
        assert data.get("type") == 'error'


    @pytest.mark.parametrize("pet_data, expected_data", [
        (pet_data_3, pet_data_3),
        (pet_data_4, pet_data_4)
    ])
    def test_update_pet(self, pet_client, pet_data, expected_data):

        update_pet_response = pet_client.update_pet(pet_data)
        data = update_pet_response.json()
        headers = update_pet_response.headers

        assert update_pet_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        result = {k:v for k, v in data.items() if k in expected_data}
        assert result == expected_data

    @pytest.mark.parametrize("pet_id", [
        pet_id_1, pet_id_2
    ])
    def test_delete_pet(self, pet_client, pet_id):

        delete_pet_response = pet_client.delete_pet(pet_id)
        data = delete_pet_response.json()
        headers = delete_pet_response.headers

        assert delete_pet_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        assert data.get("code") == 200
        assert data.get("message") == str(pet_id)

    @pytest.mark.parametrize("bad_pet_id", [
        bad_pet_id_1, bad_pet_id_2, bad_pet_id_3
    ])
    def test_delete_pet_negative(self, pet_client, bad_pet_id):

        delete_pet_response = pet_client.delete_pet(bad_pet_id)

        assert delete_pet_response.status_code == 404

class TestUserClient:

    @pytest.mark.parametrize(
        "user_data",
        [ user_data_1, user_data_2]
    )
    def test_add_user(self, user_client, user_data):

        add_user_response = user_client.add_user(user_data)
        data = add_user_response.json()
        headers = add_user_response.headers

        assert add_user_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        assert data.get("message") == str(user_data["id"])

    @pytest.mark.parametrize("user_data, expected_data", [
        (user_data_1, user_data_1), (user_data_2, user_data_2)
    ])
    def test_get_user(self, user_client, user_data, expected_data):

        get_user_response = user_client.get_user(user_data["username"])
        data = get_user_response.json()
        headers = get_user_response.headers

        assert get_user_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        result = {k:v for k, v in data.items() if k in expected_data}
        assert result == expected_data

    @pytest.mark.parametrize("bad_user_data", [
        bad_user_data_1, bad_user_data_2
    ])
    def test_get_user_negative(self, user_client, bad_user_data):

        get_user_response = user_client.get_user(bad_user_data["username"])
        data = get_user_response.json()

        assert get_user_response.status_code == 404
        assert data.get("type") == 'error'

    @pytest.mark.parametrize("user_data", [
        user_data_3, user_data_4
    ])
    def test_update_user(self, user_client, user_data):

        update_user_response = user_client.update_user(user_data["username"], user_data)
        data = update_user_response.json()
        headers = update_user_response.headers

        assert update_user_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        assert data.get("message") == str(user_data["id"])

    @pytest.mark.parametrize("user_data", [
        user_data_3, user_data_4
    ])
    def test_delete_user(self, user_client, user_data):

        delete_user_response = user_client.delete_user(user_data["username"])
        data = delete_user_response.json()
        headers = delete_user_response.headers

        assert delete_user_response.status_code == 200
        assert headers["Content-Type"] == "application/json"
        assert data.get("message") == user_data["username"]

    @pytest.mark.parametrize("bad_username", [
        bad_user_name_1, bad_user_name_2
    ])
    def test_delete_user_negative(self, user_client, bad_username):

        delete_user_response = user_client.delete_user(bad_username)

        assert delete_user_response.status_code == 404