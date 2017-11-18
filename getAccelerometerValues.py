from math import sqrt

def getAccelerometerValues(sensor1, sensor2):
    accelerometer_data1 = sensor1.get_accel_data()
    accelerometer_data2 = sensor2.get_accel_data()
    accel1 = sqrt(accelerometer_data1['x']**2 +
                  accelerometer_data1['y']**2 +
                  accelerometer_data1['z']**2)
    absAccel1 = abs(accel1-9.8)
    accel2 = sqrt(accelerometer_data2['x']**2 +
                  accelerometer_data2['y']**2 +
                  accelerometer_data2['z']**2)
    absAccel2 = abs(accel2-9.8)
    return absAccel1, absAccel2
