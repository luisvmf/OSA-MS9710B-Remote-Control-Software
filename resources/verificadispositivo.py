#instalar o modulo pyserial
import serial
import sys
import time
device=sys.argv[1]
ser = serial.Serial(''+device+'', 9600, timeout=0,
                     parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
ser.close()
time.sleep(2)
