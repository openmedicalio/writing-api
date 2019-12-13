import pprint

import requests


def print(x):
    pprint.pprint(x)


langinputs = {

    'en': [
        "myy nam is peter. i no good at speelling in english. i'm going to say that i think writing take a lot of skill "],
    'es': ['me no puede hablas inglais'],
    'fr': ['je aimes pas etude maths'],
    'zh': ['我是国外人民。我中国文很坏。'],

}
url = 'https://us-central1-project-318531836785902414.cloudfunctions.net/writing'

s = requests.Session()
for lang in langinputs:
    for input in langinputs[lang]:
        payload = {
            'method': 'correct',
            'text': input,
            'lang': lang,
        }
        r = s.post(url, json=payload).json()
        print(r)

prompts = ['I fucked',
           "you're",
           ]
s = requests.Session()
for prompt in prompts:
    payload = {
        'method': 'generate',
        'text': prompt,
        'length': 8,
        'num_samples': 100,
        'lang': 'en',

    }
    r = s.post(url, json=payload).json()
    print(r)
