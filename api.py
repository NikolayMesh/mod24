import requests
import json
from input import email, password, auth_key, id

def test_get_api_key():
    header = {'accept': 'application/json', 'email': email, 'password': password}

    res_api_key_get = requests.get(url='https://petfriends.skillfactory.ru/api/key', headers=header)
    assert res_api_key_get.status_code == 200
    print(res_api_key_get.text)
    test = json.loads(res_api_key_get.text)
   

def test_add_pet():
    input_pet = {'name':'Bob',
    'animal_type':"Shepherd",
    "age":"2"
    }
    header = {'accept': 'application/json', "auth_key": auth_key}

    res_test_add_pet_post = requests.post(url='https://petfriends.skillfactory.ru/api/create_pet_simple', data=json.dumps(input_pet), headers=header)
    assert res_test_add_pet_post.status_code == 200
    print(res_test_add_pet_post.text)
    test = json.loads(res_test_add_pet_post.text)
    iD = {test["id"]}
    print(iD)
    

def test_get_api_pets():
    header = {'accept': 'application/json', "auth_key": auth_key}

    res_api_pets_get = requests.get(url='https://petfriends.skillfactory.ru/api/pets', headers=header)
    assert res_api_pets_get.status_code == 200
    print(res_api_pets_get.text)


def test_Update_pets_put():
    header = {'accept': 'application/json', "auth_key": auth_key, "Content-Type": "multipart/form-data"}
    data = {"name":"Reks",
            "animal_type":"Dvorterer",
            "age":"10"
            }

    res_Update_pets_put_put = requests.put(url=f'https://petfriends.skillfactory.ru/api/pets/{id}', headers=header, data=json.dumps(data))
    assert res_Update_pets_put_put.status_code == 200
    print(res_Update_pets_put_put.text)
    pet = json.loads(res_Update_pets_put_put.text)
    name = {pet["name"]}
    name_new = {data["name"]}
    assert name == name_new








def test_delete_pets():
    header = {'accept': 'application/json', "auth_key": auth_key}

    res_test_delete_pets_del = requests.delete(url='petfriends.skillfactory.ru/api/pets/45d8ef48-faff-4ce0-903a-d4b53b6df467', headers=header)
    assert res_test_delete_pets_del.status_code == 200
    print(res_test_delete_pets_del.text)
