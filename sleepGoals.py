from time import gmtime, strftime 
import time

"""calculates de time you should wake up given a bed time hour"""
#good night sleep is between 5/6 cycles
#takes 15 min for someone to fall asleep 

def sleepW():
   
 #https://docs.python.org/3/library/time.html
 t = strftime("%H:%M", gmtime())


 hours, minutes = t.split(":") 
 H = int (hours) 
 M = int (minutes)
 cycle = 90  


 # it takes an average of 15 min to fall asleep

 minTimeC3 = ( 15 + ((H * 60) + M) + (3 * cycle)) #4.5h of sleep
 secTimeC3 = 60 * minTimeC3

 minTimeC4 = ( 15 + ((H * 60) + M) + (4 * cycle)) #6h of sleep
 secTimeC4 = 60 * minTimeC4

 minTimeC5 = ( 15 + ((H * 60) + M) + (5 * cycle)) #7.5h of sleep
 secTimeC5 = 60 * minTimeC5

 minTimeC6 = ( 15 + ((H * 60) + M) + (6 * cycle)) #9h of sleep
 secTimeC6 = 60 * minTimeC6

 W3C = time.strftime("%H:%M", time.gmtime(secTimeC3))
 W4C = time.strftime("%H:%M", time.gmtime(secTimeC4))
 W5C = time.strftime("%H:%M", time.gmtime(secTimeC5))
 W6C = time.strftime("%H:%M", time.gmtime(secTimeC6))



 print("If you going to bed now, you should wake up at one of these times: ")
 print("4h and 30 min of sleep:", W3C)
 print("6h of sleep:", W4C)
 print("7h and 30 min of sleep:", W5C)
 print("9h of sleep:", W6C)

 
 print("How many hours are you to sleep?")
 sleepW.sleep = input()
 
 return  W3C, W4C, W5C, W6C

sleep = sleepW.sleep
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
 secTimeC3 = 60 * minTimeC3

 minTimeC4 = ( 15 + ((H * 60) + M) - (4 * cycle)) #6h of sleep
 secTimeC4 = 60 * minTimeC4

 minTimeC5 = ( 15 + ((H * 60) + M) - (5 * cycle)) #7.5h of sleep
 secTimeC5 = 60 * minTimeC5

 minTimeC6 = ( 15 + ((H * 60) + M) - (6 * cycle)) #9h of sleep
 secTimeC6 = 60 * minTimeC6

 W3C = time.strftime("%H:%M", time.gmtime(secTimeC3))
 W4C = time.strftime("%H:%M", time.gmtime(secTimeC4))
 W5C = time.strftime("%H:%M", time.gmtime(secTimeC5))
 W6C = time.strftime("%H:%M", time.gmtime(secTimeC6))



 print("If you wanto to wake up at ", t," you should go to bed at one of these times: ")
 print("4h and 30 min of sleep:", W3C)
 print("6h of sleep:", W4C)
 print("7h and 30 min of sleep:", W5C)
 print("9h of sleep:", W6C)

 print("How many hours are you to sleep?")
 sleepB.sleep = input()

 return  W3C, W4C, W5C, W6C

sleep = sleepB.sleep 
sleepB()



