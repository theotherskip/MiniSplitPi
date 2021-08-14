import logging

log = logging.getLogger(__name__)


class LookupDict(dict):
    def __init__(self, d, name="unknown"):
        super(self.__class__, self).__init__(d)
        self.name = name

    def lookup(self, value):
        try:
            ret = [k for k, v in self.items() if v == value][0]
        except Exception:
            ret = None
            log.error("Failed to lookup %s from %s" % (value, self.name))
        return ret


POWER = LookupDict({"OFF": 0x00, "ON": 0x01}, "POWER")

TEMP = LookupDict(
    {
        # Celcius
        # 31: 0x00,
        # 30: 0x01,
        # 29: 0x02,
        # 28: 0x03,
        # 27: 0x04,
        # 26: 0x05,
        # 25: 0x06,
        # 24: 0x07,
        # 23: 0x08,
        # 22: 0x09,
        # 21: 0x0A,
        # 20: 0x0B,
        # 19: 0x0C,
        # 18: 0x0D,
        # 17: 0x0E,
        # 16: 0x0F,
        # 16.5: 0x1F,
        # 17.5: 0x1E,
        # 18.5: 0x1D,
        # 19.5: 0x1C,
        # 20.5: 0x1B,
        # 21.5: 0x1A,
        # 22.5: 0x19,
        # 23.5: 0x18,
        # 24.5: 0x17,
        # 25.5: 0x16,
        # 26.5: 0x15,
        # 27.5: 0x14,
        # 28.5: 0x13,
        # 29.5: 0x12,
        # 30.5: 0x11,
        # 31.5: 0x10,
        # Fahrenheit
        89: 0x00,
        87: 0x01,
        85: 0x02,
        83: 0x03,
        81: 0x04,
        79: 0x05,
        77: 0x06,
        75: 0x07,
        73: 0x08,
        71: 0x09,
        69: 0x0A,
        67: 0x0B,
        65: 0x0C,
        63: 0x0D,
        61: 0x0E,
        59: 0x0F,
        60: 0x1F,
        62: 0x1E,
        64: 0x1D,
        66: 0x1C,
        68: 0x1B,
        70: 0x1A,
        72: 0x19,
        74: 0x18,
        76: 0x17,
        78: 0x16,
        80: 0x15,
        82: 0x14,
        84: 0x13,
        86: 0x12,
        88: 0x11,
        90: 0x10,
    },
    "TEMP",
)

ROOM_TEMP = LookupDict(
    {
        # Celcius
        # 10: 0x00,
        # 11: 0x01,
        # 12: 0x02,
        # 13: 0x03,
        # 14: 0x04,
        # 15: 0x05,
        # 16: 0x06,
        # 17: 0x07,
        # 18: 0x08,
        # 19: 0x09,
        # 20: 0x0A,
        # 21: 0x0B,
        # 22: 0x0C,
        # 23: 0x0D,
        # 24: 0x0E,
        # 25: 0x0F,
        # 26: 0x10,
        # 27: 0x11,
        # 28: 0x12,
        # 29: 0x13,
        # 30: 0x14,
        # 31: 0x15,
        # 32: 0x16,
        # 33: 0x17,
        # 34: 0x18,
        # 35: 0x19,
        # 36: 0x1A,
        # 37: 0x1B,
        # 38: 0x1C,
        # 39: 0x1D,
        # 40: 0x1E,
        # 41: 0x1F,
        # Fahrenheit
        50: 0x00,
        52: 0x01,
        54: 0x02,
        55: 0x03,
        57: 0x04,
        59: 0x05,
        61: 0x06,
        63: 0x07,
        64: 0x08,
        66: 0x09,
        68: 0x0A,
        70: 0x0B,
        72: 0x0C,
        73: 0x0D,
        75: 0x0E,
        77: 0x0F,
        79: 0x10,
        81: 0x11,
        82: 0x12,
        84: 0x13,
        86: 0x14,
        88: 0x15,
        90: 0x16,
        91: 0x17,
        93: 0x18,
        95: 0x19,
        97: 0x1A,
        99: 0x1B,
        100: 0x1C,
        102: 0x1D,
        104: 0x1E,
        106: 0x1F,
    },
    "ROOM_TEMP",
)

MODE = LookupDict(
    {"HEAT": 0x01, "DRY": 0x02, "COOL": 0x03, "FAN": 0x07, "AUTO": 0x08}, "MODE"
)

VANE = LookupDict(
    {
        "AUTO": 0x00,
        "1": 0x01,
        "2": 0x02,
        "3": 0x03,
        "4": 0x04,
        "5": 0x05,
        "SWING": 0x07,
    },
    "VANE",
)

DIR = LookupDict(
    {
        "NA": 0x00,
        "<<": 0x01,
        "<": 0x02,
        "|": 0x03,
        ">": 0x04,
        ">>": 0x05,
        "<>": 0x08,
        "SWING": 0x0C,
    },
    "DIR",
)

FAN = LookupDict(
    {"AUTO": 0x00, "QUIET": 0x01, "1": 0x02, "2": 0x03, "3": 0x05, "4": 0x06}, "FAN"
)

CONTROL_PACKET_VALUES = LookupDict(
    {"POWER": 0x01, "MODE": 0x02, "TEMP": 0x04, "FAN": 0x08, "VANE": 0x10, "DIR": 0x80},
    "CONTROL_PACKET_VALUES",
)

CONTROL_PACKET_POSITIONS = LookupDict(
    {"POWER": 3, "MODE": 4, "TEMP": 5, "FAN": 6, "VANE": 7, "DIR": 10},
    "CONTROL_PACKET_POSITIONS",
)
