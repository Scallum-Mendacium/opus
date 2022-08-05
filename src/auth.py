import json


def get_token() -> str:
    with open("config.json", "r") as file:
        data = json.load(file)
        return data["token"]
