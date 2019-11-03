import serial
import re


class SerialWithErrorsProtection(object):

    regex = re.compile("^([-]?([0-9]+([.][0-9]+)) ){2}([-]?[0-9]+ )*[-]?[0-9]+$")

    def __init__(self, device_address, baudrate, timeout=.1):
        self.serial = serial.Serial(device_address, baudrate, timeout)

    def read_data(self):
        try:
            bytes = self.serial.inWaiting()
            data = self.serial.read(bytes).decode("utf-8")
            if self.validate_data(data):
                d1, d2, i_l = self.parse_data(data)
                Storage.set_data(d1, d2, i_l)
        except Exception as E:
            print(E)


    @classmethod
    def validate_data(cls, data):
        if re.match(cls.regex, data):
            return True
        return False

    @classmethod
    def parse_data(cls, data):
        numbers = data.split(" ")
        double1 = float(numbers[0])
        double2 = float(numbers[1])
        int_list = [int(num) for num in numbers[2:]]
        return double1, double2, int_list


class Storage(object):
    d1 = 0
    d2 = 0
    i_l = []

    @classmethod
    def set_data(cls, d1, d2, i_l):
        cls.d1 = d1
        cls.d2 = d2
        cls.i_l = i_l
