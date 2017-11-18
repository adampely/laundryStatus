from flask import Flask, render_template
import RPi.GPIO as GPIO
import time
from math import *
from collections import OrderedDict
from datetime import datetime
from twilio.rest import Client
from accelVibeInTimeInterval import accelVibeInTimeInterval


def index():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    buttonDict = {'button1Str': 'off', 'button2Str' : 'off'}
    if GPIO.input(23):
        buttonDict['button1Str'] = 'on'
    if GPIO.input(24):
        buttonDict['button2Str'] = 'on'
    return render_template('buttonStatus.html', **buttonDict)

def printFunction1(channel):
    global personIndex
    global personList
    personIndex = (personIndex + 1) % len(personList)
    print('personIndex :', list(personList.keys())[personIndex])

def goFunction(channel):
    global personIndex
    global personList
    global washerCase
    global drierCase
    washerDrierVal = 1
    if washerDrierVal == 1:
        washerCase = [list(personList.keys())[personIndex],
                      list(personList.values())[personIndex],
                      datetime.now()]
        print(washerCase)
    if washerDrierVal == 0:
        drierCase = [list(personList.keys())[personIndex],
                     list(personList.values())[personIndex],
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

    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction1, bouncetime=200)
    GPIO.add_event_detect(24, GPIO.RISING, callback=goFunction, bouncetime=200)
    print(len(washerCase))
    indexBelowThresh = 0
    deadTimeNeeded = 10 #deadtime of a sensor to send text (in seconds)
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
                
            
                
                
