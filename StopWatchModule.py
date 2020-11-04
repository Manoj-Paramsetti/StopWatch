import keyboard
import time
import datetime
import platform
import os
i= platform.system()

def clrscr():
	if(i== "Linux" or i == "Unix" or i == 'Mac'):
		os.system('clear')
	elif(i == "Windows"):
		os.system('cls')

def AfterTime(dhrs,dmin,dsec):
    if(dhrs <=23 and dmin <= 60 and dsec <=60):
        pass
    else:
        clrscr()
        title.title()
        print("Please enter correct time")
        exit()
    clrscr()
    title.title()
    print('Press space, When You are ready')
    keyboard.wait('space')
    clrscr()
    title.title()
    hour = int(datetime.datetime.now().hour)
    minute = int(datetime.datetime.now().minute)
    second = int(datetime.datetime.now().second)
    print("Started at",hour,':',minute,":",second)
    endhr=0
    endmin=0
    endsec=0
    if(second+dsec<61):
        endsec = second+dsec

        if(minute+dmin<61):
            endmin=minute+dmin

            if((hour+dhrs+1) < 24):
                endhr=hour+dhrs

            else:
                clrscr()
                title.title()
                print("Sorry, You should end this stopwatch before this day")
                exit()
        else:
            endmin=minute+dmin-60
            if(hour+dhrs+1 < 24):
                endhr=hour+dhrs+1

            else:

                clrscr()
                title.title()
                print("Sorry, You should end this stopwatch before this day")
                exit()
    else:
        endsec=second+dsec-60
        if(minute+dmin+1 < 61):
            endmin=minute+dmin+1

            if(hour+dhrs+1 < 24):
                endhr=hour+dhrs

            else:
                clrscr()
                title.title()
                print("Sorry! You should end this stopwatch before this day")
                exit()
        else:
            endmin=minute+dmin-60+1
            if(hour+dhrs+1 < 24):
                endhr=hour+dhrs+1

            else:
                clrscr()
                title.title()
                print("Sorry! You should end this stopwatch before this day")
                exit()
    print(" End time",endhr,":",endmin,":",endsec)
    true=True
    print('\n\nPress "Ctrl + C" to stop')
    try:
        while(true):
            hour = int(datetime.datetime.now().hour)
            minute = int(datetime.datetime.now().minute)
            second = int(datetime.datetime.now().second)
            if (endhr == hour and endmin==minute and endsec==second):
                true=False
    except KeyboardInterrupt:
        ehour = int(datetime.datetime.now().hour)
        eminute = int(datetime.datetime.now().minute)
        esecond = int(datetime.datetime.now().second)
        clrscr()
        title.title()
        print("Start time",hour,':',minute,":",second)
        print("\nStopped before end time")
        print("End time",endhr,":",endmin,":",endsec)
        print("Stopped at ",ehour,':',eminute,":",esecond)
        print("\n\nCreated By Paramsetti Manoj\n\n")
        print("exiting..")
        exit()
def UserStop():
    print('Press space, When You are ready')
    keyboard.wait('space')
    try:
        clrscr()
        title.title()
        hour = int(datetime.datetime.now().hour)
        minute = int(datetime.datetime.now().minute)
        second = int(datetime.datetime.now().second)
        print("Started at",hour,':',minute,":",second)
        print('\n\nPress "Ctrl + C" to stop')

    except KeyboardInterrupt:
        ehour = int(datetime.datetime.now().hour)
        eminute = int(datetime.datetime.now().minute)
        esecond = int(datetime.datetime.now().second)

        clrscr()
        title.title()
        print("Start time",hour,':',minute,":",second)
        print("Stopped at ",ehour,':',eminute,":",esecond)

        print("\n\nCreated By Paramsetti Manoj\n\n")
        print("exiting..")
        exit()
def DesiredDayTime(date,month,year,hr,min,sec):
    true=True
    today = datetime.date.today()
    sdate= int(today.strftime("%d"))
    smonth = int(today.strftime("%m"))
    syear = int(today.strftime("%Y"))
    shour = int(datetime.datetime.now().hour)
    sminute = int(datetime.datetime.now().minute)
    ssecond = int(datetime.datetime.now().second)
    try:
        clrscr()
        title.title()
        print('\n\nPress "Ctrl + C" to stop')
        while(true):
            curdate= int(today.strftime("%d"))
            curmonth = int(today.strftime("%m"))
            curyear = int(today.strftime("%Y"))
            curhour = int(datetime.datetime.now().hour)
            curminute = int(datetime.datetime.now().minute)
            cursecond = int(datetime.datetime.now().second)
            if date == curdate:
                if month == curmonth:
                    if curyear == year:
                        if hr == curhour:
                            if min == curminute:
                                if sec == cursecond:
                                    true=False
                                    ehour = int(datetime.datetime.now().hour)
                                    eminute = int(datetime.datetime.now().minute)
                                    esecond = int(datetime.datetime.now().second)
                                    today = datetime.date.today()
                                    curdate= int(today.strftime("%d"))
                                    curmonth = int(today.strftime("%m"))
                                    curyear = int(today.strftime("%Y"))

                                    clrscr()
                                    title.title()
                                    print("Start at ",sdate,"-",smonth,"-",syear," ",shour,':',sminute,":",ssecond)
                                    print("Last time",date,"-",month,"-",year," ",hr,':',min,":",sec)
                                    print("Stopped at ",curdate,"-",curmonth,"-",curyear," ",ehour,':',eminute,":",esecond)
                                    print("Time Up")
                                    print("\nCreated By Paramsetti Manoj")


    except KeyboardInterrupt:
        ehour = int(datetime.datetime.now().hour)
        eminute = int(datetime.datetime.now().minute)
        esecond = int(datetime.datetime.now().second)
        today = datetime.date.today()
        curdate= int(today.strftime("%d"))
        curmonth = int(today.strftime("%m"))
        curyear = int(today.strftime("%Y"))

        clrscr()
        title.title()
        print("Start at ",sdate,"-",smonth,"-",syear," ",shour,':',sminute,":",ssecond)
        print("Last time",date,"-",month,"-",year," ",hr,':',min,":",sec)
        print("Stopped at ",curdate,"-",curmonth,"-",curyear," ",ehour,':',eminute,":",esecond)

def convtime(getter):
    sec,min,hour=0,0,0
    if getter < 61:
        sec=getter
        if sec==60:
            min=1
            sec=0
    else:
        sec=getter%60
        temp=getter-sec
        tempmin=temp/60
        tempmin=int(tempmin)
        if tempmin < 61:
            min+=tempmin
            if tempmin==60:
                hour=1
                min=0
        else:
            min+=tempmin%60
            temp=tempmin/60
            hour+=int(temp)
    return hour,min,sec
def convsec(hours,min,sec):
    time=hours*3600+min*60+sec
    return time
