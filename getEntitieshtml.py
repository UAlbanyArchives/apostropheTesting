from nltk.tag import StanfordNERTagger
from nltk.tokenize import TweetTokenizer, WordPunctTokenizer
import os
import json
import time

startTime = time.time()
startTimeReadable = str(time.strftime("%Y-%m-%d %H:%M:%S"))
print ("Start Time: " + startTimeReadable)

__location__ = os.path.dirname(os.path.realpath(__file__))

wordToke = WordPunctTokenizer()
stanfordPath = os.path.join(__location__, "stanford-ner-2017-06-09")
st = StanfordNERTagger(os.path.join(stanfordPath, 'classifiers/english.all.3class.distsim.crf.ser.gz'), os.path.join(stanfordPath, 'stanford-ner-3.8.0.jar'))

dataPath = os.path.join(__location__, "textData")

fileTotal = 0
for file in os.listdir(dataPath):
	fileTotal = fileTotal + 1
	
fileCount = 0
for file in os.listdir(dataPath):
	fileCount = fileCount + 1
	looptime = time.time()

	text = os.path.join(dataPath, file)
	print ("Reading file " + str(fileCount) + " of " + str(fileTotal))

	with open(text, 'r', encoding='utf-8') as dataFile:
		sourceText = dataFile.read()

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
		
		processTime = time.time() - looptime
		totalTime = time.time() - startTime

		alert1 = "Process took " + str(processTime) + " seconds or " + str(processTime/60) + " minutes or " + str(processTime/3600) + " hours"
		avgTime = totalTime/fileCount
		alert2 = "Average time is " + str(avgTime)
		remaning = fileTotal - fileCount
		alert3 = str(remaning) + " Remaining"
		estimateTime = avgTime*remaning
		alert4 = "Estimated time left: " + str(estimateTime) + " seconds or " + str(estimateTime/60) + " minutes or " + str(estimateTime/3600) + " hours"
		print(alert1)
		print(alert2)
		print(alert3)
		print(alert4)