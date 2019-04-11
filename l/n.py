import serial
import time
archivo = "C:/Users/Breack/Desktop/l//a.txt"
puerto = "COM6"
ser = serial.Serial(puerto,9600, timeout = 10)
bar = open('lol.txt','a')

while True:
	try:
		if ser.inWaiting()>0:
			rx = ser.read(2)
			fecha = time.strftime("fecha: %x \nHora:%X")
			print(rx)
			bar.write(str(rx)+"\n")
			bar.write(str(fecha)+"\n")
			ser.flushInput()  
	except KeyboardInterrupt:
			#bar.write("no hay nada aqui\n")
			print ('\n Program Stopped')
			bar.close()
			break