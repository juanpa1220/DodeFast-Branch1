import serial
import time


class ArduinoServer:
    def __init__(self, lista):
        try:
            port = "/dev/tty.HC-05-DevB"
            bluetooth = serial.Serial(port, 9600)
            print("Connected")
            bluetooth.flushInput()
            time.sleep(5)
            for i in lista:
                bluetooth.write(b"" + str.encode(str(i)))
                input_data = bluetooth.readline()
                print(input_data.decode())
                time.sleep(4)
            bluetooth.close()
        except:
            print("Error: no hay conexion")


lista = ['AF', 'F', 'DFA', 'IFA', 'DFB', 'IFB',
         'A', 'DAA', 'IAA', 'DAB', 'IAB', 'AA']
arduinoServer = ArduinoServer(lista)
