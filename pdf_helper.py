#!/usr/local/opt/python@3.10/bin/python3
# -*- coding: utf-8 -*-


def get_rus():

    translations_list = []

    with open("hsk_rus.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line[0].isdigit():
                translation = line.split("   ")
                clean_translation = [
                    x.strip() for x in translation if x and not x.isspace()
                ]
                split_first = clean_translation[0].split()
                if len(split_first) == 2:
                    clean_translation.insert(0, split_first[0])
                    clean_translation.insert(1, split_first[1])
                    clean_translation.pop(2)
                if len(clean_translation) > 4:
                    clean_translation = clean_translation[:4]
                translations_list.append(clean_translation)

    rus_dict_list = []
    for l in translations_list:
        rus_dict = {}
        if len(l) == 4:
            rus_dict.update({"hanzi": l[1], "rus": l[3].split("; ")})
        else:
            rus_dict.update({"hanzi": l[1], "rus": "-"})
        rus_dict_list.append(rus_dict)
    return rus_dict_list
