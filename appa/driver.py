import struct
import time

import serial

REQUEST_CURRENT_STATE_COMMAND = b"\x55\x55\x00\x00\xAA"

MODES = {
    '0100': 'Voltage AC',
    '0101': 'Voltage DC',
    '0102': 'Voltage AC + DC',
    '0200': 'mVoltage AC',
    '0201': 'mVoltage DC',
    '0202': 'mVoltage AC + DC',
    '0300': 'Resistance',
    '0301': 'Resistance Low Voltage',
    '0400': 'p-n Test',
    '0401': 'Continuity Test',
    '0500': 'mCurrent AC',
    '0501': 'mCurrent DC',
    '0502': 'mCurrent AC + DC',
    '0600': 'Current AC',
    '0601': 'Current DC',
    '0602': 'Current AC + DC',
    '0700': 'Capacitance',
    '0800': 'Frequency',
    '0801': 'Duty Factor',
    '0900': 'Temperature C',
    '0901': 'Temperature F',
}


class AppaDriver:
    def __init__(self, port: str, baudrate: int = 9600):
        self.ser = serial.Serial(
            port=port,
            baudrate=baudrate,
            stopbits=serial.STOPBITS_TWO,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE
        )

    def isOpen(self):
        return self.ser.isOpen()

    def close(self):
        self.ser.close()

    def getCurrentState(self):
        self.ser.write(REQUEST_CURRENT_STATE_COMMAND)
        time.sleep(0.4)
        data = self.ser.read(self.ser.inWaiting())
        return AppaState(data)


class AppaState:
    def __init__(self, data: bytes):
        self.raw = data
        self.mode_raw = data[4:6]
        self.mode = MODES[self.mode_raw.hex()] if self.mode_raw and self.mode_raw.hex() in MODES else 'Unknown'
        self.value_raw = data[8:10]
        self.value = struct.unpack('h', self.value_raw)  # struct.unpack('e', self.value_raw)
        print(len(data))

    def __repr__(self):
        return "Raw: " + self.raw.hex() + " mode: " + self.mode + " value: " + self.value.__repr__()


if __name__ == '__main__':
    driver = AppaDriver('/dev/tty.usbserial-14130')
    driver.isOpen()
    n = 0
    while n < 1000:
        print(driver.getCurrentState())
        n = n + 1
    driver.close()

# 55 55 00 0e 01 01 00 00 2f 37 00 0c 01 0000000000 2d
# 55 55 00 0e 01 01 00 00 01 00 00 0c 01 0000000000 c8
# 55 55 00 0e 03 00 00 05 20 4e 00 63 01 0000000000 92
# 55 55 00 0e 03 00 00 05 5b 14 00 63 01 0000000000 93 – 5.211 MOhm
# 55 55 00 0e 03 00 00 80 20 4e 00 52 01 0000000000 fc – Infinite Ohm
# 55 55 00 0e 03 00 00 81 d0 07 00 5c 01 0000000000 70 – Infinite kOhm, 82? - MOhm, 83? - GOhm
# 55 55 00 0e 03 00 00 05 e2 2e 00 63 01 0000000000 34
# 55 55 00 0e 01 00 00 03 e3 08 00 09 01 0000007902 2c – 227.5 V AC
