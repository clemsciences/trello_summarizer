
import requests
import json
with open("key", "r") as f:
    key = f.read().strip()
with open("token", "r") as f:
    token = f.read().strip()

param = {"key": key, "token": token}

board_id = "5a250da362e909d26e2c541b"
b = json.loads(requests.request("GET", "https://api.trello.com/1/boards/"+board_id, params=param).text)
print(b)
# print(b.text)
# print(b.text)
# titre = b.text["name"]
# Pour chaque utilisateur, faire la liste des choses qu'il a faites

# https://api.trello.com/1/boards/id/memberships
memberships = json.loads(requests.request("GET", "https://api.trello.com/1/boards/"+board_id+"/memberships", params=param).text)
# https://api.trello.com/1/boards/id/cards
cards = json.loads(requests.request("GET", "https://api.trello.com/1/boards/"+board_id+"/cards", params=param).text)
# print(cards)
l_titres = []
l_dates = []
l_textes = []
l_descr = []
for card in cards:
    print("-------------------------")
    # print(card)
    c = json.loads(requests.request("GET", "https://api.trello.com/1/cards/"+card["id"], params=param).text)
    actions = json.loads(requests.request("GET", "https://api.trello.com/1/cards/"+card["id"]+"/actions", params=param).text)
    # print("Nom de la carte : ", c["name"])
    l_titres.append(c["name"])
    # print("Description : ", c["desc"])
    l_descr.append(c["desc"])
    # print("action : ", actions)
    for action in actions:
        # print(action)
        # print("\ndata :", action["data"])
        if "text" in action["data"]:
            # print("action : ", action["data"]["text"])
            # print("date : ", action["date"])
            l_dates.append(action["date"])
            l_textes.append(action["data"]["text"])
        # else:
        #     print(action)
# response = requests.request("GET", url, params=param)

# print(response.text)

print(l_titres)
print(l_dates)
print(l_textes)
print(l_descr)

