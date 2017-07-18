#!/usr/bin/env python

import serial
import time

print "\r\n==>To test ble light...\r\n"

# The serial port configuration
ser = serial.Serial(
        port = '/dev/ttyUSB0',
        baudrate = 115200,
        bytesize = serial.EIGHTBITS,
        parity = serial.PARITY_NONE,
        stopbits = serial.STOPBITS_ONE,
        timeout = 0.5,
        xonxoff = None,
        rtscts = None,
        interCharTimeout = None
        )
print ser.portstr
ser.isOpen()
try:
    while 1 :        
        RecvData = ''
        time.sleep(2)    
        while ser.inWaiting() > 0 :
            RecvData += ser.read(1)
        if RecvData != '':
            print "<<" + RecvData
        
        InPut = raw_input(">>")
        if InPut == 'exit':
            ser.close()
            exit()
        else:
            #string data
            ser.write(InPut + "\r\n")
            #hex data
            #ser.write(InPut.decode("hex"))
finally:
    ser.close()
    exit()

