from utils.api_helpers import send_request

def test_get_brands_list():
    response = send_request("brandsList", method="GET")
    assert response.status_code == 200
    assert "brands" in response.json(), f"Error, List of Brands not found in the response, got status code {response.status_code}"

def test_put_all_brand_list():
    response = send_request("brandsList", method="PUT")
    assert response.status_code == 200
    assert response.json().get("responseCode") == 405, f"Expected response code 405, but got different"
    assert response.json().get("message") == "This request method is not supported.", "Response message different than what was expected"