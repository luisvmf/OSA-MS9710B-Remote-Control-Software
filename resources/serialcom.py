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

scale=sys.argv[8]
time.sleep(1.5)
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

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#verificando comprimento de onda de inicio e fim.
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
STA=""
contador=0
effveefv=0
ser.write("STA?\n")
#print("Enviado STA?")
while contador<1:
	byteb = ser.read(size=1)
	effveefv=effveefv+1
	if effveefv>25000:
		raise Exception('This is the exception you expect to handle')
	if byteb=="\n":
		contador=contador+1
        if byteb!="\n":
		if byteb!="\r":
			if byteb!="\r\n":
        			STA=STA+byteb
STO=""
contador=0
ser.write("STO?\n")
effveefv=0
#print("Enviado STO?")
while contador<1:
	bytec = ser.read(size=1)
	effveefv=effveefv+1
	if effveefv>25000:
		raise Exception('This is the exception you expect to handle')
	if bytec=="\n":
		contador=contador+1
	if bytec!="\n":
		if bytec!="\r":
			if bytec!="\r\n":
        			STO=STO+bytec






smoothatualOSAjfvggg=""
contador=0
effveefv=0
ser.write("SMT?\n")
#print("Enviado SMT?")
while contador<1:
	bytec = ser.read(size=1)
	effveefv=effveefv+1
	if effveefv>25000:
		raise Exception('This is the exception you expect to handle')
	if bytec=="\n":
		contador=contador+1
	if bytec!="\n":
		if bytec!="\r":
			if bytec!="\r\n":
        			smoothatualOSAjfvggg=smoothatualOSAjfvggg+bytec





#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
trocouiniciooufim=0
if float(start)!=float(STA):
	ser.write("STA "+start+"\n")
	#print("Enviado STA")
	trocouiniciooufim=1
if float(stop)!=float(STO):
	ser.write("STO "+stop+"\n")
	#print("Enviado STO")
	trocouiniciooufim=1
if boxcar+""!=smoothatualOSAjfvggg+"":
	ser.write("SMT "+boxcar+"\n")
	#print("Enviado SMT")
	trocouiniciooufim=1
	time.sleep(3)
if trocouiniciooufim==1:
	ser.write("*CLS\n")




STA=""
contador=0
ser.write("STA?\n")
#print("Enviado STA?")
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
#print("Enviado STO?")
while contador<1:
	bytec = ser.read(size=1)
	if bytec=="\n":
		contador=contador+1
	if bytec!="\n":
		if bytec!="\r":
			if bytec!="\r\n":
        			STO=STO+bytec



smoothatualOSAjfvggg=""
contador=0
ser.write("SMT?\n")
#print("Enviado SMT?")
while contador<1:
	bytec = ser.read(size=1)
	if bytec=="\n":
		contador=contador+1
	if bytec!="\n":
		if bytec!="\r":
			if bytec!="\r\n":
        			smoothatualOSAjfvggg=smoothatualOSAjfvggg+bytec













if float(start)!=float(STA):
	ser.write("STA "+start+"\n")
	#print("Enviado STA")
	trocouiniciooufim=1
if float(stop)!=float(STO):
	ser.write("STO "+stop+"\n")
	#print("Enviado STO")
	trocouiniciooufim=1
if boxcar+""!=smoothatualOSAjfvggg+"":
	ser.write("SMT "+boxcar+"\n")
	#print("Enviado SMT")
	time.sleep(3)
	trocouiniciooufim=1
if trocouiniciooufim==1:
	ser.write("*CLS\n")




if float(start)!=float(STA):
	raise Exception('This is the exception you expect to handle')
if float(stop)!=float(STO):
	raise Exception('This is the exception you expect to handle')
if boxcar+""!=smoothatualOSAjfvggg+"":
	raise Exception('This is the exception you expect to handle')

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
ser.write(scale+" 1\n")
ser.write("*CLS\n")

ser.write("*CLS\n")
ser.write("MPT "+a+"\n")
ser.write("RES "+b+"\n")
ser.write("AVT "+avarages+"\n")
ser.write(scale+" 1\n")
ser.write("*CLS\n")


ser.write("*CLS\n")


ser.write("SSI\n")
#ser.write("SMT "+boxcar+"\n")

ser.write("RES?\n")
ser.write("*CLS\n")
#ser.write("DMA?\n")

ser.close()
time.sleep(4.5)
print("Enviado SSI")
