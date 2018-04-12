
import requests
with open("key", "r") as f:
    key = f.read().strip()
with open("token", "r") as f:
    token = f.read().strip()

param = {"key": key, "token": token}

board_id = "5a250da362e909d26e2c541b"
b = requests.request("GET", "https://api.trello.com/1/boards/"+board_id, params=param)
print(b.text)
