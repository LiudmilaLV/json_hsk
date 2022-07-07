Creating a JSON file containing information about all 5000 Mandarine Chinese words for all 6 HSK levels with translation to English and Russian
by:
- getting a existing JSON file with all HSK words as a base from [a repo](https://raw.githubusercontent.com/gigacool/hanyu-shuiping-kaoshi/)
- adding the information about strokes and radicals from [another repo](https://raw.githubusercontent.com/pwxcoo/chinese-xinhua/)
- and then adding a field with Russian translations (*in progress*).

## The JSON I'm aiming for:

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