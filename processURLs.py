import os
import csv
import json
from bs4 import BeautifulSoup

__location__ = os.path.dirname(os.path.realpath(__file__))


urlFile = os.path.join(__location__, "longURLs.csv")

count = 0
goodCount = 0
badCount = 0
domainList = []
domainData = {}

dataList = []

with open(urlFile, 'r', encoding='utf-8') as urlData:
	data = csv.reader(urlData, delimiter="|")
	
	for line in data:
		count += 1
		if count > 1:
			if len(line[2]) == 3:
				badCount += 1
				if str(line[2]) != "200":
					print (line[2])
			else:
				goodCount += 1
				root = line[2].split("//")[1].split("/")[0]
				if "." in root:
					if root.count('.') == 1:
						domain = root.lower()
					elif root.count('.') == 2:
						domain = root.split(".")[1] + "." + root.split(".")[2].lower()
					else:
						if root.lower().startswith("www."):
							domain = root.lower().split("www.")[1]
						else:
							endlist = ["com", "org", "net"]
							if root.split(".")[-1] in endlist:
								domain = root.split(".")[-2] + "." + root.rsplit(".")[-1]
							else:
								domain = root
					domainList.append(domain.strip())
					if domain in domainData.keys():
						domainData[domain] += 1
					else:
						domainData[domain] = 1
				if domain.lower == "twitter.com" or domain.lower() == "t.co":
					pass
				else:
					dataList.append(line[0])
					
with open(os.path.join(__location__, "output2", "domainList.txt"), "w", encoding='utf-8') as listFile:
	listFile.write("\n".join(domainList))
	
sortedDomains = []
sortedList = sorted(domainData, key=domainData.get)
for domainString in reversed(sortedList):
	hash = {'value': domainData[domainString], 'Domain': domainString, 'name': domainString}
	sortedDomains.append(hash)

with open(os.path.join(__location__, "output2", "domainData.json"), "w", encoding='utf-8') as outFile:
	outFile.write(json.dumps(sortedDomains))
					
				
total = goodCount + badCount
print (str(goodCount) + " of " + str(total))
print (str(goodCount / total) + " %")

for item in dataList:
	print (item)
	filepath = os.path.join(__location__, "outputData", "outputData", str(item) + ".html")
	outpath = os.path.join(__location__, "textData", str(item) + ".txt")
	with open(filepath, "r", encoding='utf-8') as file:
		data = file.read()
		soup = BeautifulSoup(data, 'html.parser')
		htmlText = soup.text
		with open(outpath, "w", encoding='utf-8') as output:
			output.write(htmlText)
