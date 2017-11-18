from twilio.rest import Client
import RPi.GPIO as GPIO

'''account_sid = "ACa03f275640ab4ab523a2c594ba61699d"
auth_token = "21299aab68d19d77a0037e3e701d6a2f"
client = Client(account_sid, auth_token)

message = client.messages.create(
    body = "Your laundry is done",
    to = "+19199859093",
    from_ = "14806668508")'''

GPIO.setmode(GPIO.BCM)

'''GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
while True:
    GPIO.wait_for_edge(23, GPIO.RISING)
    print('Button 1 Pressed')
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print('Button 1 Released')
    GPIO.wait_for_edge(24, GPIO.FALLING)
    print('Button 2 Pressed')
    GPIO.wait_for_edge(24, GPIO.RISING)
    print('Button 2 Released')'''

'''
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
def printFunction(channel):
    print('Button 1 pressed!')
    print('Note how the bouncetime affects the button press')

GPIO.add_event_detect(23, GPIO.RISING, callback=printFunction, bouncetime=200)
while True:
    GPIO.wait_for_edge(24, GPIO.FALLING)
    print('Button 2 Pressed')
    GPIO.wait_for_edge(24, GPIO.RISING)
    print('Button 2 Released')'''




