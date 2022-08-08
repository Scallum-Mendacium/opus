import json


def get_token() -> str:
    with open("src/config.json") as f:
        return json.load(f)["token"]
