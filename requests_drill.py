import requests
import logging

logging.basicConfig(
    filename="error.log",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ServerUnreachable(Exception):
    pass

def fetching(URL):
    for i in range(3):
        try:
            response = requests.get(URL, timeout=0.0001)
            print(response.text)
            print(response.status_code)
            break
        except requests.exceptions.ConnectTimeout as e:
            print("Built-in timeout triggered.")
            logging.debug("Custom error: Server unreachable due to timeout")
            raise ServerUnreachable("Server unreachable due to timeout") from e
        finally:
            print("Finally block runs no matter what.")
    else:
        print("Attempt finished.")

try:
    fetching("https://jsonplaceholder.typicode.com/posts/1")
except ServerUnreachable as e:
    print(f"Caught custom error: {e}")
