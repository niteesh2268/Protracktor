import subprocess
import csv
import time
import os
from operator import itemgetter
from pathlib import Path
import threading
from read_config import read_config
import pandas as pd 
from matplotlib import pyplot as plt 

period = 1 
order = "up"
maindir = "../results/ActivityTracker"
try:
    os.mkdir(maindir)
except FileExistsError:
    pass
logdir = "../results/ActivityTracker/text"
csvdir = "../results/ActivityTracker/csv"
pltdir = "../results/ActivityTracker/usage_graph"

def currtime(tformat=None):
    '''
    This method checks for the file and returns the time in respective format.
    :param tformat: string argument
    :returns: date and time 
    '''
    return time.strftime("%Y_%m_%d_%H_%M_%S") if tformat == "file"\
           else time.strftime("%Y-%m-%d %H:%M:%S")
try:
    os.mkdir("../results/ActivityTracker/text")
except FileExistsError:
    pass
try:
    os.mkdir("../results/ActivityTracker/csv")
except FileExistsError:
    pass
try:
    os.mkdir("../results/ActivityTracker/usage_graph")
except FileExistsError:
    pass

filename = currtime("file")
log1 = logdir+"/"+read_config()+currtime("file")+".txt"; startt = currtime()
log2 = csvdir+"/"+read_config()+currtime("file")+".csv"; startt = currtime()

def get(command):
    '''
    This method gets the output of the command and converts it into utf-8 format
    :param command: list argument
    :returns: output of command in utf-8 format
    '''
    try:
        return subprocess.check_output(command).decode("utf-8").strip()
    except subprocess.CalledProcessError:
        pass

def time_format(s):
    '''
    This method coverts cumulative time in seconds into HH:MM:SS
    :param s: total seconds time
    :returns: time in HH:MM:SS format
    '''
    m, s = divmod(s, 60); h, m = divmod(m, 60)
    return "%d:%02d:%02d" % (h, m, s)

def summarize(t,winlist,applist):
    '''
    This is heart of the program it lists the applications and corresponding duration of usage for each application
    '''
    with open(log1, "wt" ) as report:
        totaltime = sum([it[2] for it in winlist]) 
        report.write("")
        alldata = []      
        for app in applist:
            appdata = []; windata = []; appinfo = []
            apptime = sum([it[2] for it in winlist if it[0] == app])
            appperc = round(100*apptime/totaltime)            
            for d in [app, apptime, appperc]:
                appdata.append(d)
            
            wins = [r for r in winlist if r[0] == app]            
            for w in wins:
                wperc = str(round(100*w[2]/apptime))
                windata.append([w[1], w[2], wperc])                
            windata = sorted(windata, key=itemgetter(1))
            windata = windata[::-1] if order == "up" else windata
            appdata.append(windata); alldata.append(appdata)            
        alldata = sorted(alldata, key = itemgetter(1))
        alldata = alldata[::-1] if order == "up" else alldata  
        
              
        for item in alldata:
            app = item[0]; apptime = item[1]; appperc = item[2]
            report.write(("-"*60)+"\n"+app+"\n"+time_format(apptime)+" ("+str(appperc)+"%)\n"+("-"*60)+"\n")
            field_names = ['Application', 'Time', 'Percentage']
            dict = {'Application': app, 'Time': time_format(apptime), 'Percentage': appperc}
            appinfo.append(dict)
            with open(log2, "w") as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames = field_names) 
                writer.writeheader() 
                writer.writerows(appinfo)  
            for w in item[3]:
                wname = w[0]; time = w[1]; perc = w[2]
                report.write("   "+time_format(time)+" ("+perc+"%)"+(6-len(perc))*" "+wname+"\n")
        report.write("\n"+"="*60+"\nstarted: "+startt+"\t"+"updated: "+currtime()+"\n"+"="*60)

def plot():
    '''
	This method is used for plotting the bar graph from the final csv file 
	generated by summarize() method
	'''
    try:
        data = pd.read_csv(log2)
    except FileNotFoundError:
        return     
    df = pd.DataFrame(data) 
    name = df['Application']
    perc = df['Percentage']
    fig, ax = plt.subplots(figsize =(13, 7))  
    ax.barh(name, perc) 
    for s in ['top', 'bottom', 'left', 'right']: 
        ax.spines[s].set_visible(False) 
    ax.xaxis.set_ticks_position('none') 
    ax.yaxis.set_ticks_position('none') 
    ax.xaxis.set_tick_params(pad = 5) 
    ax.yaxis.set_tick_params(pad = 10) 
    ax.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2) 
    ax.invert_yaxis() 
    for i in ax.patches: 
        plt.text(i.get_width()+0.2, i.get_y()+0.5, str(round((i.get_width()), 2)), fontsize = 10, fontweight ='bold', color ='grey')  
    ax.set_title('Activity Tracker Result', loc ='center') 
    plt.xlabel('Percentage of time used', fontweight ='bold') 
    fig.text(0.9, 0.15, 'Protracktor', fontsize = 12, color ='grey', ha ='right', va ='bottom', alpha = 0.7) 
    fig.savefig(pltdir+'/'+filename+'.png')
        
class myThread4 (threading.Thread):
    '''
	It is a threading class which is controlled by our main application file
	'''
    def __init__(self):
        '''
    	Initiates the window activity tracking process
    	'''
        threading.Thread.__init__(self)
        self.flag=0
        self.t = 0 
        self.applist = []
        self.winlist = []

    def set(self):
        '''
    	This method triggers to close the thread
    	'''
        self.flag=1
    def run(self):
        '''
    	This method initiates and continuosly runs the activity tracking with the help of other methods
    	'''
        while True:
            time.sleep(period)
            if self.flag==1:
                plot()
                break
            frpid = get(["xdotool", "getactivewindow", "getwindowpid"])
            frname = get(["xdotool", "getactivewindow", "getwindowname"])
            app = get(["ps", "-p", frpid, "-o", "comm="]) if frpid != None else "Unknown"
            
            if "gnome-terminal" in app:
                app = "gnome-terminal"
            elif app == "soffice.bin":
                app = "libreoffice"
            
            if not app in self.applist:
                self.applist.append(app)
            checklist = [item[1] for item in self.winlist]
            if not frname in checklist:
                self.winlist.append([app, frname, 1*period])
            else:
                self.winlist[checklist.index(frname)][2] = self.winlist[checklist.index(frname)][2]+1*period
            if self.t == 60/period:
                summarize(self.t,self.winlist,self.applist)
                self.t = 0
            else:
                self.t += 1
