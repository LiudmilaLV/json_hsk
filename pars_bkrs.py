from bs4 import BeautifulSoup
from check_rus import get_words
import re
import requests

"""
Parsing bkrs.info (a web-site for searching through the Big Chinese-Russian Dictionary),
getting Russian translations.
"""


def main():
    words = get_words()
    rus_translations_list = []
    for word in words:
        html_text = requests.get(f"https://bkrs.info/slovo.php?ch={word}").text
        soup = BeautifulSoup(html_text, features="html.parser")
        try:
            rus = soup.find(class_="ru").div.text
            if rus and rus[0].isupper():
                rus = soup.find(class_="m2").text
        except:
            try:
                rus = soup.find(class_="m2").text
                if rus and rus[0].isupper():
                    rus = soup.find(class_="ru").text
            except:
                try:
                    rus = soup.find(class_="ru").text
                except:
                    rus = "Please, add translation manually"
        if rus[0].isnumeric():
            rus = rus[2:]
        rus = list(rus)
        for char in rus:
            if char.isalpha() and not re.search("[\u0400-\u04FF]", char):
                rus.remove(char)
        rus_translation = "".join(rus)
        if re.search("[\u0400-\u04FF]", rus_translation):
            rus_translations_list.append(rus_translation)
    print(
        f"{len(rus_translations_list)} words still need a Russian transation to be added manually"
    )
    """207 words still need a Russian transation to be added manually"""


if __name__ == "__main__":
    main()
