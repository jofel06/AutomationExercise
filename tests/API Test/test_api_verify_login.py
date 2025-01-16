from utils.api_helpers import send_request

def test_post_to_verify_login_with_valid_detail():
    data = {"email": "sampleuser01@yahoo.com",
              "password": "thisispass01"}
    response = send_request("verifyLogin", method="POST", data=data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json().get("message") == "User exists!", "Response messsage different than what was expected"

def test_post_to_verify_login_without_an_email_parameter():
    data = {"password": "randompassword"}
    response = send_request("verifyLogin", method="POST", data=data)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json().get("responseCode") == 400, "Expected response code 400, but got different"
    assert response.json().get("message") == "Bad request, email or password parameter is missing in POST request.", \
        "Response message different than what was expected"