import pyautogui 
import cv2 
import numpy as np 
import time
import threading
from datetime import datetime
from read_config import read_config

class myThread1 (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.flag=0
		
		
	def set(self):
		self.flag=1
	def run(self):
		'''
	    This method generates the Screen Recording file.
	    It specifies the device screen resolution and takes screenshot using PyAutoGUI.
	    The screenshot is converted to a numpy array.
	    PyAutoGUI captures the screen in RGB(Red, Green, Blue) form and OpenCV converts it to BGR(Blue, Green, Red) and then writes that in an output file.
	    The file is saved in ScreenRecordings folder and named by current date and time in .avi format.
	    
	    :returns: Screen Recording file
	    
	    '''
		resolution = pyautogui.size()
		  

		codec = cv2.VideoWriter_fourcc(*"XVID") 
		filename = "../results/ScreenRecordings/"+read_config()+"_"+datetime.now().strftime('%d-%m-%Y_%H:%M:%S')+".avi"
  
		fps =24.0
		out = cv2.VideoWriter(filename, codec, fps, resolution) 
		  
		while True: 
		    img = pyautogui.screenshot() 
		    frame = np.array(img) 
		    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
		    out.write(frame)
		    if self.flag==1:
		      break
		cv2.destroyAllWindows()
 

