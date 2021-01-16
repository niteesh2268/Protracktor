import notify2 
import urllib.request
import time
import threading
from webcam import myThread2
from screen import myThread1


notify2.init("Protractor") 
n = notify2.Notification(None) 
n.set_urgency(notify2.URGENCY_NORMAL) 

def connect(host='http://google.com'):
    '''
    This method checks internet connectivity by pinging google.com

    :returns: True or False
    '''
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False
            

thread1=myThread1()
thread2=myThread2()

def stop(val1,val2):
  if val1==True:
    thread1.set()
  if val2==True:
    thread2.set()



def notify(val1,val2):
    '''
    This method issue notification to the user if Internet is down and starts the local proctoring thread .

    :param val1: bool argument
    :param val2: bool argument
    :returns: True or False 
    '''
    if connect()==False:
        n.update('Protractor','Internet down! Starting Recording')
        n.show()

        if val1==True:
            thread1.start()
        if val2==True:
            thread2.start() 
        
        return False
    return True    

def check():
    '''
    This method issues notification if Internet comes back.

    :returns: True or False
    '''
    if connect():
        n.update('Protractor','Internet Up! You can join back to MS-Teams.')
        n.show()
        return True
    return False    

class myThread5 (threading.Thread):
    def __init__(self,val1,val2,course_name):
        threading.Thread.__init__(self)
        self.flag=0
        self.exit=0
        self.val1=val1
        self.val2=val2
        self.course_name=course_name
    def setf(self):
        self.flag=1
    def sete(self):
        self.exit=1
    def run(self):
        '''
        This method controls the calling of other methods like checking of internet connectivity and calling notification functions.

        '''
        if self.val1==False and self.val2==False:
            return
        while(True):
            time.sleep(5)
            if self.flag==0:
                if notify(self.val1,self.val2)==False:
                    self.setf()

            else:
                if check()==True:
                    self.sete()
            if self.exit==1:
                break
