import urllib.request as Request
from urllib.error import HTTPError, URLError
import json
from collections import namedtuple

letters = [
    " ### ####  ### #### ########## ### #   # ###  #####   ##    #   ##   # ### ####  ### ####  ### ######   ##   ##   ##   ##   ######     ",
    "#   ##   ##   ##   ##    #    #    #   #  #     # #  # #    ## ####  ##   ##   ##   ##   ##      #  #   ##   ##   # # #  # #    #      ",
    "######### #    #   ############ ########  #     # ###  #    # # ## # ##   ##### # # #####  ###   #  #   ##   ## # #  #    #    #       ",
    "#   ##   ##   ##   ##    #    #   ##   #  #  #  # #  # #    #   ##  ###   ##    #  # #  #     #  #  #   # # # ## ## # #   #   #        ",
    "#   #####  ### #### ######     ### #   # ###  ##  #   #######   ##   # ### #     ## ##   #####   #   ###   #  #   ##   #  #  #####     "
]


def print_chars(chars):
    lines = ["", "", "", "", ""]
    for c in chars.lower():
        index = "abcdefghijklmnopqrstuvwxyz".find(c) * 5
        index = 130 if index < 0 else index
        for line_no, _ in enumerate(lines):
            lines[line_no] = f"{lines[line_no]}{letters[line_no][index:index+5]} "
    for line in lines:
        print(line)


def get_props_by_no(pokemon_id):
    try:
        number = int(pokemon_id)
        url = f"https://pokeapi.co/api/v2/pokemon/{number}"
    except ValueError:
        return "You didn't give a number"

    try:
        response = Request.urlopen(url)
        response_json = json.loads(response.read())
        Pokemon = namedtuple("Pokemon", ["name", "speed", "special_defence",
                                         "special_attack", "defence", "attack", "hp"])
        return Pokemon(name=response_json["name"],
                       speed=response_json["stats"][0]["base_stat"],
                       special_defence=response_json["stats"][1]["base_stat"],
                       special_attack=response_json["stats"][2]["base_stat"],
                       defence=response_json["stats"][3]["base_stat"],
                       attack=response_json["stats"][4]["base_stat"],
                       hp=response_json["stats"][5]["base_stat"])
    except HTTPError as error:
        return error.reason
    except URLError as error:
        return error.reason
