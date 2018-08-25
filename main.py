import tweepy
import sys
from time import sleep
from generate_lyrics import generate_lyrics
from tokens import *


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

    def automate(self, delay):
        self.tweet()


def main():
    try:
        bot = TweetBot()
    except KeyboardInterrupt:
        sys.exit("KeyboardInterrupt")
    except Exception as e:
        print(e)
        pass

if __name__ == "__main__":
    main()