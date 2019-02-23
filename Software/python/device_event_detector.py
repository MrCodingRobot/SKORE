# General Utility
import time
import sys

# PYQT5, GUI Library
from PyQt5 import QtCore, QtGui, QtWidgets

# Serial and MIDI
from serial.tools import list_ports
import rtmidi

# SKORE modules
import globals

#-------------------------------------------------------------------------------
# Functions

class DeviceDetector(QtCore.QThread):

    arduino_change_signal = QtCore.pyqtSignal('QString')

    piano_change_signal = QtCore.pyqtSignal('QString')

    def __init__(self, gui = None):

        QtCore.QThread.__init__(self)
        self.gui = gui

        return None

    def enumerate_serial_devices(self):

        ports = list(list_ports.comports())

        return ports

    def enumerate_midi_devices(self):

        ports = self.midiout.get_ports()

        return ports

    def check_device_changes(self):

        #---------------------------------------------------------------------------
        # USB ports
        current_serial_devices = self.enumerate_serial_devices()

        for device in self.old_serial_devices:
            if device not in current_serial_devices:
                print("Removed USB port: ", device)
                self.removed_serial_devices.append(device)

                self.arduino_change_signal.emit('OFF')

        for device in current_serial_devices:
            if device not in self.old_serial_devices:
                print("Added USB port: ", device)
                self.added_serial_devices.append(device)

                self.arduino_change_signal.emit('ON')

        self.old_serial_devices = current_serial_devices

        #---------------------------------------------------------------------------
        # MIDI port detection
        current_midi_devices = self.enumerate_midi_devices()

        for device in self.old_midi_devices:
            if device not in current_midi_devices:
                print("Removed MIDI port: ", device)
                self.removed_midi_devices.append(device)

                self.piano_change_signal.emit('OFF')

        for device in current_midi_devices:
            if device not in self.old_midi_devices:
                print("Added MIDI port: ", device)
                self.added_midi_devices.append(device)

                self.piano_change_signal.emit('ON')

        self.old_midi_devices = current_midi_devices

    def run(self):

        print("DEVICE EVENT DETECTOR ENABLED")

        self.old_serial_devices = self.enumerate_serial_devices()
        self.added_serial_devices = []
        self.removed_serial_devices = []

        self.midiout = rtmidi.MidiOut()
        self.old_midi_devices = self.enumerate_midi_devices()
        self.added_midi_devices = []
        self.removed_midi_devices = []

        while True:
            self.check_device_changes()
            time.sleep(0.5)

#-------------------------------------------------------------------------------
# Main Code

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    detector = DeviceDetector()
    detector.start()
    sys.exit(app.exec_())