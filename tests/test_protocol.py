import unittest

from appa.protocol import DataFormat, DataParser, VALUE_INFINITE

TEST_DATA = {
    b'\x55\x55\x00\x0e\x03\x00\x00\x05\x5b\x14\x00\x63\x01\x00\x00\x00\x00\x00\x93': {'mode': 'Resistance', 'range': '20 MOhm', 'unit': 'MOhm', 'val': '5.211'},
    b'\x55\x55\x00\x0e\x03\x00\x00\x80\x20\x4e\x00\x52\x01\x00\x00\x00\x00\x00\xfc': {'mode': 'Resistance', 'range': '200 Ohm', 'unit': 'Ohm',
                                                                                      'val': VALUE_INFINITE},
    b'\x55\x55\x00\x0e\x01\x00\x00\x03\xe3\x08\x00\x09\x01\x00\x00\x00\x79\x02\x2c': {'mode': 'Voltage AC', 'range': '750 V', 'unit': 'V', 'val': '227.5'},
    b'\x55\x55\x00\x0e\x03\x00\x00\x81\xd0\x07\x00\x5c\x01\x00\x00\x00\x00\x00\x70': {'mode': 'Resistance', 'range': '2 kOhm', 'unit': 'KOhm', 'val': '0.2000'},
    b'\x55\x55\x00\x0e\x03\x00\x00\x05\x20\x4e\x00\x63\x01\x00\x00\x00\x00\x00\x92': {'mode': 'Resistance', 'range': '20 MOhm', 'unit': 'MOhm',
                                                                                      'val': VALUE_INFINITE},
    b'\x55\x55\x00\x0e\x01\x01\x00\x00\x01\x00\x00\x0c\x01\x00\x00\x00\x00\x00\xc8': {'mode': 'Voltage DC', 'range': '2 V', 'unit': 'V', 'val': '0.0001'},
    b'\x55\x55\x00\x0e\x01\x01\x00\x00\x78\xcc\xff\x0c\x01\x00\x00\x00\x00\x00\xff': {'mode': 'Voltage DC', 'range': '2 V', 'unit': 'V', 'val': '-1.3192'},
    b'\x55\x55\x00\x0e\x01\x01\x00\x00\xff\xff\xff\x0c\x01\x00\x00\x00\x00\x00\xc4': {'mode': 'Voltage DC', 'range': '2 V', 'unit': 'V', 'val': '-0.0001'},
    b'\x55\x55\x00\x0e\x01\x01\x00\x00\x2f\x37\x00\x0c\x01\x00\x00\x00\x00\x00\x2d': {'mode': 'Voltage DC', 'range': '2 V', 'unit': 'V', 'val': '1.4127'},
    b'\x55\x55\x00\x0e\x04\x00\x00\x80\x27\x05\x00\x0b\x01\x00\x00\x00\x00\x00\x74': {'mode': 'p-n Test', 'range': '2 V', 'unit': 'V', 'val': '1.319'},
    b'\x55\x55\x00\x0e\x04\x00\x00\x80\x00\x00\x00\x0b\x01\x00\x00\x00\x00\x00\x48': {'mode': 'p-n Test', 'range': '2 V', 'unit': 'V', 'val': '0.0'},
    b'\x55\x55\x00\x0e\x04\x01\x00\x80\x00\x00\x00\x51\x00\x00\x00\x00\x00\x00\x8e': {'mode': 'Continuity Test', 'range': '200 Ohm', 'unit': 'Ohm',
                                                                                      'val': '0.0'},
    b'\x55\x55\x00\x0e\x04\x01\x00\x80\x00\x00\x00\x51\x01\x00\x00\x00\x00\x00\x8f': {'mode': 'Continuity Test', 'range': '200 Ohm', 'unit': 'Ohm',
                                                                                      'val': '0.0'},
    b'\x55\x55\x00\x0e\x04\x01\x00\x80\xd0\x07\x00\x51\x01\x00\x00\x00\x00\x00\x66': {'mode': 'Continuity Test', 'range': '200 Ohm', 'unit': 'Ohm',
                                                                                      'val': VALUE_INFINITE},
}


class TestStateParser(unittest.TestCase):
    parser = DataParser()

    def test_data_format(self):
        data = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x10\x11\x12\x13\x14\x15\x16\x17\x18'
        d = DataFormat(data)
        self.assertEqual('0405', d.mode)
        self.assertEqual('07', d.range)
        self.assertEqual(b'\x08\x09\x10', d.main_value)
        self.assertEqual('00010001', d.main_state)
        self.assertEqual('12', d.main_function)
        self.assertEqual('1314151617', d.sub)
        self.assertEqual('18', d.checksum)

    def test_parse_data(self):
        for raw in TEST_DATA:
            data = self.parser.parse(raw)
            print(data)
            expected = TEST_DATA[raw]
            self.assertEqual(expected['mode'], data.mode.name)
            self.assertEqual(expected['range'], data.range.name)
            self.assertEqual(expected['unit'], data.unit)
            self.assertEqual(expected['val'], data.value)
