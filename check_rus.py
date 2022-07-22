import json

"""
Get a list of words which corresponding JSONS missing a Russian translation field.
So I can add a translations later manually or by parsing a dictionary.
"""


def get_words():
    with open("hsk.json", "r") as f:
        hsk_json = json.load(f)

    # List of words without Russian translations
    words = []
    for obj in hsk_json:
        if not "rus" in obj["translations"].keys():
            words.append(obj["hanzi"])
    return words
