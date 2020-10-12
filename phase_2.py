import keys
import tweepy
import time
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import argparse


def choose_hashtag(hashtags):
    auth = tweepy.OAuthHandler(keys.consumer_key, keys.consumer_secret)
    auth.set_access_token(keys.access_token, keys.access_secret)
    api = tweepy.API(auth)

    public_tweets = api.search(q = hashtags)

    return public_tweets

def print_result(annotations):
    score = annotations.document_sentiment.score
    magnitude = annotations.document_sentiment.magnitude

    print(
        "Overall Sentiment: score of {} with magnitude of {} for this hashtag".format(score, magnitude)
    )
    return 0

def analyze(tweet): 
    """Run a sentiment analysis request on text within a passed filename."""
    client = language.LanguageServiceClient()

    document = types.Document(content=tweet, type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    # Print the results
    print_result(annotations)




if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "--twitter_hashtag",
        help="Username of desired twitter account.",
    )
    parser.add_argument(
        "--num_tweets",
        help="Define the number of tweets to analyze.",
    )

    args = parser.parse_args()

    tweets = choose_hashtag(args.twitter_hashtag)

    for i in range(int(args.num_tweets)):
        print("Tweet {}".format(i))
        print(tweets[i].text)
        analyze(tweets[i].text) 
    
    
