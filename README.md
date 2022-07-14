# JSON for HSK word list
JSON file containing information about all 5000 words for all 6 HSK levels (for Mandarine Chinese proficiency exam) with translation to English and Russian created by:
- getting a existing JSON file with all HSK words as a base from [a repo](https://github.com/gigacool/hanyu-shuiping-kaoshi/)
- adding the information about strokes and radicals from [another repo](https://github.com/pwxcoo/chinese-xinhua/)
- and then adding a field with Russian translations I got from an awesome [project](https://chineseplus.club/) for Russian-speaking Chinese learners.

Please, feel free to suggest corrections.


*Список всех слов для всех уровней HSK (экзамен на знание китайского языка) в формате JSON с переводом на русский и английский языки.*

*Правки и предложения приветствуются :)*

## JSON example:
```
[
    {
        "hanzi": "爱",
        "id": 1,
        "level": 1,
        "pinyin": "ài",
        "radicals": "爫",
        "strokes": "10",
        "translations": {
            "eng": [
                "to love",
                "affection",
                "to be fond of",
                "to like"
            ],
            "rus": [
                "любить",
                "любовь"
            ]
        }
    },
    {
        "hanzi": "吧",
        "id": 151,
        "level": 2,
        "pinyin": "ba",
        "radicals": "口",
        "strokes": "7",
        "translations": {
            "eng": [
                "(modal particle indicating suggestion or surmise)",
                "...right?",
                "...OK?",
                "...I presume."
            ],
            "rus": [
                "(частица, выражает предложение ч-л сделать, догадку и пр.)"
            ]
        }
    }
]
```