import tweepy
import json

# json読み込み
with open("../twitter_config.json") as twi_config:
    conf = json.load(twi_config)

a_key = conf["API_key"]
as_key = conf["API_secret_key"]
a_token = conf["Access_token"]
as_token = conf["Access_token_secret"]

# Twitter object
auth = tweepy.OAuthHandler(a_key, as_key)
auth.set_access_token(a_token, as_token)
twi_api = tweepy.API(auth)

# Tweet
twi = """
\n
お昼です。
\n
今日のお昼ご飯は何でしょうか？
ψ(｀∇´)ψ
"""
twi_api.update_status(twi)
