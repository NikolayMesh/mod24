import requests
import json
from settings import User, Userlist, User_up, pet, store_pet

"""---------------------------------PET---------------------------------------------------------------"""
def test_add_pet():  ## добавление нового петомца поиск по  id
    input_pet = pet

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    res_post = requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    print(res_post.text)
    res_json = json.loads(res_post.text)
    assert input_pet == res_json

    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/{input_pet["id"]}')

    assert res_get.status_code == 200
    assert json.loads(res_get.text) == input_pet


def test_available_list():  ## проверка статуса available
    input_pet = pet
    header = {'accept': 'application/json', 'Content-Type': 'application/json'}

    requests.post(url='https://petstore.swagger.io/v2/pet', data=json.dumps(input_pet), headers=header)
    res_get = requests.get(url=f'https://petstore.swagger.io/v2/pet/findByStatus', params={'status': 'available'})

    assert res_get.status_code == 200
    assert input_pet in list(json.loads(res_get.text))
    print(list(json.loads(res_get.text)))


def test_pet_Update_name_state(): ## обновление имени и статуса

    header = {'accept': 'application/json'}
    Update = {'name':'dog','status':'sold'}
    res_pet_Update_name_state_post = requests.post(url=f'https://petstore.swagger.io/v2/pet/{pet["id"]}',
                                                   headers=header, data =  Update)
    print(res_pet_Update_name_state_post.text)
    assert res_pet_Update_name_state_post.status_code == 200


def test_uploadImage():

    header = {'accept': 'application/json','Content-Type': 'multipart/form-data'}
    image = open('dog.jpg', 'rb')


    files = {'file': image, 'type': 'image/jpeg'}
    res_uploadImage_post = requests.post(url=f'https://petstore.swagger.io/v2/pet/{pet["id"]}/uploadImage',
                                                   headers=header, files=files)
    print(res_uploadImage_post.text)
    assert res_uploadImage_post.status_code == 200



"""---------------------------------STORE---------------------------------------------------------------"""


def test_StoreOrder():

    header = {'accept': 'application/json','Content-Type': 'multipart/form-data'}
    res_StoreOrder_post = requests.post(url='https://petstore.swagger.io/v2/store/order',
                                                   headers=header, data=store_pet)
    print(res_StoreOrder_post.text)
    assert res_StoreOrder_post.status_code == 200



"""-------------------------------------StoreInventory--------------------------------------------------------"""


def test_StoreInventory():
    header = {'accept': 'application/json'}

    res_StoreInventory_get = requests.get(url='https://petstore.swagger.io/v2/store/inventory', headers=header)

    print(res_StoreInventory_get.text)
    assert res_StoreInventory_get.status_code == 200


"""-------------------------------------DeleteOrderIDy--------------------------------------------------------"""


def test_DeleteOrderID():
    header = {'accept': 'application/json'}

    res_DeleteOrderID_del = requests.delete(url='https://petstore.swagger.io/v2/store/order/0', headers=header)

    print(res_DeleteOrderID_del.text)
    assert res_DeleteOrderID_del.status_code == 200



"""-------------------------------------StoreOrderID--------------------------------------------------------"""


def test_StoreOrderID():
    header = {'accept': 'application/json'}

    res_StoreOrderID_get = requests.get(url='https://petstore.swagger.io/v2/store/order/0', headers=header)

    print(res_StoreOrderID_get.text)
    assert res_StoreOrderID_get.status_code == 200



"""---------------------------------USER----------------------------------------------------------"""



def test_create_User():  ## создание нового пользователя
    input_user = User

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    res_user_post = requests.post(url='https://petstore.swagger.io/v2/user', data=json.dumps(input_user),
                                  headers=header)
    res_user_json = json.loads(res_user_post.text)
    print(res_user_json)
    assert res_user_post.status_code == 200


def test_get_UserLodin():  ## вход в учетную запись

    header = {'accept': 'application/json'}
    res_userLogin_get = requests.get(url=f'https://petstore.swagger.io/v2/user/login?{User["username"]}&password={User["password"]}', headers=header)
    print(res_userLogin_get.text)
    assert res_userLogin_get.status_code == 200


def test_get_UserName():  ## получение имени

    header = {'accept': 'application/json'}
    res_user_get_name = requests.get(url=f'https://petstore.swagger.io/v2/user/{User["username"]}', headers=header)
    print(res_user_get_name.text)
    assert res_user_get_name.status_code == 200


def test_put_UpdateUser():  ## обновление записи

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    res_user_get_name = requests.get(url=f'https://petstore.swagger.io/v2/user/{User["username"]}',
                                     data=json.dumps(User_up), headers=header)
    print(res_user_get_name.text)
    assert res_user_get_name.status_code == 200


def test_get_UserLodout():  ## выход из учетной записи

    header = {'accept': 'application/json'}
    res_userLogout_get = requests.get(url='https://petstore.swagger.io/v2/user/logout', headers=header)
    print(res_userLogout_get.text)
    assert res_userLogout_get.status_code == 200


def test_create_UserWithArray():  ## создание учтных записей массивом

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    res_UserArray_post = requests.post(url='https://petstore.swagger.io/v2/user/createWithArray',
                                       data=json.dumps(Userlist), headers=header)
    print(res_UserArray_post)
    assert res_UserArray_post.status_code == 200


def test_create_UserWithList():  ## создание учетных записей списком

    header = {'accept': 'application/json', 'Content-Type': 'application/json'}
    res_UserList_post = requests.post(url='https://petstore.swagger.io/v2/user/createWithList',
                                      data=json.dumps(Userlist), headers=header)
    print(res_UserList_post.text)
    assert res_UserList_post.status_code == 200


def test_delete_User():  ##удаление учетной записи

    header = {'accept': 'application/json'}
    res_userdelete_del = requests.delete(url=f'https://petstore.swagger.io/v2/user/{User["username"]}', headers=header)
    print(res_userdelete_del.text)
    assert res_userdelete_del.status_code == 200
