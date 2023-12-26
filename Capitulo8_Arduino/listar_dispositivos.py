import serial
from serial.tools import list_ports

#lista as portas do arduino;

for port in list_ports.comports():
    print('Dispositivo: {} - porta: {} '.format(port.description, port.device))