#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:55:15 2023

@author: thilrasirfana
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import binascii
from Crypto.Random import get_random_bytes
import serial



ser = serial.Serial('/dev/tty.usbmodem1402',
                    baudrate=115200, parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS,
                    timeout=1)

file_locationPT = "/Users/thilrasirfana/Desktop/PT.txt"
file_locationCT = "/Users/thilrasirfana/Desktop/CT.txt"
open(file_locationPT, "w") #clear file
open(file_locationCT, "w")
##### End of the setup ####


   
final_array = []
tcounter = 0
counter = 0
    
def get_formatted_hex_string(value): #format string by 2 char = 1 byte
    formatted=''
    for i in range(0,32,2):
        formatted+= value[i]+value[i+1]+' '
    return formatted


c = 1000
NUMBER_OF_TRACES = c
while counter < c:
    plaintext=get_random_bytes(16)
    hexpt=binascii.hexlify(plaintext,' ')
    with open(file_locationPT, "ab") as file_PT : #append PT in file
                    file_PT.write(hexpt)
                    file_PT.write(b'\n')
    ser.write(plaintext)
    print('Start')
    endbyte = ser.read(16)  # Check for CT

    if len(endbyte) == 16:
        print('Encryption has ended')
        hexct=binascii.hexlify(endbyte,' ')
        with open(file_locationCT, "ab") as file_CT :
                        file_CT.write(hexct)
                        file_CT.write(b'\n')
        counter += 1
        print(counter)
    else:
        print('No encryption')





ser.close()