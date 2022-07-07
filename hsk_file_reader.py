#!/usr/local/opt/python@3.10/bin/python3
# -*- coding: utf-8 -*-
import os


def get_rus():
    # get the text content of all txt files into one list
    content = []
    filelist = os.listdir("txts")
    for filename in filelist:
        if not filename.endswith(".txt"):
            continue
        with open("txts/" + filename, "r") as f:
            for line in f:
                content.append(line)

    # split that content into lines and every line - into a list of words
    translations_list = []
    for line in content:
        translation = line.split("\t")
        translations_list.append(translation)

    # clean the data regarding every Chinese charachter
    # create a dictionary for easyy access to hanzi name and Russian translation
    rus_dict_list = []
    for l in translations_list:
        rus_dict = {}
        l[3] = l[3].strip()
        rus_list = []
        if "; " in l[3]:
            rus_list = l[3].split("; ")
        elif "," in l[3] and ("(" not in l[3] or ")," in l[3]):
            rus_list = l[3].split(", ")
        else:
            rus_list = [l[3]]
        rus_dict.update({"hanzi": l[1], "rus": rus_list})
        rus_dict_list.append(rus_dict)

    return rus_dict_list
