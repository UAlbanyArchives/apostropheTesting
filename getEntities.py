from nltk.tag import StanfordNERTagger
from nltk.tokenize import TweetTokenizer, WordPunctTokenizer
import os
import json

__location__ = os.path.dirname(os.path.realpath(__file__))

wordToke = WordPunctTokenizer()
stanfordPath = os.path.join(__location__, "stanford-ner-2017-06-09")
st = StanfordNERTagger(os.path.join(stanfordPath, 'classifiers/english.all.3class.distsim.crf.ser.gz'), os.path.join(stanfordPath, 'stanford-ner-3.8.0.jar'))

dataPath = os.path.join(__location__, "possibleBotTweetContent.txt")

sourceText = ""

with open(dataPath, 'r', encoding='utf-8') as dataFile:
	data = dataFile.read()
	for line in data.split("\n"):
		tweet = json.load(line)
		sourceText += tweet["full_text"]

orgs = open(os.path.join(__location__, "outputHTML", "organizations.csv"), "a", encoding='utf-8')
peeps = open(os.path.join(__location__, "outputHTML", "people.csv"), "a", encoding='utf-8')
places = open(os.path.join(__location__, "outputHTML", "locations.csv"), "a", encoding='utf-8')
	
print ("extracting entities...")
for tagged in st.tag(wordToke.tokenize(sourceText)):
	#print (tagged)
	if tagged[1] == 'ORGANIZATION':
		orgs.write("\n" + tagged[0])

	if tagged[1] == 'PERSON':
		peeps.write("\n" + tagged[0])

	if tagged[1] == 'LOCATION':
		places.write("\n" + tagged[0])

orgs.close()
peeps.close()
places.close()
dataFile.close()