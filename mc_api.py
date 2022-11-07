import os
import requests


def get_server_status():
    response = requests.get((os.getenv('URL')))
    data = response.json()

    is_online = (data['online'])
    number_of_players = (data['players']['online'])

    return is_online, number_of_players
