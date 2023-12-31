import json
import random
import os
import time
import base64
from pysimplebase import SimpleBase, DBSession
import requests
from ru.travelfood.simple_ui import NoSQL as noClass


BASIC_BIRDS = [
    {
        "name": "tucan",
        "feathers_color": "rainbow"
    },
    {
        "name": "parrot",
        "feathers_color": "red"
    },
    {
        "name": "eagle",
        "feathers_color": "desert"
    },
    {
        "name": "stork",
        "feathers_color": "white"
    },
    {
        "name": "cock",
        "feathers_color": "pink"
    },
    {
        "name": "jackdaw",
        "feathers_color": "black"
    },
    {
        "name": "albatross",
        "feathers_color": "white"
    },
    {
        "name": "rook",
        "feathers_color": "black"
    },
    {
        "name": "goose",
        "feathers_color": "white"
    },
    {
        "name": "lark",
        "feathers_color": "white"
    },
    {
        "name": "woodpecker",
        "feathers_color": "black"
    }
]


def customcards_on_open(hashMap, _files=None, _data=None):

    j = {"customcards":         {
        "options": {
            "search_enabled": True,
            "save_position": True
        },
        "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
                    {
                        "type": "LinearLayout",
                        "orientation": "horizontal",
                        "height": "wrap_content",
                        "width": "match_parent",
                        "weight": "0",
                        "Elements": [
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "1",
                                "Elements": [
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@string1",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    },
                                    {
                                        "type": "TextView",
                                        "show_by_condition": "",
                                        "Value": "@string2",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": "",
                                        "Variable": ""
                                    }
                                ]
                            }
                        ]
                    },
                {
                        "type": "TextView",
                        "show_by_condition": "",
                        "Value": "@descr",
                        "NoRefresh": False,
                        "document_type": "",
                        "mask": "",
                        "Variable": "",
                        "TextSize": "-1",
                        "TextColor": "#6F9393",
                        "TextBold": False,
                        "TextItalic": True,
                        "BackgroundColor": "",
                        "width": "wrap_content",
                        "height": "wrap_content",
                        "weight": 0
                    }
            ]
        }

    }
    }

    j["customcards"]["cardsdata"] = []
    ncl = noClass("birds_nosql")
    birds = json.loads(ncl.get("birds"))
    for bird in birds:

        unit = {
            "key": bird["name"],

            "descr": bird["name"],
            "val": bird["name"],
            "string1": bird["name"],
            "string2": bird["feathers_color"]
        }

        j["customcards"]["cardsdata"].append(unit)

    if not hashMap.containsKey("cards"):
        hashMap.put("cards", json.dumps(
            j, ensure_ascii=False).encode('utf8').decode())

    return hashMap


def customcards_touch(hashMap, _files=None, _data=None):
    hashMap.put("toast", "res="+str(hashMap.get("listener")+"/" +
                str(hashMap.get("layout_listener"))
                + "/"+str(hashMap.get("card_data"))))
    return hashMap


def refresh_nosql_bd(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "refresh_button":
        ncl = noClass("birds_nosql")

        url = 'http://127.0.0.1:5000/birds'

        try:
            response = requests.get(url, timeout=2)
            if response.status_code == 200:
                json_data = response.json()
            else:
                json_data = []
        except Exception as exc:
            hashMap.put("toast", f"{str(exc)} external data isn't availaible")
            return hashMap

        for bird in json_data:
            ncl.put("birds", json.dumps(bird, ensure_ascii=False), True)
        hashMap.put("toast", str(ncl.get("birds")))

    return hashMap


def birds_on_create(hashMap, _files=None, _data=None):
    if not hashMap.containsKey("bname"):
        hashMap.put("bname", "Например: parrot")
    if not hashMap.containsKey("bfeathers_color"):
        hashMap.put("bfeathers_color", "Например: orange")
    return hashMap


def input_new_bird(hashMap, _files=None, _data=None):
    ncl = noClass("birds_nosql")
    bird_data = {"name": hashMap.get("bname"),
                 "feathers_color": hashMap.get("bfeathers_color")}
    if hashMap.get("listener") == "accept_inp_bird":
        ncl.put("birds", json.dumps(bird_data,
                                    ensure_ascii=False),
                True)
        try:
            url = 'http://127.0.0.1:5000/birds'
            requests.post(url, json=bird_data, timeout=2)
        except Exception as exc:
            hashMap.put("toast", f"{str(exc)} external data isn't availaible")
            return hashMap

    hashMap.put("toast", str(ncl.get("birds")))
    return hashMap
