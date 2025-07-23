import requests


def post_and_get():
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {'Name': 'Mani', 'Age': '23'}


    post_response = requests.post(url, json=payload)
    print("POST Status:", post_response.status_code)
    print("POST Response:", post_response.json())


    get_response = requests.get(f"{url}/1")
    print("GET Status:", get_response.status_code)
    print("GET Response:", get_response.json())


def customheader():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    headers = {
        "Content-Type": "application/json",
        "Custom-Header": "MyWish"
    }
    response = requests.get(url, headers=headers)
    print("Headers Status:", response.status_code)
    print("Headers Response:", response.json())


def forparams():
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {
        "postId": 1
    }
    response = requests.get(url, params=params)
    print("Params Status:", response.status_code)
    print("Params Response:", response.json())


def forauth():
    url = "https://api.github.com/user"
    username = "Manikantachavvakula"
    token = "token"
    response = requests.get(url, auth=(username, token))
    print("Auth Status:", response.status_code)
    print("Auth Response:", response.json())


def put_example():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {"id": 1, "title": "Updated Title", "body": "Updated Body", "userId": 1}
    response = requests.put(url, json=payload)
    print("PUT Status:", response.status_code)
    print("PUT Response:", response.json())

def patch_example():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    payload = {"title": "Patched Title"}
    response = requests.patch(url, json=payload)
    print("PATCH Status:", response.status_code)
    print("PATCH Response:", response.json())

def delete_example():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.delete(url)
    print("DELETE Status:", response.status_code)
    print("DELETE Response:", response.text)  


post_and_get()
customheader()
forparams()
forauth()
put_example()
patch_example()
delete_example()
