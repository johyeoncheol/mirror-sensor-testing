import RPi.GPIO as gpio
import time
 
gpio.setmode(gpio.BCM)
gpio.setwarnings(False)
 
sig = 23


try:
    while True:
        gpio.setup(sig,gpio.OUT)
        gpio.output(sig,False)
        time.sleep(0.5)
        
        gpio.output(sig, True)
        time.sleep(0.00001)
        gpio.output(sig,False)
        
        gpio.setup(sig,gpio.IN)
        while gpio.input(sig)==False:
            pulse_start = time.time()
             
        while gpio.input(sig)==True:
            pulse_end = time.time()
             
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round(distance,2)
          
        print("Distance: " , distance,"cm")
        
         
except:
   gpio.cleanup()