import RPi.GPIO as GPIO
import time
from math import *
from collections import OrderedDict
from datetime import datetime
from twilio.rest import Client
from accelVibeInTimeInterval import accelVibeInTimeInterval

def printFunction1(channel):
    global personIndex
    global personList
    personIndex = (personIndex + 1) % (len(personList)*2) #includes person and wash/dry info (values above 1/2 * len(personList) are dry while below are wash
    personIdx2 = personIndex % len(personList) #This reduces personIndex to person with no wash/dry info
    print(personIndex)
    #LED control for wash/dry
    if personIndex > len(personList)-1:
        GPIO.output(16, False)
        GPIO.output(12, True)
    else:
        GPIO.output(16, True)
        GPIO.output(12, False)
        
    #LED controls for person
    if personIdx2 == 0:
        GPIO.output(13, False)
        GPIO.output(19, False)
        GPIO.output(26, True)
    elif personIdx2 == 1:
        GPIO.output(13, False)
        GPIO.output(19, True)
        GPIO.output(26, False)
    elif personIdx2 == 2:
        GPIO.output(13, True)
        GPIO.output(19, False)
        GPIO.output(26, False)
    elif personIdx2 == 3:
        GPIO.output(13, False)
        GPIO.output(19, True)
        GPIO.output(26, True)
    elif personIdx2 == 4:
        GPIO.output(13, True)
        GPIO.output(19, False)
        GPIO.output(26, True)
    elif personIdx2 == 5:
        GPIO.output(13, True)
        GPIO.output(19, True)
        GPIO.output(26, False)
        
    print('personIndex :', list(personList.keys())[personIdx2])

def goFunction(channel):
    global personIndex
    global personList
    global washerCase
    global drierCase
    personIdx2 = personIndex % len(personList)
    if personIndex > (len(personList)-1):
        washerDrierVal = 1
    else:
        washerDrierVal = 1
    if washerDrierVal == 1:
        washerCase = [list(personList.keys())[personIdx2],
                      list(personList.values())[personIdx2],
                      datetime.now()]
        print(washerCase)
    if washerDrierVal == 0:
        drierCase = [list(personList.keys())[personIdx2],
                     list(personList.values())[personIdx2],
                     datetime.now()]
        #print(drierCase)

def textUser(activeCaseList):
    phoneNumber = activeCaseList[1]
    
    account_sid = "ACa03f275640ab4ab523a2c594ba61699d"
    auth_token = "21299aab68d19d77a0037e3e701d6a2f"
    client = Client(account_sid, auth_token)

    '''message = client.messages.create(
    body = "Your laundry is done",
    to = phoneNumber,
    from_ = "14806668508")'''

if __name__ == '__main__':
    global personIndex
    global personList
    global washerCase
    global drierCase
    washerCase = []
    sensorValue = 0;
    personList = OrderedDict([('Adam', '+19199859093'), ('Timmy', '+19199859093'),
                             ('Paul', '+19199859093'), ('Jordan', '+19199859093'),
                             ('Alby', '+19199859093'), ('Nicole', '+19199859093')])
    personIndex = 1
    GPIO.setmode(GPIO.BCM)
    # user scroll and submit buttons
    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    
    # Washer/Dryer LEDs
    GPIO.setup(12, GPIO.OUT) #Green LED
    GPIO.setup(16, GPIO.OUT) #Blue LED
    
    # User LEDs
    GPIO.setup(13, GPIO.OUT) #Red LED
    GPIO.setup(19, GPIO.OUT) #Blue LED
    GPIO.setup(26, GPIO.OUT) #Green LED
    
    #Reaction to input button events
    GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction1, bouncetime=200)
    GPIO.add_event_detect(24, GPIO.RISING, callback=goFunction, bouncetime=200)
    print(len(washerCase))
    indexBelowThresh = 0
    deadTimeNeeded = 10 #deadtime of a sensor to send text (in seconds)
    try: #in a try statement to ensure LEDs shut off on exit
        while True:
            time.sleep(0.1)
            #print(len(washerCase))
            if len(washerCase) > 0:
                sensor1, sensor2 = accelVibeInTimeInterval(timeInterval = 10, accelThreshold = 1)
                print(sensor1)
                if sensor1 is True:
                    indexBelowThresh = indexBelowThresh + 1
                    print('machine running')
                else:
                    print('machineOff')
                    #text the person in the active case and delete their case
                    #textUser(washerCase)
                    print('texted user')
                    washerCase = []
    except:
        GPIO.cleanup()
                
            
                
                
