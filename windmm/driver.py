import time

import serial

from windmm.protocol import REQUEST_READ_DATA_COMMAND, DataParser


class AppaDriver:
    def __init__(self, port: str):
        self.ser = serial.Serial(
            port=port,
            baudrate=9600,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
        )
        self.parser = DataParser()

    def is_open(self):
        return self.ser.isOpen()

    def close(self):
        self.ser.close()

    def read_data(self):
        self.ser.write(REQUEST_READ_DATA_COMMAND)
        time.sleep(0.4)
        data = self.ser.read(self.ser.inWaiting())
        return self.parser.parse(data) if data else None
