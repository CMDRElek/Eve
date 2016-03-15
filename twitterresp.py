
import tweepy, time, sys
#from our keys module (keys.py), import the keys dictionary
on = 1
from keys import keys
from function import chatbot
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']
 
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
twt = api.search(q="@ArtificialEve")     
 
#list of specific strings we want to check for in Tweets
text = ['@ArtificialEve']
text = text.replace('@ArtificialEve', "")
cmd = text
for s in twt:
    for i in text:
        if i == s.text:
            sn = s.user.screen_name
            m = ("@%s" + chatbot.get_response(cmd)) % (sn)
            
while on == 1:
    api.update_status(m, s.id)
    time.sleep(15)#Tweet every 15 minutes