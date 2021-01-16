import cv2 
import threading
import time
from datetime import datetime
from read_config import read_config

class myThread2 (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.flag=0
		
	def set(self):
		self.flag=1
	def run(self):
		'''
		This method captures video from Webcam using OpenCV and writes each frame of the video in an output file.
		The file is then saved in WebcamRecordings folder and named by current date and time in .avi format.

		:returns: Webcam Recording file
		'''
		video = cv2.VideoCapture(0) 
		frame_width = int(video.get(3)) 
		frame_height = int(video.get(4)) 
		size = (frame_width, frame_height)
		filename="../results/WebcamRecordings/"+read_config()+"_"+datetime.now().strftime('%d-%m-%Y_%H:%M:%S')+".avi" 
		result = cv2.VideoWriter(filename,cv2.VideoWriter_fourcc(*'XVID'), 24, size) 
			
		while(True):
			ret, frame = video.read()
			result.write(frame)

			if self.flag==1:
				break
		video.release() 
		result.release() 
 
