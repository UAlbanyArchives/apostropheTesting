# -*- coding: utf-8 -*-
import json
import os

def pp(stuff):
	print (json.dumps(stuff, indent=2))

__location__ = os.path.dirname(os.path.realpath(__file__))

#inputFile = os.path.join(__location__, "bumpStockUpstate.jsonl")
#inputFile = os.path.join(__location__, "bumpStockNYC.jsonl")
inputFile = os.path.join(__location__, "possibleBotTweets.jsonl")
print (inputFile)

count = 0
with open(inputFile, 'r', encoding='utf-8') as dataFile:
	data = dataFile.read()
	for line in data.split("\n"):
		count += 1
		#print (line)
		if len(line) > 0:
			tweet = json.loads(line)
		
			if count == 6355:
				print (line)
				pp(tweet)

			
print (count)
		