import os
import re
from urllib.request import urlopen
from urllib.request import Request, urlopen

__location__ = os.path.dirname(os.path.realpath(__file__))
outputPath = os.path.join(__location__, "outputData")

links = "count|short|long\n"
count = 0

dataPath = os.path.join(__location__, "possibleBotTweetContent.txt")
with open(dataPath, 'r', encoding='utf-8') as dataFile:
	data = dataFile.read()
	for tweet in data.split("\n"):
		#regex from https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
		urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)
		for url in urls:
			count += 1
			print ("extracting link " + str(count))
			q = Request(url)
			q.add_header('User-Agent', 'Mozilla/5.0')
			try:
				fp = urlopen(q)
				longLink = fp.geturl()
				links = links + str(count) + "|" + url + "|" + longLink + "\n"
			except:
				links = links + str(count) + "|" + url + "|" + str(fp.getcode()) + "\n"
			try:
				outputHTML = os.path.join(outputPath, str(count) + ".html")
				with open(outputHTML, "w", encoding='utf-8') as output:
					output.write(fp.read().decode('utf-8'))
			except:
				pass
			
			outputFile = os.path.join(__location__, "longURLs.csv")
			with open(outputFile, "w", encoding='utf-8') as output:
				output.write(links)