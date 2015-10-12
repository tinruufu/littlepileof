from subprocess import check_call
from time import sleep
from random import random

MIN_PAUSE = 2 * 60 * 60
MAX_PAUSE = 6 * 60 * 60
DELTA = MAX_PAUSE - MIN_PAUSE

# i dont want to store the entire wordnet corpus in memory at all times on my
# server, so we're just gonna spawn twooters on the (ir)reg

while True:
    sleep(MIN_PAUSE + (random() * DELTA))
    check_call(['python', 'tweet.py'])
