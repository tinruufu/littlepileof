from random import choice

from nltk.corpus import wordnet
from pattern.en import pluralize, referenced

RAREST = 1500
COMMONEST = 500

ADJECTIVES, NOUNS = [
    sorted([
        lemma for synset in wordnet.all_synsets(kind)
        for lemma in synset.lemmas()
    ], key=lambda lemma: lemma.count())[-RAREST:-COMMONEST]
    for kind in wordnet.ADJ, wordnet.NOUN
]


for i in xrange(10):
    print 'what is a man? {} little pile of {}'.format(
        referenced(choice(ADJECTIVES).name()),
        pluralize(choice(NOUNS).name()),
    )
