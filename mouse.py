import serial
import serial.tools.list_ports
import time
import sys
from termcolor import colored

class ArduinoMouse:
    def __init__(self):
        self.serial_port = serial.Serial()
        self.serial_port.baudrate = 115200
        self.serial_port.timeout = 1
        self.serial_port.port = self.find_serial_port()

        try:
            self.serial_port.open()
            print(colored('[Info]', 'green'), colored(f'Connected to {self.serial_port.port}', 'white'))
        except serial.SerialException as e:
            print(colored('[Error]', 'red'), colored('Failed to open serial port. Check if it is busy or unplugged.', 'white'))
            print(colored('[Exception]', 'red'), colored(str(e), 'white'))
            sys.exit()

    def find_serial_port(self):
        ports = serial.tools.list_ports.comports()
        for port in ports:
            if "Arduino" in port.description or "CH340" in port.description:
                return port.device
        print(colored('[Warning]', 'yellow'), colored('Could not auto-detect Arduino. Falling back to COM13...', 'white'))
        return "COM13"  # fallback nếu không tìm được

    def move(self, x, y):
        x = x + 256 if x < 0 else x
        y = y + 256 if y < 0 else y
        self.serial_port.write(b"M" + bytes([int(x), int(y)]))

    def click(self):
        self.serial_port.write(b"C")
        time.sleep(0.01)
        self.serial_port.write(b"U")

    def close(self):
        if self.serial_port.is_open:
            self.serial_port.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def __del__(self):
        self.close()
