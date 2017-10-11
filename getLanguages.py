# -*- coding: utf-8 -*-
import json
import os
import operator

def pp(stuff):
	print (json.dumps(stuff, indent=2))

__location__ = os.path.dirname(os.path.realpath(__file__))

#inputFile = os.path.join(__location__, "bumpStockUpstate.jsonl")
#inputFile = os.path.join(__location__, "bumpStockNYC.jsonl")
inputFile = os.path.join(__location__, "possibleBotTweets.jsonl")
print (inputFile)

langLookup = {'fr': 'French', 'en': 'English', 'ar': 'Arabic', 'ja': 'Japanese', 'es': 'Spanish', 'de': 'German', 'it': 'Italian', 'id': 'Indonesian', 'pt': 'Portuguese', 'ko': 'Korean', 'tr': 'Turkish', 'ru': 'Russian', 'nl': 'Dutch', 'fil': 'Filipino', 'msa': 'Malay', 'zh-tw': 'Traditional Chinese', 'zh-cn': 'Simplified Chinese', 'hi': 'Hindi', 'no': 'Norwegian', 'sv': 'Swedish', 'fi': 'Finnish', 'da': 'Danish', 'pl': 'Polish', 'hu': 'Hungarian', 'fa': 'Farsi', 'he': 'Hebrew', 'ur': 'Urdu', 'th': 'Thai', 'en-gb': 'English UK'}

count = 0
languages = {}
with open(inputFile, 'r', encoding='utf-8') as dataFile:
	data = dataFile.read()
	for line in data.split("\n"):
		count += 1
		#print (line)
		if len(line) > 0:
			tweet = json.loads(line)
			
			if tweet["lang"] in languages.keys():
				languages[tweet["lang"]] += 1
			else:
				languages[tweet["lang"]] = 1
				
			
		
		
			if count == 6455:
				print (tweet["lang"])
				#print (line)
				#pp(tweet)
				#for url in tweet["entities"]["urls"]:
					#print (url["expanded_url"])
sortedLang = []
reverseLang = sorted(languages, key=languages.get)
for lang in reversed(reverseLang):
	if lang in langLookup.keys():
		sortedLang.append({'value': languages[lang], "Language": langLookup[lang], "name": langLookup[lang]})
	else:
		sortedLang.append({'value': languages[lang], "Language": lang, "name": lang})

			
print (json.dumps(sortedLang))