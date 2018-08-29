import tweepy
import os
import sys
from generate_lyrics import generate_lyrics

try:
    from tokens import *
except ModuleNotFoundError:
    print('Getting access tokens from Heroku Environment...')
    access_secret = os.environ.get('ACCESS_SECRET')
    access_token = os.environ.get('ACCESS_TOKEN')
    consumer_key = os.environ.get('CONSUMER_KEY')
    consumer_secret = os.environ.get('CONSUMER_SECRET')

class TweetBot:
    def __init__(self):

        # initialize Twitter authorization with Tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(auth)

    def tweet(self):

        message = generate_lyrics()
        try:
            self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)

    def automate(self):
        self.tweet()


def main():
    try:
        bot = TweetBot()
    except KeyboardInterrupt:
        sys.exit("KeyboardInterrupt")
    except Exception as e:
        print(e)
        pass
    bot.automate()

if __name__ == "__main__":
    main()