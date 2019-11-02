import serial


class SerialPortFacade(object):

    def __init__(self, device_address, baudrate, timeout=.1):
        # self.serial = serial.Serial(device_address, baudrate, timeout)
        pass

    def send_data(self, data):
        data= str(data) + "\r\n"
        print(data)
        # self.serial.write(data.encode())
