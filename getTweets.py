import os
import csv
import json
from twarc import Twarc

__location__ = os.path.dirname(os.path.realpath(__file__))

users = os.path.join(__location__, "apostrophe", "tweets.csv")

userList = []
with open(users, 'r', encoding='utf-8') as f:
	reader = csv.reader(f)
	rowCount = 0
	for row in reader:
		rowCount += 1
		if rowCount > 1:
			if not row[3] in userList:
				userList.append(row[3])

tweets = []
tweetContent = ""
for user in userList:				
	t = Twarc()
	for tweet in t.search("from:" + user):
		print (tweet["full_text"])
		tweetContent += "%s\n" % str(tweet["full_text"])
		tweets.append(tweet)
		
outputFile = os.path.join(__location__, "possibleBotTweets.jsonl")
with open(outputFile, "w", encoding='utf-8') as output:
	for line in tweets:
		output.write("%s\n" % str(json.dumps(line)))
		
contentOutput = os.path.join(__location__, "possibleBotTweetContent.txt")
with open(contentOutput, "w", encoding='utf-8') as output2:
	output2.write(tweetContent)