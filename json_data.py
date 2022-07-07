#!/usr/local/opt/python@3.10/bin/python3
# -*- coding: utf-8 -*-

import json
import requests
import sys

"""
- getting a existing JSON file with all HSK words as a base
from [a repo](https://raw.githubusercontent.com/gigacool/hanyu-shuiping-kaoshi/)
- adding the information about strokes and radicals from [another repo](https://raw.githubusercontent.com/pwxcoo/chinese-xinhua/)
"""


def main():
    try:
        base_response = requests.get(
            "https://raw.githubusercontent.com/gigacool/hanyu-shuiping-kaoshi/master/hsk.json"
        ).json()
    except requests.RequestException:
        sys.exit("Can not fetch base json")
    else:
        with open("base.json", "w", encoding="utf-8") as json_file:
            json.dump(
                base_response, json_file, indent=4, sort_keys=True, ensure_ascii=False
            )

    try:
        strokes_response = requests.get(
            "https://raw.githubusercontent.com/pwxcoo/chinese-xinhua/master/data/word.json"
        ).json()
    except requests.RequestException:
        sys.exit("Can not fetch json with strokes and radicals")
    else:
        with open("strokes.json", "w", encoding="utf-8") as json_file:
            json.dump(
                strokes_response,
                json_file,
                indent=4,
                sort_keys=True,
                ensure_ascii=False,
            )

    with open("./strokes.json", "r") as sf:
        strokes_data = json.load(sf)

    with open("./base.json", "r") as bf:
        base_data = json.load(bf)

    for b_obj in base_data:
        for s_obj in strokes_data:
            if b_obj["hanzi"] == s_obj["word"]:
                b_obj["strokes"] = s_obj["strokes"]
                b_obj["radicals"] = s_obj["radicals"]
        b_obj["translations"] = {"eng": b_obj["translations"]}

    with open("hsk_json.json", "w", encoding="utf-8") as json_file:
        json.dump(base_data, json_file, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    main()
