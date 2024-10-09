import serial
import time

port = '/dev/pts/2'
baudrate = 115200

try:
    ser = serial.Serial(port, baudrate, timeout=1)
    # Time to open the port
    time.sleep(2)

    print("Waiting for data...")
    while True:
        try:
            data_received = ser.read(100)  # Read 100 bytes (can be changed as needed)
            if data_received:
                print("Received raw data: ", data_received)
                hex_data = ' '.join(f'{byte:02x}' for byte in data_received)
                print(f'Received (hex):')
                print(f'{hex_data}')
                print('')
        except serial.SerialException as e:
            print(f'Error reading from serial port: {e}')
            break
except serial.SerialException as e:
    print(f'Error opening serial port: {e}')
except Exception as e:
    print(f'Unexpected error: {e}')
finally:
    if ser.is_open:
        ser.close()
