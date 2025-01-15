from utils.api_helpers import send_request

def test_get_products_list():
    response = send_request("productsList", method="GET")
    assert response.status_code == 200
    assert "products" in response.json(), "Error, productsList not found in the response"

def test_post_all_product_list():
    response = send_request("productsList", method="POST")
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json().get("responseCode") == 405, "Expected responseCode 405, but got different"
    assert response.json().get("message") == "This request method is not supported.", "Expected error message"