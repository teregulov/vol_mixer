


import serial.tools.list_ports
ports = serial.tools.list_ports.comports()

import threading

for port, desc, hwid in sorted(ports):
        print (f"{port}, {desc}, {hwid}")
        # print("{}: {} [{}]".format(port, desc, hwid))



ser = serial.Serial()
ser.baudrate = 9600
ser.port = 'COM20'







def serial_reading():
    ser.open()
    while True:
        s = ser.readline()
        print(s)
    ser.close()
 

def main():
    thread = threading.Thread(target=serial_reading)
    thread.start()

if __name__ == "__main__":
     main()