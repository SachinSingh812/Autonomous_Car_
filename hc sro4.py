from socket import*
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_ip='DESKTOP-QV5HS8F'
port=6542
s.connect((host_ip,port))

trig=15
echo=16

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(trig,GPIO.IN)

GPIO.OUTPUT(trig,False)
time.sleep(10)

GPIO.OUTPUT(trig,True)
time.sleep(0.0001)

GPIO.OUTPUT(trig,False)

while GPIO.input(echo)==0:
    pulse_begin=time.time()
    
while GPIO.input(echo)==1:
    pulse_end=time.time()

pulse_time=pulse_end-pulse_begin

distance=pulse_time*17150
print(distance)

s.send(str(distance))
time.sleep(0.5)
s.close()
GPIO.cleanup()
