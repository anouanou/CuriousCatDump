# Projet :
# Objectifs :
# 1) Script qui récupère tous les messages existant d'un compte curious cat pour les dump et archiver
# 2) Amélioration : Pouvoir gérer les "conversations" de réponses et sous réponse aux questions

# URL : https://curiouscat.qa/api/v2.1/profile?username=username&max_timestamp=1602894813

import json,requests
from requests import Response

###
def get_reponse_from_user(username) -> Response:
    """
        Get Curious Cat URL Response from an username
    :param username: Curious Cat's username
    :return: Response
    """
    PARAMS = {
        'username': username,
    }
    url = "https://curiouscat.qa/api/v2.1/profile"
    return requests.get(url, params=PARAMS)

def write_json_to_file(json, filename) -> None:
    """
        Write json response to a file with a special formatting
    :param json: json object
    :param filename: Output file's name
    :return:
    """
    with open(filename, 'w') as outfile:
        json.dump(json, outfile)

def get_posts_from_json(json) -> json:
    """
        Get all posts from a json response
    :param json: Response from URL as json
    :return: Json
    """
    return


if __name__ == '__main__':
    response = get_reponse_from_user("cestpasdechance")
    print(response.json())

