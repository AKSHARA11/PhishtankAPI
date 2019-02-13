import json
import configparser
import pyphishtank
from pyphishtank import PhishTank
#import urllib.parse as ub
#from urllib.parse import resolve
from urlunshort import resolve

new_tweets = []                 
for line in open('data.json'):           # reading the lines in given json file
    new_tweets.append(json.loads(line))     # appending the dictionaries in json file to a the list tweets
    
# print(new_tweets)
urls = []
for tweet in new_tweets:
	if 'expanded_url' in tweet:
		urls.append(tweet['expanded_url'])
	else:
		pass

api = PhishTank()

for url in urls:
	unshortenUrl = resolve(url)
	print(api.check(str(unshortenUrl)))
