
import requests
import json


class Action:
    def __init__(self):
        self.date = None
        self.texte = ""

    def from_action(self, act):
        self.date = act["date"]
        self.texte = act["data"]["text"]


class Carte:
    def __init__(self):
        self.description = ""
        self.titre = ""

    def from_card(self, c):
        self.description = c["desc"]
        self.titre = c["name"]


class Necessaire:
    def __init__(self):
        self.l_actions = []
        self.l_titres = []
        self.l_dates = []
        self.l_textes = []
        self.l_descr = []


with open("key", "r") as f:
    key = f.read().strip()

with open("token", "r") as f:
    token = f.read().strip()

with open("boards", "r") as f:
    boards = [line for line in f.read().split("\n")]

for board_id in boards:
    # print(type(board_id))
    # print(repr(board_id))
    param = {"key": key, "token": token}
    b = json.loads(requests.request("GET", "https://api.trello.com/1/boards/"+board_id, params=param).text)
    # print(b)

    # print(b.text)
    # print(b.text)
    # titre = b.text["name"]
    # Pour chaque utilisateur, faire la liste des choses qu'il a faites

    # https://api.trello.com/1/boards/id/memberships
    memberships = json.loads(requests.request("GET", "https://api.trello.com/1/boards/"+board_id+"/memberships", params=param).text)
    # https://api.trello.com/1/boards/id/cards
    cards = json.loads(requests.request("GET", "https://api.trello.com/1/boards/"+board_id+"/cards", params=param).text)
    # print(cards)
    # l_titres = []
    # l_dates = []
    # l_textes = []
    # l_descr = []
    l = []
    for card in cards:
        # print("-------------------------")
        # print(card)
        c = json.loads(requests.request("GET", "https://api.trello.com/1/cards/"+card["id"], params=param).text)
        actions = json.loads(requests.request("GET", "https://api.trello.com/1/cards/"+card["id"]+"/actions", params=param).text)
        # print("Nom de la carte : ", c["name"])
        name = c["name"]
        d = {}
        d["carte"] = Carte()
        d["carte"].from_card(c)
        d["actions"] = []
        # print("Description : ", c["desc"])
        # l_descr.append(c["desc"])
        # print("action : ", actions)
        for action in actions:
            # print(action)
            # print("\ndata :", action["data"])
            if "text" in action["data"]:
                # print("action : ", action["data"]["text"])
                # print("date : ", action["date"])
                act = Action()
                act.from_action(action)
                d["actions"].append(act)

        l.append(d)
            # else:
            #     print(action)
    # response = requests.request("GET", url, params=param)

    # print(response.text)

    # print(l_titres)
    # print(l_dates)
    # print(l_textes)
    # print(l_descr)
    for d in l:
        print("-------------------------")
        print(d["carte"].titre)
        print(d["carte"].description)
        for a in d["actions"]:
            print("date :", a.date)
            print("texte :", a.texte)

