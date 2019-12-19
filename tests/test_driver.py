import unittest
from unittest import mock

from appa.driver import AppaDriver


class MyTestCase(unittest.TestCase):

    @mock.patch("serial.Serial", create=True)
    def test_is_open(self, mock_serial):
        driver = AppaDriver('COM1')
        driver.ser.isOpen.return_value = False
        self.assertFalse(driver.is_open())
        driver.ser.isOpen.assert_called()

    @mock.patch("serial.Serial", create=True)
    def test_close(self, mock_serial):
        driver = AppaDriver('COM1')
        driver.close()
        driver.ser.close.assert_called()

    @mock.patch("serial.Serial", create=True)
    def test_read_data(self, mock_serial):
        raw_data = b'\x55\x55\x00\x0e\x01\x01\x00\x00\x2f\x37\x00\x0c\x01\x00\x00\x00\x00\x00\x2d'
        driver = AppaDriver('COM1')
        driver.ser.read.return_value = raw_data
        data = driver.read_data()
        driver.ser.write.assert_called_with(b"\x55\x55\x00\x00\xAA")
        print(data)
        self.assertTrue(data)
        self.assertEqual('Voltage DC', data.mode.name)
        self.assertEqual('2 V', data.range.name)
        self.assertEqual('2', data.range.max)
        self.assertEqual(True, data.range.auto)
        self.assertEqual('1.4127', data.value)
        self.assertEqual('V', data.unit)
        self.assertEqual('0.0', data.sub_value)
        self.assertEqual('None', data.sub_unit)
        self.assertEqual('\\x55\\x55\\x00\\x0e\\x01\\x01\\x00\\x00\\x2f\\x37\\x00\\x0c\\x01\\x00\\x00\\x00\\x00\\x00\\x2d', data.get_raw())


if __name__ == '__main__':
    unittest.main()
