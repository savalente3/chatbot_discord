#from time import gmtime, strftime 
#import time
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta


"""calculates de time you should wake up given a bed time hour"""
#good night sleep is between 5/6 cycles
#takes 15 min for someone to fall asleep 

def sleepW():
   
 #https://docs.python.org/3/library/time.html
 ##t = strftime("%H:%M", gmtime())
 t1 = datetime.now()
 t2 = t1.strftime("%H:%M")

 hours, minutes = t2.split(":") 

 H = int (hours) 
 M = int (minutes)
 cycle = 90  

 #it takes an average of 15 min to fall asleep

 minTimeC3 = ( 15 + ((H * 60) + M) + (3 * cycle)) #4.5h of sleep
 minTimeC4 = ( 15 + ((H * 60) + M) + (4 * cycle)) #6h of sleep
 minTimeC5 = ( 15 + ((H * 60) + M) + (5 * cycle)) #7.5h of sleep
 minTimeC6 = ( 15 + ((H * 60) + M) + (6 * cycle)) #9h of sleep


 #https://stackoverflow.com/questions/775049/how-do-i-convert-seconds-to-hours-minutes-and-seconds
 #conert seconds to hours and minutes

 W3C = str(timedelta(minutes=minTimeC3))
 W4C = str(timedelta(minutes=minTimeC4))
 W5C = str(timedelta(minutes=minTimeC5))
 W6C = str(timedelta(minutes=minTimeC6))


 W3C1 = W3C[:-3] 
 W4C1 = W4C[:-3] 
 W5C1 = W5C[:-3] 
 W6C1 = W6C[:-3] 


 print("If you going to bed at",t2,"you should wake up at one of these times: ")
 print("4h and 30 min of sleep:", W3C1)
 print("6h of sleep:", W4C1)
 print("7h and 30 min of sleep:", W5C1)
 print("9h of sleep:", W6C1)

 
 print("How many hours are you to sleep?")
 sleepW.sleep = input()
 
 return  W3C1, W4C1, W5C1, W6C1

#sleep = sleepW.sleep
sleepW()


"""Calculates the time you should go to sleep to wake up at a certain time"""

print("when do you want to get up? ")
t = input()

def sleepB():
   
 hours, minutes = t.split(":") 
 H = int (hours)
 M = int (minutes)
 cycle = 90  


 minTimeC3 = ( 15 + ((H * 60) + M) - (3 * cycle)) #4.5h of sleep
 minTimeC4 = ( 15 + ((H * 60) + M) - (4 * cycle)) #6h of sleep
 minTimeC5 = ( 15 + ((H * 60) + M) - (5 * cycle)) #7.5h of sleep
 minTimeC6 = ( 15 + ((H * 60) + M) - (6 * cycle)) #9h of sleep

 W3C = timedelta(minutes=minTimeC3)
 W4C = str(timedelta(minutes=minTimeC4))
 W5C = str(timedelta(minutes=minTimeC5))
 W6C = str(timedelta(minutes=minTimeC6))


 #W3C1 = W3C[:-3] 
 #W4C1 = W4C[:-3] 
 #W5C1 = W5C[:-3] 
 #W6C1 = W6C[:-3] 

 print(W3C.hour, W3C.minute)


 #print("If you wanto to wake up at ",t," you should go to bed at one of these times: ")
 #print("4h and 30 min of sleep:", W3C1)
 #print("6h of sleep:", W4C1)
 #print("7h and 30 min of sleep:", W5C1)
 #print("9h of sleep:", W6C1)

 print("How many hours are you to sleep?")
 sleepB.sleep = input()

 return  W3C, W4C, W5C, W6C

#sleep = sleepB.sleep 
sleepB()



