import os
import time
import datetime

#this program is created by Manoj Paramsetti
#this code is maded as public and open source can be modified

os.system("color a")
os.system('cls')
#click enter to run the program
print("Read the README.md to get help")
print("   ________    ____________ __    _______   __________________     __________")
print("  / ____/ /   /  _/ ____/ //_/   / ____/ | / /_  __/ ____/ __ \   /_  __/ __ \\")
print(" / /   / /    / // /   / /<     / __/ /  |/ / / / / __/ / /_/ /    / / / / / /")
print("/ /___/ /____/ // /___/ /| |   / /___/ /|  / / / / /___/ _/_ /    / / / /_/ /")
print("\____/_____/___/\____/_/ |_|  /_____/_/ |_/ /_/ /_____/_/ |_|    /_/  \____/")
print("\n")
print("			   ______________    ____  ______")
print("			  / ___/_  __/   |  / __ \/_  __/")
print("			  \__ \ / / / /| | / /_/ / / /")
print("			 ___/ // / / ___ |/ _/_ / / /")
input("			/____//_/ /_/  |_/_/ |_| /_/")
os.system('cls')

print("""    _              __   __            ____                _
   / \   _ __ ___  \ \ / /__  _   _  |  _ \ ___  __ _  __| |_   _
  / _ \ | '__/ _ \  \ V / _ \| | | | | |_) / _ \/ _` |/ _` | | | |
 / ___ \| | |  __/   | | (_) | |_| | |  _ <  __/ (_| | (_| | |_| |
/_/   \_\_|  \___|   |_|\___/ \__,_| |_| \_\___|\__,_|\__,_|\__, |
                                                            |___/""")
time.sleep(1)
os.system("cls")
os.system("color a")
os.system("cls")
name = input("Type your full name: ")

print("welcome ",name)
age_user = input("Enter your age: ")

id_num = input("Enter your id: ")
os.system('cls')

print("Don't press \'Enter\' untill we inform")
time.sleep(3)
start=input("-->")


if start=="start" or ("START"or "Start" or not None):
	hour = int(datetime.datetime.now().hour)
	minute = int(datetime.datetime.now().minute)
	second = int(datetime.datetime.now().second)
	print("started at",hour,':',minute,":",second)


time.sleep(2)
os.system("cls")

print("    _    _ _   _______            ____            _ ")
print("   / \  | | | |_   _| |__   ___  | __ )  ___  ___| |_")
print("  / _ \ | | |   | | | '_ \ / _ \ |  _ \ / _ \/ __| __|")
print(" / ___ \| | |   | | | | | |  __/ | |_) |  __/\__ \ |_")
print("/_/   \_\_|_|   |_| |_| |_|\___| |____/ \___||___/\__")

print("Started at ",hour,":",minute,":",second)
time.sleep(5)

end= input("press \'Enter\' when you finished")
os.system("cls")

print("===========")
print("| Results |")
print("===========")
print("\nName:", name,"  Age:",age_user,"   Id: ",id_num,"\nstarted at ", hour,":",minute,':',second)

hour_1 = int(datetime.datetime.now().hour)
minute_1 = int(datetime.datetime.now().minute)
second_1 = int(datetime.datetime.now().second)

print("finished at",hour_1,":",minute_1,":",second_1)
time.sleep(1)
diff_h= hour_1 - hour
diff_m= minute_1 - minute
diff_s= second_1 - second

print("Time taken", diff_h ,":",diff_h ,":",diff_s )
os.system("rundll32.exe user32.dll, LockWorkStation")
