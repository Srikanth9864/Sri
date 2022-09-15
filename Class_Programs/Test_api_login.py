from requests import request
from json import loads, dumps

# d = {"a": 1, "b": 2}

# # Serilisation
# # Converting python DS to JSON string for HTTP transmission
# json_string = dumps(d)

# print(json_string)

def test_login_positive():
    url = "https://reqres.in/api/login"
    payload = {
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            }
    response = request("POST", url, json=payload)
    print(response.status_code)
    # Verify the response code
    assert response.status_code == 200
    json_string = response.text
    print(json_string)
    # De-serialise
    json_object = loads(json_string)
    actual_token = json_object['token']
    assert actual_token == "QpwL5tke4Pnpja7X4"


def test_login_negative_missing_password():
    url = "https://reqres.in/api/login"
    payload = {
                "email": "eve.holt@reqres.in",
            }
    response = request("POST", url, json=payload)
    print(response.status_code)
    json_string = response.text
    print(json_string)
    # Verify the response code
    assert response.status_code == 400
    # De-serialise
    json_object = loads(json_string)
    actual_token = json_object['error']
    assert actual_token == "Missing password"

def test_login_negative_missing_email():
    url = "https://reqres.in/api/login"
    payload = {
                "password": "cityslicka"
            }
    response = request("POST", url, json=payload)
    print(response.status_code)
    json_string = response.text
    print(json_string)
    # Verify the response code
    assert response.status_code == 400
    # De-serialise
    json_object = loads(json_string)
    actual_token = json_object['error']
    assert actual_token == "Missing email or username"