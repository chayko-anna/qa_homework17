import requests
from jsonschema import validate
import schemas
from schemas.schemas_users.py import post_user, register_user, update_user, get_user


def test_create_user():
    response = requests.post("https://reqres.in/api/users", data={"name": "morpheus", "job": "master"})
    assert response.status_code == 201
    body = response.json()
    validate(body, post_user)


def test_get_existing_user_info():
    response = requests.get("https://reqres.in/api/users/2")
    body = response.json()
    assert response.status_code == 200
    validate(body, get_user)


def test_get_not_existing_user_info():
    response = requests.get("https://reqres.in/api/users/77")
    assert response.status_code == 404


def test_update_user():
    response = requests.put("https://reqres.in/api/users/2", data={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200
    body = response.json()
    validate(body, update_user)


def test_register_user_successful():
    response = requests.post("https://reqres.in/api/register",
                             data={"email": "eve.holt@reqres.in", "password": "pistol"})
    assert response.status_code == 200
    body = response.json()
    validate(body, register_user)


def test_register_user_unsuccessful():
    response = requests.post("https://reqres.in/api/register")
    assert response.status_code == 400
    assert response.text == '{"error":"Missing email or username"}'


def test_delete_user_successful():
    response = requests.delete("https://reqres.in/api/users/2")
    assert response.status_code == 204
