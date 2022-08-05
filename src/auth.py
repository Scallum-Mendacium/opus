import json

def get_token():
    with open("config.json", 'r') as file:
        data = json.load(file)
        return data['token']