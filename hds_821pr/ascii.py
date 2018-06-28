import serial  # pylint: disable=import-error
import time
import logging

_LOGGER = logging.getLogger(__name__)


class Ascii(object):

    def __init__(self, port):
        self.port = port
        self.ser = serial.Serial(port,
                                 baudrate=115200,
                                 bytesize=8,
                                 parity='N',
                                 stopbits=1,
                                 timeout=2,
                                 writeTimeout=1)

        self.status = {
            'inputs': {
                'active': 1,
                1: {'signal': False, 'format': 0, 'RxON': 0},
                2: {'signal': False, 'format': 0, 'RxON': 0}
               },
            'mode': 'QUAD',
            'output_resolution': '1080P/60',
            'power_on': False,
            'pip_position': 'unknown',
            'pip_size': 'unknown',
            'pip_border': 'unknown'
        }

    def check_serial(self):
        if self.ser.is_open:
            self.get_serial_response()
            self.ser.flushInput()
            self.ser.flushOutput()
            return True
        return False

    def send_command(self, command_string):
        if self.check_serial():
            _LOGGER.debug("serial OK")
        else:
            _LOGGER.debug("serial BAD")

            _LOGGER.debug(self.port + ": writing " + str(len(command_string)) + " bytes: " +
                          str(command_string))

        final_command = ''.join([command_string, '!']).encode('utf-8')
        self.ser.write(final_command)
        time.sleep(.1)
        return self.get_serial_response()

    def get_serial_response(self):
        read = []
        while self.ser.in_waiting:
            read += self.ser.read(1)
        if len(read) > 0:
            length = str(len(read))
            _LOGGER.debug(self.port + ": Received " + length + " bytes")
            status_lines = bytearray(read).decode('utf-8').splitlines()
            for line in status_lines:
                _LOGGER.debug(line)
                self.update_status(line)

        else:
            _LOGGER.debug("get_serial_response", "no data")
        if len(read) > 0:
            return True
        return False

    def reboot(self):
        self.send_command("POWEROFF")
        time.sleep(3)
        self.send_command("POWERON")

    def reset(self):
        self.send_command("RESET")

    def set_port(self, input_device):
        self.send_command('IN' + str(input_device))

    def set_resolution(self, resolution):
        resolution_list = {
            '1080p':    "T1",
            '720p':     "T2",
            '1080i':    "T3",
            '1024x768': "T4",
            '1360x768': "T5"
        }
        if resolution in resolution_list:
            self.send_command(resolution_list[resolution])

    def set_mode(self, mode):
        mode_list = {
            'single':     "ONEINPUT",
            'pip':        "PIP",
            'side_full':  "SIDEBYSIDE1",
            'side_scale': "SIDEBYSIDE2"
        }
        if mode in mode_list:
            self.send_command(mode_list[mode])

    def set_pip_position(self, pip_position):
        return False

    def set_pip_size(self, pip_size):
        return False

    def set_pip_border(self, pip_border):
        return False

    def get_status(self):
        return self.status

    def get_port(self):
        return str(self.status['inputs']['active'])

    def get_mode(self):
        if self.status['mode'] == 'QUAD':
            return 'single'
        elif self.status['mode'] == 'PIP':
            return 'pip'
        elif self.status['mode'] == 'POP1':
            return 'side_full'
        elif self.status['mode'] == 'POP2':
            return 'side_scale'

    def get_resolution(self):
        # Internal: 1080P/60  720P/60  1080P/60  1024x768/60  1360x768/60
        # Returns:  1080p     720p     1080i     1024x768     1360x768
        return str(self.status['inputs']['output_resolution'])[:-3].lower()

    def get_pip_position(self):
        return str(self.status['inputs']['pip_position'])

    def get_pip_size(self):
        return str(self.status['inputs']['pip_size'])

    def get_pip_border(self):
        return str(self.status['inputs']['pip_border'])

    @staticmethod
    def invert_input_device(input_device):
        if input_device == 1:
            return 2
        if input_device == 2:
            return 1
        return False

    def update_status(self, line):
        # interprets whatever crud is in the serial buffer
        # hopefully it's usable to update status
        if line.startswith('PowerOFF'):
            _LOGGER.debug('setting power_on: _' + 'False' + '_')
            self.status['power_on'] = False
            return True

        if line.startswith('PowerON'):
            _LOGGER.debug('setting power_on: _' + 'True' + '_')
            self.status['power_on'] = True
            return True

        if line.startswith('Mode :'):
            _LOGGER.debug('setting mode: _' + str(line[6:]) + '_')
            print('setting mode: _' + str(line[6:]) + '_')
            self.status['mode'] = line[6:]
            return True

        if line.startswith('Select '):
            _LOGGER.debug('setting input active: _' + str(int(line[7:])) + '_')
            self.status['inputs']['active'] = int(line[7:])
            return True

        if line.startswith('Resolution : '):
            _LOGGER.debug('setting output_resolution: _' + str(line[13:]) + '_')
            self.status['output_resolution'] = line[13:]
            return True

        if line.startswith('num'):
            if line.startswith('IN', 7, 9):
                input_device = Ascii.invert_input_device(int(line[4:5]))
                _LOGGER.debug('setting input ' + str(input_device) + ' signal _True_')
                self.status['inputs'][input_device]['signal'] = True
                return True
            else:
                input_device = Ascii.invert_input_device(int(line[4:5]))
                _LOGGER.debug('setting input ' + str(input_device) + ' signal _False_')
                self.status['inputs'][input_device]['signal'] = False
                return True

        if line.startswith('Rx'):
            if line.startswith('format', 5, 11):
                input_device = Ascii.invert_input_device(int(line[3:4]))
                _LOGGER.debug('setting input ' + str(input_device) + ' format _' + str(line[14:]) + '_')
                self.status['inputs'][input_device]['format'] = int(line[14:])
                return True

            else:
                input_device = Ascii.invert_input_device(int(line[3:4]))
                _LOGGER.debug('setting input ' + str(input_device) + ' RxON _' + str(line[12:]) + '_')
                self.status['inputs'][input_device]['RxON'] = int(line[12:])
                return True

        if line.startswith('Factory init'):
            _LOGGER.debug('resetting status to defaults')
            self.status = {
                'inputs': {
                    'active': 1,
                    1: {'signal': False, 'format': 0, 'RxON': 0},
                    2: {'signal': False, 'format': 0, 'RxON': 0}
                   },
                'mode': 'QUAD',
                'output_resolution': '1080P/60',
                'power_on': False
            }
            return True

        # didn't update anything
        return False
