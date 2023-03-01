import json

import requests

credentials = {"email":"marius.sorin@test.com","password":"MariusTest"}
credentials_negative = {"email":"marius.sorin@test.com","password":"Marius"}

def test_login_negative():
    response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login')
    assert response.status_code ==401

def test_login():
    response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login', json=credentials)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["user"]["firstName"]=="Marius"
    assert response_body["user"]["email"] == "marius.sorin@test.com"

def test_login_negative2():
    response = requests.post('https://thinking-tester-contact-list.herokuapp.com/users/login', json=credentials_negative)
    assert response.status_code == 401