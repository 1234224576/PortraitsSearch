# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os

def readHtmlFile(path):
	data = open(path).read()
	soup = BeautifulSoup(data)
	results = []
	for imgElement in soup.find_all("img"):
		src = imgElement.get("src")

		if(src == None or src.find("test_data") != 0):
			continue
		else:
			src = "./data/" + src

		alt = imgElement.get("alt") if imgElement.get("alt") != None or imgElement.get("alt") == "" else "NONE"
		alt = alt.replace("\n",'')
		alt = alt.replace("\r",'')

		parText = ""

		for string in imgElement.parent.stripped_strings:
			parText += string
		if parText == "": parText = "NONE"
		parText = parText.replace('\n','')
		parText = parText.replace('\r','')
		
		results.append((src,alt,parText))
	return results

if __name__ == "__main__":

	fileList = os.listdir("./data/")
	for fullFileName in fileList:
		filename = fullFileName.split(".")
		if(len(filename) > 1 and filename[1] == "html"):
			results = readHtmlFile("./data/"+filename[0] +".html")
			f = open("./result/" + filename[0] + ".image_and_text","w")
			for result in results:
				f.write(result[0] + "\t" + result[1].encode('utf-8') + "\t" + result[2].encode('utf-8') + "\n")