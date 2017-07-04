#instalar o modulo pyserial
import serial
import sys
import time
device=sys.argv[2]
time.sleep(1.7)
#ser = serial.Serial(''+device+'', 9600, timeout=0,
#                     parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
try:
	ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
	ser.write("*CLS\n")
except serial.serialutil.SerialException:
	time.sleep(1)
	try:
		ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
		ser.write("*CLS\n")
	except serial.serialutil.SerialException:
		time.sleep(3)
		try:
			ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
			ser.write("*CLS\n")
		except serial.serialutil.SerialException:
			time.sleep(5)
			try:
				ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
				ser.write("*CLS\n")
			except serial.serialutil.SerialException:
				time.sleep(3)
				ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
				ser.write("*CLS\n")
ser.write("DMA?\n")
numerodados=int(float(sys.argv[1]))
contador=0
conta=0
while contador<(numerodados):
        byte = ser.read(size=1)
	if byte=="\n":
		contador=contador+1
        sys.stdout.write(byte),
#	if conta==1:
#		contador=contador+1
ser.write("*CLS\n")
ser.close()
time.sleep(2)
