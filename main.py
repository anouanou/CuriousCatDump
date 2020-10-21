# Projet :
# Objectifs :
# 1) Script qui récupère tous les messages existant d'un compte curious cat pour les dump et archiver
# 2) Amélioration : Pouvoir gérer les "conversations" de réponses et sous réponse aux questions

# URL : https://curiouscat.qa/api/v2.1/profile?username=username&max_timestamp=1602894813

import json, requests
from requests import Response


def get_reponse_from_user(username, timestamp=None) -> Response:
    """
        Get Curious Cat URL Response from an username
    :param username: Curious Cat's username
    :param timestamp: Message before this timestamp
    :return: Response
    """
    PARAMS = {
        'username': username,
        'timestamp': timestamp
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

# Il faudra faire en sorte de prendre en compte dans la 2ème version les sous-réponses qui sont stockés dans le set "in_response_to"
def get_posts_from_json(json) -> json:
    """
        Get all posts from a json response
    :param json: Response from URL as json
    :return: Json
    """
    new = {}
    start = 0
    for x in json["posts"]:
        new[start] = {
            "id": x["post"]["id"],
            "timestamp": x["post"]["timestamp"],
            "seconds_elapsed": x["post"]["seconds_elapsed"],
            "question": x["post"]["comment"],
            "reply": x["post"]["reply"]
        }
        start += 1
    return new



if __name__ == '__main__':
    response = get_reponse_from_user("iampostbad")
    print("Posts : ")
    print(get_posts_from_json(response.json()))
