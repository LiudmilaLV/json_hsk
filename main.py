#!/usr/local/opt/python@3.10/bin/python3
# -*- coding: utf-8 -*-

import json
from hsk_file_reader import get_rus


def main():
    with open("hsk_json.json", "r", encoding="utf-8") as json_f:
        hsk_json = json.load(json_f)

    # get list with all HSK hanzi names
    hanzi_list = []
    for obj in hsk_json:
        hanzi_list.append(obj["hanzi"])

    # add Russian translation to every json object
    rus = get_rus()
    for obj in hsk_json:
        for el in rus:
            if obj["hanzi"] == el["hanzi"]:
                obj["translations"]["rus"] = el["rus"]

    # save the JSON into a file
    with open("rus_hsk_json.json", "w", encoding="utf-8") as json_file:
        json.dump(hsk_json, json_file, indent=4, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    main()
