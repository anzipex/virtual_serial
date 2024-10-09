import serial
import time

port = '/dev/pts/1'
baudrate = 115200

try:
    ser = serial.Serial(port, baudrate, timeout=1)
    # Time to open the port
    time.sleep(2)
    
    data_to_send = b'Hello, World!\n'
    ser.write(data_to_send)
    print(f'Sent: {data_to_send}')
    
    ser.close()
except serial.SerialException as e:
    print(f'Error opening/writing to serial port: {e}')
