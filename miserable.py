from random import choice
import re
import os

from inflect import engine
from nltk.corpus import wordnet
import requests

inflect = engine()

CACHE_PATH = os.path.join(os.path.dirname(__file__), 'word-cache')
BLACKLIST = [
    'miserable',
    'little',
    'secret',
]
SLURS = requests.get(
    'https://raw.githubusercontent.com/dariusk/wordfilter/'
    'master/lib/badwords.json'
).json()


def populate_cache():
    adjectives, nouns = (set(), set())

    for wordset, kind in [
        (adjectives, wordnet.ADJ),
        (nouns, wordnet.NOUN),
    ]:
        for synset in wordnet.all_synsets(kind):
            for lemma in filter(
                lambda l: all((
                    not re.search(r'\d', l.name()),
                    l.name() not in BLACKLIST,
                    not l.name().endswith('_to'),
                    l.count() > 0,
                )), synset.lemmas()
            ):
                wordset.add(lemma.name().replace('_', ' '))

    os.mkdir(CACHE_PATH)

    for words, filename in [
        (adjectives, 'adjectives'),
        (nouns, 'nouns'),
    ]:
        with open(os.path.join(CACHE_PATH, filename), 'w') as f:
            f.writelines((u'{}\n'.format(w) for w in words))


def is_slur(word):
    for slur in SLURS:
        if slur in word:
            return True

    return False


def get_words():
    if not os.path.isdir(CACHE_PATH):
        populate_cache()

    return [
        [l.strip()
         for l in open(os.path.join(CACHE_PATH, filename)).readlines()
         if not is_slur(l)]
        for filename in ['adjectives', 'nouns']
    ]


def generate():
    adjectives, nouns = get_words()

    adjective = choice(adjectives)
    article = inflect.a(adjective).replace(adjective, '').strip().capitalize()

    return '{} {} little pile of {}.'.format(
        article,
        adjective,
        inflect.plural(choice(nouns)),
    )


if __name__ == '__main__':
    for i in xrange(100):
        print generate()
