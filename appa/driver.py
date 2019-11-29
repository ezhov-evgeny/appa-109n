import time

import serial

from appa.protocol import REQUEST_READ_DATA_COMMAND, DataParser


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
        return self.parser.parse(data) if data else ''


if __name__ == '__main__':
    driver = AppaDriver('/dev/tty.usbserial-14130')
    driver.is_open()
    n = 0
    while n < 1000:
        data = driver.read_data()
        print(data.get_raw())
        print(data)
        n = n + 1
        time.sleep(1)
    driver.close()
