from petstore_client import PetClient, UserClient

# #----------PET----------
# pet_client = PetClient()
#
# add_pet_response = pet_client.add_pet(
#     {
#     "id": 9606,
#     "name": "Octavian",
#     "status": "available",
#     "category": {
#         "id": 1,
#         "name": "cat"
#     }
# })
# print("Status code:", add_pet_response.status_code)
# print(add_pet_response.json())
#
# get_pet_response = pet_client.get_pet(9606)
# print("Status code:", get_pet_response.status_code)
# print(get_pet_response.json())
#
# update_pet_response = pet_client.update_pet({
#     "id": 9606,
#     "name": "Octavian",
#     "status": "sold"
# })
# print("Status code:", update_pet_response.status_code)
# print(update_pet_response.json())
#
# delete_pet_response = pet_client.delete_pet(9606)
# print("Status code:", delete_pet_response.status_code)
# print(delete_pet_response.json())

# #----------USER----------
# user_client = UserClient()
#
# add_user_response = user_client.add_user({
#     "id": 9101,
#     "username": "horsehead",
#     "firstName": "John",
#     "lastName": "Doe",
#     "email": "example@email.com",
#     "password": "1234567890",
#     "userStatus": 1
# })
# print(add_user_response.status_code)
# print(add_user_response.json())
#
# get_user_response = user_client.get_user("horsehead")
#
# print(get_user_response.status_code)
# print(get_user_response.json())
#
# update_user_response = user_client.update_user("horsehead", {
#     "id": 9101,
#     "username": "horsehead",
#     "firstName": "John",
#     "lastName": "Doe",
#     "email": "example@email.com",
#     "password": "1234567890",
#     "phone": "+123456789",
#     "userStatus": 1
# })
# print(update_user_response.status_code)
# print(update_user_response.json())
#
# delete_user_response = user_client.delete_user("horsehead")
#
# print(delete_user_response.status_code)
# print(delete_user_response.json())