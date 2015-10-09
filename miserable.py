from random import choice
import re

from nltk.corpus import wordnet
from inflect import engine

inflect = engine()

ADJECTIVES, NOUNS = (set(), set())
BLACKLIST = [
    'miserable',
    'little',
    'secrets',
]


for wordset, kind in [
    (ADJECTIVES, wordnet.ADJ),
    (NOUNS, wordnet.NOUN),
]:
    for synset in wordnet.all_synsets(kind):
        for lemma in filter(
            lambda l: all((
                not re.search(r'\d', l.name()),
                l.name() not in BLACKLIST,
                l.count() > 0,
            )), synset.lemmas()
        ):
            wordset.add(lemma.name().replace('_', ' '))


ADJECTIVES, NOUNS = (list(ADJECTIVES), list(NOUNS))


for i in xrange(10):
    adjective = choice(ADJECTIVES)
    article = inflect.a(adjective).replace(adjective, '').strip().capitalize()

    print '{} {} little pile of {}.'.format(
        article,
        adjective,
        inflect.plural(choice(NOUNS)),
    )
