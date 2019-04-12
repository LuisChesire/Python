import json 
import serial
import time
#archivo = "C:/Users/Breack/Desktop/l//a.txt"
puerto = "COM6"
ser = serial.Serial(puerto,9600, timeout = 10)
#bar = open('lol.txt','a')

while True:
	try:
		if ser.inWaiting()>0:
			rx = ser.readln()
			Fecha = time.strftime("%x")
			Hora = time.strftime("%X")
			#print(rx)
			#bar.write(str(rx)+"\n")
			#bar.write(str(fecha)+"\n")
			#ser.flushInput()  
			data = {"fecha": Fecha,"hora": Hora, "dato": rx}
			with open('data.json', 'w') as file:
				json.dump(data, file, indent=4)
	except KeyboardInterrupt:
			#bar.write("no hay nada aqui\n")
			print ('\n Program Stopped')
			break