#instalar o modulo pyserial
import serial
import sys
import time
a=sys.argv[1]
b=sys.argv[2]
device=sys.argv[3]
avarages=sys.argv[4]
boxcar=sys.argv[5]
start=sys.argv[6]
stop=sys.argv[7]
#ser = serial.Serial(''+device+'', 9600, timeout=0,
#                     parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
try:
	ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
except serial.serialutil.SerialException:
	time.sleep(1)
	try:
		ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
	except serial.serialutil.SerialException:
		time.sleep(3)
		try:
			ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
		except serial.serialutil.SerialException:
			time.sleep(5)
			try:
				ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)
			except serial.serialutil.SerialException:
				time.sleep(3)
				ser = serial.Serial(''+device+'', 9600, timeout=0,parity=serial.PARITY_NONE,bytesize=serial.EIGHTBITS,stopbits=serial.STOPBITS_ONE, rtscts=1)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#verificando comprimento de onda de inicio e fim.
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
STA=""
contador=0
ser.write("STA?\n")
print("Enviado STA?")
while contador<1:
        byteb = ser.read(size=1)
	if byteb=="\n":
		contador=contador+1
        if byteb!="\n":
		if byteb!="\r":
			if byteb!="\r\n":
        			STA=STA+byteb
STO=""
contador=0
ser.write("STO?\n")
print("Enviado STO?")
while contador<1:
        bytec = ser.read(size=1)
	if bytec=="\n":
		contador=contador+1
	if bytec!="\n":
		if bytec!="\r":
			if bytec!="\r\n":
        			STO=STO+bytec
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
trocouiniciooufim=0
if float(start)!=float(STA):
	ser.write("STA "+start+"\n")
	print("Enviado STA")
	trocouiniciooufim=1
if float(stop)!=float(STO):
	ser.write("STO "+stop+"\n")
	print("Enviado STO")
	trocouiniciooufim=1
if trocouiniciooufim==1:
	ser.write("*CLS\n")
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#Espera ate o fim da aquisicao
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
if trocouiniciooufim==1:
	ser.write("*CLS\n")
	ser.write("MOD?\n")
	bytekaaa=1
	fimespera=0
	while float(fimespera)!=1:
  	      byteaaa = ser.read(size=1)
	      if byteaaa!="":
			if byteaaa!="\n":
				if byteaaa!="\r":
					if byteaaa!="\n\r":
						bytekaaa=int(byteaaa)
						if float(bytekaaa)==1:
							time.sleep(2)
							ser.write("*CLS\n")
							ser.write("MOD?\n")
						if float(bytekaaa)==2:
							time.sleep(2)
							ser.write("*CLS\n")
							ser.write("MOD?\n")
						if float(bytekaaa)==3:
							time.sleep(2)
							ser.write("*CLS\n")
							ser.write("MOD?\n")
						if float(bytekaaa)==0:
							time.sleep(2)
							fimespera=1

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
ser.write("*CLS\n")
ser.write("MPT "+a+"\n")
ser.write("RES "+b+"\n")
ser.write("AVT "+avarages+"\n")
ser.write("*CLS\n")
ser.write("SSI\n")
#ser.write("SMT "+boxcar+"\n")
print("Enviado SSI")
ser.write("RES?\n")
ser.write("*CLS\n")
#ser.write("DMA?\n")

ser.close()
time.sleep(2)
