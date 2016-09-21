#!/usr/bin/env python

import serial
import time

print "\r\n==>To test NBIoT module...\r\n"

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


ser.write('ATI\r\n')
time.sleep(0.2)    # We must have a delay here otherwise we can't get the RX data.
ser_buffer_size = ser.inWaiting()

reply_data = ser.read(ser_buffer_size)

print '\r\n==>Data replied:\r\n', reply_data
print '\r\n==>ser buffer size:\r\n', ser_buffer_size

# Send AT command and check the response string
def sendCMD (cmd_str,check_str):
    ser.reset_input_buffer()
    dataRev = ''
    print '\r\n==>Send command and verify...\r\n'
    ser.write(cmd_str)
    time.sleep(0.2)
    dataRev = ser.read(ser.inWaiting())
    if check_str in dataRev:
        return 1
    else:
        return 0

x = sendCMD('ATI\r\n','ok')
print x

ser.close()
