import serial  # pylint: disable=import-error
import time
import logging

_LOGGER = logging.getLogger(__name__)


class Hex(object):

    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port,
                                 baudrate=115200,
                                 bytesize=8,
                                 parity='N',
                                 stopbits=1,
                                 timeout=2,
                                 writeTimeout=1)

    def check_serial(self):
        if self.ser.is_open:
            junk = []
            while self.ser.in_waiting:
                junk += self.ser.read(1)
            if len(junk) > 0:
                length = str(len(junk))
                _LOGGER.debug(self.port + ": Received " + length + " unexpected bytes: " +
                              Hex.format_bytelist_for_print(junk))
            else:
                _LOGGER.debug("check_serial, no unexpected junk")
            self.ser.flushInput()
            self.ser.flushOutput()
            return True
        return False

    @staticmethod
    def format_bytelist_for_print(command):
        formatted_string = ""
        for char in command:
            formatted_string += ' 0x{0:0{1}X}'.format(char, 2)
        return formatted_string

    @staticmethod
    def checksum_calculate(command):
        crc_sum = 0
        crc = None
        for i in command:
            crc_sum += i
            crc = (0x100 - crc_sum) & 0xFF
        return crc

    def write_command(self, command):
        if self.check_serial():
            command_string = command
            command_string.append(Hex.checksum_calculate(command))
            _LOGGER.debug("Writing" + Hex.format_bytelist_for_print(command_string))
            self.ser.write(command_string)
            time.sleep(.2)

    def get_serial_response(self):
        read = []
        while self.ser.in_waiting:
            read += self.ser.read(1)
        if len(read) > 0:
            length = str(len(read))
            _LOGGER.debug(self.port + ": Received " + length + " bytes")
            _LOGGER.debug(Hex.format_bytelist_for_print(read))

        else:
            _LOGGER.debug("get_serial_response, no data")
        if len(read) > 0:
            return read
        return False

    def reset(self):
        reset_command = [0xA5, 0x5B, 0x08, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.write_command(reset_command)
        time.sleep(.6)

    def set_port(self, port):
        port_list = {
            '1': [0xA5, 0x5B, 0x02, 0x03, 0x01, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00],
            '2': [0xA5, 0x5B, 0x02, 0x03, 0x02, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00]
        }
        if str(port) in port_list:
            self.write_command(port_list[str(port)])
            time.sleep(.1)

    def set_resolution(self, resolution):
        resolution_list = {
            '1080p':    [0xA5, 0x5B, 0x08, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '720p':     [0xA5, 0x5B, 0x08, 0x06, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '1080i':    [0xA5, 0x5B, 0x08, 0x06, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '1024x768': [0xA5, 0x5B, 0x08, 0x06, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
            '1360x768': [0xA5, 0x5B, 0x08, 0x06, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        }
        if resolution in resolution_list:
            self.write_command(resolution_list[resolution])
            time.sleep(.6)

    def set_mode(self, mode):
        mode_list = {
            'single':     [0xA5, 0x5B, 0x19, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            'pip':        [0xA5, 0x5B, 0x19, 0x01, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            'side_full':  [0xA5, 0x5B, 0x19, 0x01, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            'side_scale': [0xA5, 0x5B, 0x19, 0x01, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00]
        }
        if mode in mode_list:
            self.write_command(mode_list[mode])
            time.sleep(.6)

    def set_pip_position(self, pip_position):
        pip_position_list = {
            'top_left':     [0xA5, 0x5B, 0x19, 0x03, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            'top_right':    [0xA5, 0x5B, 0x19, 0x03, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            'bottom_left':  [0xA5, 0x5B, 0x19, 0x03, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            'bottom_right': [0xA5, 0x5B, 0x19, 0x03, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00]
        }
        if pip_position in pip_position_list:
            self.write_command(pip_position_list[pip_position])

    def set_pip_size(self, pip_size):
        pip_size_list = {
            'small':  [0xA5, 0x5B, 0x19, 0x05, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            'medium': [0xA5, 0x5B, 0x19, 0x05, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00],
            'large':  [0xA5, 0x5B, 0x19, 0x05, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00]
        }
        if pip_size in pip_size_list:
            self.write_command(pip_size_list[pip_size])

    def set_pip_border(self, pip_border):
        pip_border_list = {
            'show': [0xA5, 0x5B, 0x0C, 0x01, 0x0F, 0x00, 0x0F, 0x00, 0x00, 0x00, 0x00, 0x00],
            'hide': [0xA5, 0x5B, 0x0C, 0x01, 0xF0, 0x00, 0xF0, 0x00, 0x00, 0x00, 0x00, 0x00]
        }
        if pip_border in pip_border_list:
            self.write_command(pip_border_list[pip_border])

    def get_port(self):
        query = [0xA5, 0x5B, 0x02, 0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.write_command(query)
        response = self.get_serial_response()
        return str(response[6])

    def get_resolution(self):
        query = [0xA5, 0x5B, 0x09, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.write_command(query)
        response = self.get_serial_response()
        resolution = ['1080p', '720p', '1080i', '1024x768', '1360x768']
        if response:
            return resolution[response[4]]
        else:
            return False

    def get_mode(self):
        query = [0xA5, 0x5B, 0x19, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.write_command(query)
        response = self.get_serial_response()
        mode_list = [None, 'single', 'pip', 'side_full', 'side_scale']
        if response:
            return mode_list[response[4]]
        else:
            return False

    def get_pip_position(self):
        query = [0xA5, 0x5B, 0x19, 0x04, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.write_command(query)
        response = self.get_serial_response()
        pip_position_list = [None, 'top_left', 'top_right', 'bottom_left', 'bottom_right']
        if response:
            return pip_position_list[response[4]]
        else:
            return False

    def get_pip_size(self):
        query = [0xA5, 0x5B, 0x19, 0x06, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.write_command(query)
        response = self.get_serial_response()
        pip_size_list = [None, 'small', 'medium', 'large']
        if response:
            return pip_size_list[response[4]]
        else:
            return False

    def get_pip_border(self):
        query = [0xA5, 0x5B, 0x0C, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        self.write_command(query)
        response = self.get_serial_response()
        # pip_size_list = [None, 'small', 'medium', 'large']
        if response:
            if response[4] == 0xF0:
                return 'hide'
            elif response[4] == 0x0F:
                return 'show'
            else:
                return False
        else:
            return False
