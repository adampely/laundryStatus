from flask import Flask, render_template
import RPi.GPIO as GPIO
from mpu6050 import mpu6050
from accelVibeInTimeInterval import accelVibeInTimeInterval

app = Flask(__name__)

@app.route('/')
def index():
    sensor1, sensor2 = accelVibeInTimeInterval()
    buttonDict = {'button1Str': 'washer off', 'button2Str' : 'dryer off'}
    if sensor1:
        buttonDict['button1Str'] = 'washer on'
    if sensor2:
        buttonDict['button2Str'] = 'dryer on'
        
    return render_template('buttonStatus.html', **buttonDict)





if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0')
