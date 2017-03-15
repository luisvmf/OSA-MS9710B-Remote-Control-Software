#instalar o modulo pyserial
import serial
import sys
import time
device=sys.argv[1]
ser = serial.Serial(''+device+'', 9600, timeout=0,
                     parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
ser.write("MOD?\n")
cnt=0
while cnt<90000:
        byte = ser.read(size=1)
        sys.stdout.write(byte),
	cnt=cnt+1
ser.write("*CLS\n")
ser.close()
time.sleep(2)
