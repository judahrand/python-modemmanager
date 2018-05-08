# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManager import ModemManagerHelper


class Firmware(ModemManagerHelper):
    def __init__(self, path):
        super(Firmware, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Firmware', path=path)

    ### org.freedesktop.ModemManager1.Modem.Firmware ###
    def List(self):
        return self._dbus.List()

    def Select(self, uniqueid):
        self._dbus.Select(uniqueid)
