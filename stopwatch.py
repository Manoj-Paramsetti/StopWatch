import os
import time
import keyboard
import datetime
import platform
import StwFun.title
import StwFun.StopWatchModule
i= platform.system()
def clrscr():
	if(i== "Linux" or i == "Unix" or i == 'Mac'):
		os.system('clear')
	elif(i == "Windows"):
		os.system('cls')
	else:
		print("Sorry you're not supported to use this software")
		exit()

def exitscreen():
	StwFun.title.title()
	print("                     XX-XX<-  Exit  ->XX-XX")
vrai=True
try:
	while(vrai):
		clrscr()
		StwFun.title.title()
		print("press 1 to have stop in a peroid of time (Till 24:00:00)")
		print("press 2 to have user stop control  (Till 24:00:00)")
		print("press 3 to stop in desired day and time")
		print("press 4 to convert second into time format")
		print("press 5 to convert time to seconds")
		print("type exit to quit")
		print("Note: There is no pause option")
		capkey = input("\n==>")

		if capkey == '1':
			clrscr()
			StwFun.title.title()
			print("Stop after")
			print("==========")
			dhrs = int(input("Hours: "))
			dmin = int(input("minute: "))
			dsec = int(input("second: "))
			clrscr()
			StwFun.StopWatchModule.AfterTime(dhrs,dmin,dsec)
			time.sleep(0.2)
		if capkey == '2':
			clrscr()
			StwFun.title.title()
			StwFun.StopWatchModule.UserStop()
			time.sleep(0.2)
		if capkey == '3':
			clrscr()
			StwFun.title.title()
			print("End Time")
			print("========")
			ddate = int(input("Date: "))
			dmonth = int(input("Month: "))
			dyear = int(input("Year: "))
			dhrs = int(input("Hours: "))
			dmin = int(input("minute: "))
			dsec = int(input("second: "))
			StwFun.StopWatchModule.DesiredDayTime(ddate,dmonth,dyear,dhrs,dmin,dsec)
			time.sleep(0.2)
		if capkey=='4':
			clrscr()
			StwFun.title.title()
			inp=int(input("Enter seconds to convert into time format\n==>"))
			hr,min,sec = StwFun.StopWatchModule.convtime(inp)
			print("output\n=>",hr,min,sec)
		if capkey=='5':
			clrscr()
			StwFun.title.title()
			dhrs = int(input("Hours: "))
			dmin = int(input("minute: "))
			dsec = int(input("second: "))
			sec = StwFun.StopWatchModule.convsec(dhrs,dmin,dsec)
			print("output\n=>",second)
		if capkey == "exit":
			vrai=False
			clrscr()
			exitscreen()
			exit()
except KeyboardInterrupt:
	clrscr()
	exitscreen()
