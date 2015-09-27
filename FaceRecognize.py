# -*- coding: utf-8 -*-
import sys
import cv2
import os
 
#顔検出器をロード
face_cascade = cv2.CascadeClassifier('./haarcascade_frontalface_alt2.xml')
 

def writeWordCountFile(path,faceCountArr):
	f = open(path,"w")
	for value in faceCountArr:
		f.write(value[0] + "\t" + str(value[1]) + "\n")
	f.close()

def facecount(path):
	print(path)
	try:
		img = cv2.imread(path)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = face_cascade.detectMultiScale(gray,scaleFactor=1.2, minNeighbors=3, minSize=(5, 5))
		print len(faces)
		return len(faces)
	except:
		print "error"
		return -1

if __name__ == "__main__":

	fileList = os.listdir("./result/")
	for fileName in fileList:
		faceCountArr = []
		for line in open("./result/" + fileName,"r"):
			element = line.split('\t')
			imgFileName = element[0]
			extension = imgFileName.split(".")[-1]
			if extension == "jpg" or extension == "JPG" or extension == "jpeg" or extension == "png" or extension == "bmp":
				c = facecount(imgFileName)
				if c != -1: faceCountArr.append((imgFileName,c))			
		newFileName = "./imgfc/" + fileName.split(".")[0] + ".image_and_face_count"
		writeWordCountFile(newFileName,faceCountArr)
	print("completed")