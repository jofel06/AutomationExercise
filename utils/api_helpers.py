import requests

base_url =  "https://automationexercise.com/api"

def send_request(endpoint, method="GET", headers=None, params=None, data=None):


    URL = f"{base_url}/{endpoint}" #this assigns the combination of base URL itself endpoint to the URL
    response = None

    if method == "GET":
        response = requests.get(URL, headers=headers, params=params)
    elif method == "POST":
        response = requests.post(URL, headers=headers, json=data) #use Json as this methods usually sends data using Json format
    elif method == "PUT":
        response = requests.put(URL, headers=headers, json=data)
    elif method == "PATCH":
        response = requests.put(URL, headers=headers, json=data)
    elif method == "DELETE":
        response = requests.delete(URL, headers=headers)

    return response