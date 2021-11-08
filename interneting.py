import requests

IP = "192.168.1.195"
PORT = "8085"
URL = "http://" + IP + ":" + PORT + "/cards/verify/"

def verify_card(uuid, password):
    DATA = { "uuid": uuid, "password": password }
    res = requests.post(
        url = URL,
        data = str(DATA),
        headers = {'Content-Type': 'application/json'}
    )
    return res.json()

def verify_uuid(uuid):
    DATA = { "uuid": uuid }
    res = requests.post(
        url = URL,
        data = str(DATA),
        headers = {'Content-Type': 'application/json'}
    )
    return res.json()
    