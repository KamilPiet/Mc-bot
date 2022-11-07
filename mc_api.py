import os
import requests


def get_server_status():
    response = requests.get(str(os.getenv('URL')))
    data = response.json()

    is_online = (data['online'])
    if is_online:
        number_of_players = (data['players']['online'])
    else:
        number_of_players = 0

    return is_online, number_of_players

