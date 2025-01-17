from utils.api_helpers import send_request

def test_post_to_create_register_user_account():
    data = {
    "name": "steven",
    "email": "mysample010101999@yahoo.com",
    "password": "randompass01",
    "title": "Mr",
    "birth_date": "1",
    "birth_month": "2",
    "birth_year": "2001",
    "firstname": "steven jay",
    "lastname": "ronalds",
    "company": "Google",
    "address1": "this is address 1",
    "address2": "this is address 2",
    "country": "canada",
    "zipcode": "1111",
    "state": "this is state",
    "city": "this is city",
    "mobile_number": "09234561234"
    }

    response = send_request("createAccount", method="POST", data=data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json().get("responseCode") == 201, "Expected response code 201, but got different"
    assert response.json().get("message") == "User created!", \
        "Response message different than what was expected"

def test_get_user_account_by_email():
    params = {"email": "mysample010101999@yahoo.com"}
    response = send_request("getUserDetailByEmail", method="GET", params=params)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"


def test_to_delete_user_account():
    data = {"email": "mysample010101999@yahoo.com",
    "password": "randompass01"}

    response = send_request("deleteAccount", method="DELETE", data=data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json().get("responseCode") == 200, "Expected response code 200, but got different"
    assert response.json().get("message") == "Account deleted!", \
        "Response message different than what was expected"

