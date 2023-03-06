import requests
import json


header = {'accept': 'application/json', 'Content-Type': 'application/json'}
url = 'https://petstore.swagger.io/v2'

datas = {
    "id": "74530000000000099",
    "username": "IvanIvanov",
    "firstName": "Ivan",
    "lastName": "Ivanov",
    "email": "IvanIvanov@mail.ru",
    "password": "IvanIvanov75839",
    "phone": "8912034567",
    "userStatus": 0
}

"""Запись нового пользователя"""
def test_user_post():
    res_user_post = requests.post(url=f'{url}/user',headers=header, data=json.dumps(datas))
    res_user_json = json.loads(res_user_post.text)
    print(res_user_json)
    assert res_user_post.status_code == 200
"""проверка наличия пользователя"""
def test_user_get():
    res_user_get = requests.get(url=f'{url}/user/{datas["username"]}',headers={'accept': 'application/json'})
    print(res_user_get.text)
    assert res_user_get.status_code == 200
"""вход под пользователем"""
def test_get_user_lodin():

    res_userLogin_get = requests.get(url=f'{url}/user/login?{datas["username"]}&password={datas["password"]}', headers=header)
    print(res_userLogin_get.text)
    assert res_userLogin_get.status_code == 200
"""выход """
def test_get_userlodout():

    res_userLogout_get = requests.get(url=f'{url}/user/logout', headers=header)
    print(res_userLogout_get.text)
    assert res_userLogout_get.status_code == 200
"""обновление данных пользователя"""
def test_user_update():
    data = {
        "id": "74530000000000099",
        "username": "PetrPetrov",
        "firstName": "Petr",
        "lastName": "Petrov",
        "email": "IvanIvanov@mail.ru",
        "password": "IvanIvanov75839",
        "phone": "8912034567",
        "userStatus": 0
    }
    res_user_update_put = requests.put(url=f'{url}/user/{datas["id"]}', headers=header, data=json.dumps(data))
    print(res_user_update_put.text)
    assert res_user_update_put.status_code == 200
"""проверка обнавленных данных"""
def test_user_new_get():
    res_user_new_get = requests.get(url=f'{url}/user/PetrPetrov',headers={'accept': 'application/json'})
    print(res_user_new_get.text)
    assert res_user_new_get.status_code == 200
"""проверка на наличие старых данных"""
def test_user_old_get():
    res_user_new_get = requests.get(url=f'{url}/user/IvanIvanov',headers={'accept': 'application/json'})
    print(res_user_new_get.text)
    assert res_user_new_get.status_code == 404
"""удаление пользователя"""
def test_delete_User():

    res_userdelete_del = requests.delete(url=f'{url}/user/PetrPetrov', headers=header)
    print(res_userdelete_del.text)
    assert res_userdelete_del.status_code == 200
"""проверка удаленного пользователя """
def test_user_new2_get():

    res_user_new_get = requests.get(url=f'{url}/user/PetrPetrov',headers=header)
    print(res_user_new_get.text)
    assert res_user_new_get.status_code == 404
