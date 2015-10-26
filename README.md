# miserable

[@chillallmen][cam] tweeted [this gem][gem] so i made [@littlepileof][lpo]

[cam]: https://twitter.com/ChillAllMen
[gem]: https://twitter.com/ChillAllMen/status/652244976680726528
[lpo]: https://twitter.com/littlepileof

## install

get a unix-looking system with python 2, then clone and `cd` to this repo, then
run:

```
pip2 install -r requirements.txt
python2 -c 'import nltk; nltk.download("wordnet")'
```

## use

if you just want to generate dumb fake sotn quotes at your command line, all
you need to do at this point is run `python2 miserable.py`:

```
$ python2 miserable.py
A prolonged little pile of separations.
An interdependent little pile of fences.
A razor-sharp little pile of lilts.
A kindly little pile of supermarkets.
A radial little pile of solipsisms.
A scorched little pile of registrations.
An adverse little pile of sheets.
An atrophied little pile of tentacles.
A precarious little pile of indignations.
A pert little pile of diabetics.
```

note that this command might take a minute or two to run; there are a lot of
words to try

----

if you want to tweet, you will need to [make a twitter app][app]. if you make
the app using the account that will be tweeting, twitter will give you all the
keys you need. if you don't, though, you'll need to follow [tweepy's
instructions][auth] to get the 'consumer token' or whatever they call it.
however you get them, make a file called `secrets.py` alongside the rest of the
stuff in the folder you're in and make it look like this (but with real keys):

```python
app_key = 'AAAAAAAAAAAAAAAAAAAAAAAAA'
app_secret = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
token_key = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
token_secret = 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'
```

[app]: https://apps.twitter.com/app/new
[auth]: http://docs.tweepy.org/en/latest/auth_tutorial.html

to tweet, you should now be able to run `python2 tweet.py` (but remember it will
take a few minutes). i run `daemon.py` as a service on my server to keep the
posts a-coming, but you can do whatever you like, i'm not the boss of you
