# -*- coding: utf-8 -*-
import MeCab
import os

def writeWordCountFile(path,allImagesWordCountDic):
	f = open(path,"w")
	for imgName,wordCountDic in allImagesWordCountDic.items():
		for word,count in wordCountDic.items():
			f.write(imgName + "\t" + word +"\t" + str(count) +"\n")
	f.close()

def morphologicalAnalysis(text):
	wordCount = {}

	mt = MeCab.Tagger("mecabrc")
	res = mt.parseToNode(text)

	while res:
		arr = res.feature.split(",")

		if arr[0] == "名詞" or arr[0] == "動詞":
			if res.surface in wordCount:
				wordCount[res.surface] += 1
			else:
				wordCount[res.surface] = 1
		res = res.next
	if "NONE" in wordCount:
		wordCount.pop("NONE")
	return wordCount

if __name__ == "__main__":

	fileList = os.listdir("./result/")
	for fileName in fileList:
		allImagesWordCount = {}
		for line in open("./result/" + fileName,"r"):
			element = line.split('\t')
			imgFileName = element[0]
			altStr = element[1]
			parText = element[2]
			extension = imgFileName.split(".")[-1]
			if extension == "jpg" or extension == "JPG" or extension == "jpeg" or extension == "png" or extension == "bmp":
				allImagesWordCount[imgFileName] = morphologicalAnalysis(altStr + " " + parText)
		newFileName = "./imgtf/" + fileName.split(".")[0] + ".image_and_tf"
		writeWordCountFile(newFileName,allImagesWordCount)
	print("completed")