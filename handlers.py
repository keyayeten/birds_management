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
                                "type": "CheckBox",
                                "Value": "@cb1",
                                "NoRefresh": False,
                                "document_type": "",
                                "mask": "",
                                "Variable": "cb1",
                                "BackgroundColor": "#DB7093",
                                "width": "match_parent",
                                "height": "wrap_content",
                                "weight": 2
                            },
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
                                    },
                                    {
                                        "type": "Button",
                                        "show_by_condition": "",
                                        "Value": "#f290",
                                        "TextColor": "#DB7093",
                                        "Variable": "btn_tst1",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": ""

                                    },
                                    {
                                        "type": "Button",
                                        "show_by_condition": "",
                                        "Value": "#f469",
                                        "TextColor": "#DB7093",
                                        "Variable": "btn_tst2",
                                        "NoRefresh": False,
                                        "document_type": "",
                                        "mask": ""

                                    }
                                ]
                            },
                            {
                                "type": "PopupMenuButton",
                                "show_by_condition": "",
                                "Value": "Удалить;Проверить",
                                "NoRefresh": False,
                                "document_type": "",
                                "mask": "",
                                "Variable": "menu_delete"

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
    for bird in BASIC_BIRDS:

        c = {
            "key": bird["name"],

            "descr": bird["name"],
            "val": bird["name"],
            "string1": bird["name"],
            "string2": bird["feathers_color"]
        }

        j["customcards"]["cardsdata"].append(c)

    if not hashMap.containsKey("cards"):
        hashMap.put("cards", json.dumps(
            j, ensure_ascii=False).encode('utf8').decode())

    return hashMap


def customcards_touch(hashMap, _files=None, _data=None):
    hashMap.put("toast", "res="+str(hashMap.get("listener")+"/" +
                str(hashMap.get("layout_listener"))+"/"+str(hashMap.get("card_data"))))
    return hashMap


def refresh_nosql_bd(hashMap, _files=None, _data=None):
    if hashMap.get("listener") == "refresh_button":
        ncl = noClass("birds_nosql")

        # url = 'http://127.0.0.1:5000/birds'

        # response = requests.get(url)

        # if response.status_code == 200:
        #     json_data = response.json()
        # else:
        #     json_data = []

        for bird in BASIC_BIRDS:
            ncl.put("birds", json.dumps(bird, ensure_ascii=False), True)
        hashMap.put("toast", str(ncl.get("birds")))

    return hashMap
