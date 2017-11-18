from mpu6050 import mpu6050
from math import sqrt
from time import sleep
from numpy import array
from getAccelerometerValues import getAccelerometerValues
import numpy as np
sensor1 = mpu6050(0x68)
sensor2 = mpu6050(0x69)
while True:
    accelList1 = []
    accelList2 = []
    for loopTimer in range(50):
        absAccel1, absAccel2 = getAccelerometerValues(sensor1, sensor2)
        accelList1.append(absAccel1)
        accelList2.append(absAccel2)
        sleep(0.1)

    if max(accelList1)>1:
        print('sensor 1 still vibrating')
    else:
        print('sensor 1 stationary')
    if max(accelList2)>1:
        print('sensor 2 still vibrating')
    else:
        print('sensor 2 stationary')
    
