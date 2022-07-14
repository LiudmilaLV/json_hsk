#!/usr/local/opt/python@3.10/bin/python3
# -*- coding: utf-8 -*-

import json

"""
Get a list of words which corresponding JSONS missing a Russian translation field.
So I can add a translations later manually.
"""

def main():
    with open("hsk.json", "r") as f:
        hsk_json = json.load(f)
        
    # List of words without Russian translations
    words = []
    for obj in hsk_json:
        if not "rus" in obj["translations"].keys():
            words.append(obj["hanzi"])
    print (words)
    print(f"{len(words)} words missing Russian translation :( ")
        
if __name__ == "__main__":
    main()