import requests
import json


def jokes(f):
    data = requests.get(f)
    tt = json.loads(data.text)
    return tt


f = r"https://official-joke-api.appspot.com/jokes/general/random"
a = jokes(f)



