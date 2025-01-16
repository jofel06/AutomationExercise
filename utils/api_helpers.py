import requests
import logging

base_url =  "https://automationexercise.com/api"
logger = logging.getLogger(__name__)

def send_request(endpoint, method="GET", headers=None, params=None, data=None):

    URL = f"{base_url}/{endpoint}" #this assigns the combination of base URL itself endpoint to the URL
    response = None

    logging.info(f"Sending {method} request to: {URL} with params: {params} and data: {data}")
    if method == "GET":
        response = requests.get(URL, headers=headers, params=params)
    elif method == "POST":
        response = requests.post(URL, headers=headers, data=data) #use Json as this methods usually sends data using Json format
    elif method == "PUT":
        response = requests.put(URL, headers=headers, data=data)
    elif method == "PATCH":
        response = requests.put(URL, headers=headers, data=data)
    elif method == "DELETE":
        response = requests.delete(URL, headers=headers, data=data)

    if response is not None:
        logging.info(f"Received response status code: {response.status_code} with body: {response.json()}")

    return response