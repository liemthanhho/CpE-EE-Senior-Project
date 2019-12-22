import serial #for Serial communication
import time   #for delay functions
 
arduino = serial.Serial('/dev/ttyUSB0',9600) #Create Serial port object called arduinoSerialData
time.sleep(2) #wait for 2 secounds for the communication to get established

print arduino.readline() #read the serial data and print it as line
print ("Enter 1 to get LED ON & 0 to get OFF")

 
while 1:      #Do this in loop

    var = raw_input() #get input from user
   
    
    if (var == '1'): #if the value is 1
        arduino.write('1') #send 1
        print ("LED turned ON")
        time.sleep(1)
    
    if (var == '0'): #if the value is 0
        arduino.write('0') #send 0
        print ("LED turned OFF")
        time.sleep(1)