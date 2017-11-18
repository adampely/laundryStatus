from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def index():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    buttonDict = {'button1Str': 'off', 'button2Str' : 'off'}
    if GPIO.input(23):
        buttonDict['button1Str'] = 'on'
    if GPIO.input(24):
        buttonDict['button2Str'] = 'on'
        
    return render_template('buttonStatus.html', **buttonDict)





if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
