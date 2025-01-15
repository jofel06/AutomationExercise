from utils.api_helpers import send_request

def test_get_products_list():
    response = send_request("productsList", method="GET")
    assert response.status_code == 200
    assert "products" in response.json(), f"Error, List of Products not found in the response, got status code {response.status_code}"

def test_post_all_product_list():
    response = send_request("productsList", method="POST")
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json().get("responseCode") == 405, "Expected response code 405, but got different"
    assert response.json().get("message") == "This request method is not supported.", "Response message different than what was expected"

def test_post_search_product():
    params = {"search_product": "Tops"}
    response = send_request("searchProduct", method="POST", params=params)
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json().get("responseCode") == 400, "Expected response code 400, but got different"
    assert response.json().get("message") == "Bad request, search_product parameter is missing in POST request.", \
        "Response message different than what was expected"

def test_post_search_product_without_search_product_parameter():
    response = send_request("searchProduct", method="POST")
    assert response.status_code == 200, f"Expected 200, but got {response.status_code}"
    assert response.json().get("responseCode") == 400, "Expected response code 400, but got different"
    assert response.json().get("message") == "Bad request, search_product parameter is missing in POST request.", \
        "Response message different than what was expected"