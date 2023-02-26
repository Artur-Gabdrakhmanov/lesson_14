import requests
from pytest_voluptuous import S
from schemas import user


def test_register_single_user():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    req = requests.post(
        url='https://reqres.in/api/register',
        json={'email': email, 'password': password}
    )

    assert req.status_code == 200
    assert req.json() == S(user.register_single_user)


def test_create_user():
    name = 'Chev'
    job = 'leader'

    req = requests.post(
        url='https://reqres.in/api/users',
        json={'name': name, 'job': job}
    )

    assert req.status_code == 201
    assert req.json() == S(user.create_single_user)
    assert req.json()['name'] == name
    assert req.json()['job'] == job


def test_update_user():
    update_name = 'morpheus'
    update_job = 'follower'

    req = requests.put(
        url='https://reqres.in/api/users/2',
        json={'name': update_name, 'job': update_job}
    )

    assert req.status_code == 200
    assert req.json() == S(user.update_single_user)
    assert req.json()['name'] == update_name
    assert req.json()['job'] == update_job


def test_register_successful():
    email = 'eve.holt@reqres.in'
    password = 'pistol'

    req = requests.post(
        url='https://reqres.in/api/register',
        json={'email': email, 'password': password}
    )

    assert req.status_code == 200
    assert req.json()['id'] == 4
    assert req.json()['token'] == 'QpwL5tke4Pnpja7X4'


def test_register_unsuccessful():
    email = 'sydney@fife'
    password = 'pistol'

    req = requests.post(
        url='https://reqres.in/api/register',
        json={'email': email, 'password': password}
    )

    assert req.status_code == 400


def test_delete_user():
    result = requests.delete(url='https://reqres.in/api/users/2')

    assert result.status_code == 204
