from mpu6050 import mpu6050
from math import sqrt
from time import sleep
from numpy import array
from getAccelerometerValues import getAccelerometerValues
import numpy as np

def accelVibeInTimeInterval(timeInterval = 5, accelThreshold = 1)
    '''
    This function will run through the accelerometer values over the time
    interval indicated in timeInterval. If at any point during the timeInterval
    the value exceeds the threshold value it will return a true else, it will return
    false
    timeInterval = time interval over which accelerometer value is checked in seconds
    accelThreshold = acceleration over 1g which the accelerometer must exceed to be
        considered on. Value in m/s^2 
    '''
    sensor1 = mpu6050(0x68)
    sensor2 = mpu6050(0x69)
    sensor1On = False
    sensor2On = False
    accelList1 = []
    accelList2 = []
    for loopTimer in range(timeInterval*10):
        absAccel1, absAccel2 = getAccelerometerValues(sensor1, sensor2)
        accelList1.append(absAccel1)
        accelList2.append(absAccel2)
        sleep(0.1)

    if max(accelList1)>accelThreshold:
        sensor1On = True
    if max(accelList2)>accelThreshold:
        sensor2On = True

    return sensor1On, sensor2On
