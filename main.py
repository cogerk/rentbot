import tweepy
from time import sleep
import generate_text
from tokens import *

class TweetBot:
    def __init__(self):

        # initialize Twitter authorization with Tweepy
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)
        self.api = tweepy.API(auth)

    def tweet(self):
        message = generate_text.generate_lyrics()
        try:
            self.api.update_status(message)
        except tweepy.TweepError as error:
            print(error.reason)

    def automate(self, delay):
        while True:
            self.tweet()
            sleep(delay)


def main():
    bot = TweetBot()
    bot.automate(3600)

if __name__ == "__main__":
    main()