import struct

REQUEST_READ_DATA_COMMAND = b"\x55\x55\x00\x00\xAA"

MODE_VOLTAGE_AC = '0100'
MODE_VOLTAGE_DC = '0101'
MODE_VOLTAGE_AC_DC = '0102'
MODE_MILLI_VOLTAGE_AC = '0200'
MODE_MILLI_VOLTAGE_DC = '0201'
MODE_MILLI_VOLTAGE_AC_DC = '0202'
MODE_RESISTANCE = '0300'
MODE_RESISTANCE_LV = '0301'
MODE_P_N_TEST = '0400'
MODE_CONTINUITY_TEST = '0401'
MODE_MILLI_CURRENT_AC = '0500'
MODE_MILLI_CURRENT_DC = '0501'
MODE_MILLI_CURRENT_AC_DC = '0502'
MODE_CURRENT_AC = '0600'
MODE_CURRENT_DC = '0601'
MODE_CURRENT_AC_DC = '0602'
MODE_CAPCITANCE = '0700'
MODE_FREQUENCY = '0800'
MODE_DUTY_FACTOR = '0801'
MODE_TEMPERATURE_C = '0900'
MODE_TEMPERATURE_F = '0901'

RANGE_AUTO = '0'
RANGE_MANUAL = '8'
RANGE_0 = '0'
RANGE_1 = '1'
RANGE_2 = '2'
RANGE_3 = '3'
RANGE_4 = '4'
RANGE_5 = '5'
RANGE_6 = '6'
RANGE_7 = '7'

MODES = {
    MODE_VOLTAGE_AC: 'Voltage AC',
    MODE_VOLTAGE_DC: 'Voltage DC',
    MODE_VOLTAGE_AC_DC: 'Voltage AC + DC',
    MODE_MILLI_VOLTAGE_AC: 'mVoltage AC',
    MODE_MILLI_VOLTAGE_DC: 'mVoltage DC',
    MODE_MILLI_VOLTAGE_AC_DC: 'mVoltage AC + DC',
    MODE_RESISTANCE: 'Resistance',
    MODE_RESISTANCE_LV: 'Resistance Low Voltage',
    MODE_P_N_TEST: 'p-n Test',
    MODE_CONTINUITY_TEST: 'Continuity Test',
    MODE_MILLI_CURRENT_AC: 'mCurrent AC',
    MODE_MILLI_CURRENT_DC: 'mCurrent DC',
    MODE_MILLI_CURRENT_AC_DC: 'mCurrent AC + DC',
    MODE_CURRENT_AC: 'Current AC',
    MODE_CURRENT_DC: 'Current DC',
    MODE_CURRENT_AC_DC: 'Current AC + DC',
    MODE_CAPCITANCE: 'Capacitance',
    MODE_FREQUENCY: 'Frequency',
    MODE_DUTY_FACTOR: 'Duty Factor',
    MODE_TEMPERATURE_C: 'Temperature C',
    MODE_TEMPERATURE_F: 'Temperature F',
}

RANGES = {
    MODE_VOLTAGE_AC: {
        RANGE_0: '2 V',
        RANGE_1: '20 V',
        RANGE_2: '200 V',
        RANGE_3: '750 V',
    },
    MODE_VOLTAGE_DC: {
        RANGE_0: '2 V',
        RANGE_1: '20 V',
        RANGE_2: '200 V',
        RANGE_3: '1000 V',
    },
    MODE_VOLTAGE_AC_DC: {
        RANGE_0: '2 V',
        RANGE_1: '20 V',
        RANGE_2: '200 V',
        RANGE_3: '750 V',
    },
    MODE_MILLI_VOLTAGE_AC: {
        RANGE_0: '20 mV',
        RANGE_1: '200 mV',
    },
    MODE_MILLI_VOLTAGE_DC: {
        RANGE_0: '20 mV',
        RANGE_1: '200 mV',
    },
    MODE_MILLI_VOLTAGE_AC_DC: {
        RANGE_0: '20 mV',
        RANGE_1: '200 mV',
    },
    MODE_RESISTANCE: {
        RANGE_0: '200 Ohm',
        RANGE_1: '2 kOhm',
        RANGE_2: '20 kOhm',
        RANGE_3: '200 kOhm',
        RANGE_4: '2 MOhm',
        RANGE_5: '20 MOhm',
        RANGE_6: '200 MOhm',
        RANGE_7: '2 GOhm',
    },
    MODE_RESISTANCE_LV: {
        RANGE_0: '2 kOhm',
        RANGE_1: '20 kOhm',
        RANGE_2: '200 kOhm',
        RANGE_3: '2 MOhm',
        RANGE_4: '20 MOhm',
        RANGE_5: '200 MOhm',
        RANGE_6: '2 GOhm',
    },
    MODE_P_N_TEST: {
        RANGE_0: '2 V',
    },
    MODE_CONTINUITY_TEST: {
        RANGE_0: '200 Ohm',
    },
    MODE_MILLI_CURRENT_AC: {
        RANGE_0: '20 mA',
        RANGE_1: '200 mA',
    },
    MODE_MILLI_CURRENT_DC: {
        RANGE_0: '20 mA',
        RANGE_1: '200 mA',
    },
    MODE_MILLI_CURRENT_AC_DC: {
        RANGE_0: '20 mA',
        RANGE_1: '200 mA',
    },
    MODE_CURRENT_AC: {
        RANGE_0: '2 A',
        RANGE_1: '10 A',
    },
    MODE_CURRENT_DC: {
        RANGE_0: '2 A',
        RANGE_1: '10 A',
    },
    MODE_CURRENT_AC_DC: {
        RANGE_0: '2 A',
        RANGE_1: '10 A',
    },
    MODE_CAPCITANCE: {
        RANGE_0: '4 nF',
        RANGE_1: '40 nF',
        RANGE_2: '400 nF',
        RANGE_3: '4 µF',
        RANGE_4: '40 µF',
        RANGE_5: '400 µF',
        RANGE_6: '4 mF',
        RANGE_7: '40 mF',
    },
    MODE_FREQUENCY: {
        RANGE_0: '20 Hz',
        RANGE_1: '200 Hz',
        RANGE_2: '2 kHz',
        RANGE_3: '20 kHz',
        RANGE_4: '200 kHz',
        RANGE_5: '1 MHz',
    },
    MODE_TEMPERATURE_C: {
        RANGE_0: '400 °C',
        RANGE_1: '1200 °C',
    },
    MODE_TEMPERATURE_F: {
        RANGE_0: '400 °F',
        RANGE_1: '2192 °F',
    },
}

UNITS = {
    0: 'None',
    1: 'V',
    2: 'mV',
    3: 'A',
    4: 'mA',
    5: 'dB',
    6: 'dBm',
    7: 'nF',
    8: 'µF',
    9: 'mF',
    10: 'Ohm',
    11: 'KOhm',
    12: 'MOhm',
    13: 'GOhm',
    14: '%',
    15: 'Hz',
    16: 'KHz',
    17: 'MHz',
    18: '°C',
    19: '°F',
    20: 's',
    21: 'ms',
    22: 'ns',
}

VALUE_INFINITE = 'Infinite'


class MalformedDataFormat(Exception):
    def __init__(self, data):
        self.message = 'Received malformed data: \'{}\''.format(data)

    def __repr__(self):
        return 'MalformedDataFormat: {}'.format(self.message)


class Mode:
    def __init__(self, raw_code: str, name: str, ranges: dict):
        self.raw_code = raw_code
        self.name = name
        self.ranges = ranges

    def get_range(self, raw_range: str):
        return self.ranges.get(raw_range)

    def __repr__(self):
        return 'Mode: ' + self.name


class Range:
    def __init__(self, raw_code: str, name: str, auto: bool = True):
        self.raw_code = raw_code
        self.name = name
        self.max = name.split()[0]
        self.auto = auto

    def __repr__(self):
        return 'Range: ' + ('auto ' if self.auto else 'manual ') + self.name


class DataFormat:
    def __init__(self, data: bytes):
        self.raw = self.convert_to_escaped_hex_string(data)
        if len(data) < 19:
            raise MalformedDataFormat(data)
        self.mode = data[4:6].hex()
        self.range = data[7:8].hex()
        self.main_value = data[8:11]
        self.main_state = bin(int(data[11:12].hex(), 16))[2:].zfill(8)
        self.main_function = data[12:13].hex()
        self.sub_value = data[13:16]
        self.sub_state = bin(int(data[16:17].hex(), 16))[2:].zfill(8)
        self.sub_function = data[17:18].hex()
        self.checksum = data[-1:].hex()

    @staticmethod
    def convert_to_escaped_hex_string(data: bytes):
        h = data.hex()
        return ''.join('\\x{}'.format(h[i:i + 2]) for i in range(0, len(h) - 1, 2))


class DataParser:
    def __init__(self):
        self.dmm_modes = {}
        self._init_modes()

    def parse(self, data: bytes):
        try:
            raw = DataFormat(data)
            mode = self._parse_mode(raw)
            range = mode.get_range(raw.range)
            value = self._parse_value(raw.main_value, raw.main_state, range)
            unit = self._parse_unit(raw.main_state)
            sub_value = self._parse_value(raw.sub_value, raw.sub_state, None)
            sub_unit = self._parse_unit(raw.sub_state)
            return WindmmData(raw, mode, range, value, unit, sub_value, sub_unit)
        except MalformedDataFormat as e:
            print(e.message)
            return None

    def _parse_mode(self, raw: DataFormat):
        return self.dmm_modes[raw.mode] if raw.mode and raw.mode in self.dmm_modes else None

    @staticmethod
    def _parse_value(raw_value: bytes, raw_state: str, range: Range):
        base = raw_value[0] + raw_value[1] * 256 + struct.unpack('b', raw_value[2:])[0] * 65536
        result = str(base)
        point = int(raw_state[-3:], 2)
        if not base:
            return '0.0'
        if point:
            result = result.zfill(point + (1 if base > 0 else 2))
            result = result[:-point] + '.' + result[-point:]
        if range and result.split('.')[0] == range.max:
            result = VALUE_INFINITE
        return result

    @staticmethod
    def _parse_unit(raw_state):
        unit_code = int(raw_state[:-3], 2)
        return UNITS.get(unit_code)

    def _init_modes(self):
        for mode in MODES:
            ranges = self._get_ranges(mode)
            self.dmm_modes[mode] = Mode(mode, MODES[mode], ranges)

    @staticmethod
    def _get_ranges(mode):
        ranges = {}
        if mode in RANGES:
            for range_index in RANGES[mode]:
                range_auto_code = RANGE_AUTO + range_index
                ranges[range_auto_code] = Range(range_auto_code, RANGES[mode][range_index])
                range_manual_code = RANGE_MANUAL + range_index
                ranges[range_manual_code] = Range(range_manual_code, RANGES[mode][range_index], False)
        return ranges


class WindmmData:
    def __init__(self, raw: DataFormat, mode: Mode, range: Range, value: str, unit: str, sub_value: str = None, sub_unit: str = None):
        self.raw = raw
        self.mode = mode
        self.range = range
        self.value = value
        self.unit = unit
        self.sub_value = sub_value
        self.sub_unit = sub_unit

    def get_raw(self):
        return self.raw.raw

    def __repr__(self):
        return "[" \
               + self.mode.__str__() \
               + ", " + self.range.__repr__() \
               + ", value: " + self.value.__repr__() \
               + ", unit: " + self.unit.__repr__() \
               + ((", sub value: " + self.sub_value.__repr__()) if self.sub_value else '') \
               + ((", sub unit: " + self.sub_unit.__repr__()) if self.sub_unit else '') \
               + ']'
