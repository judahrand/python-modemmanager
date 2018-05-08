# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManager import ModemManagerHelper
from datetime import time


class Time(ModemManagerHelper):
    def __init__(self, path):
        super(Time, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Time', path=path)

    ### org.freedesktop.ModemManager1.Modem.Time ###
    def GetNetworkTime(self):
        return time(self._dbus.GetNetworkTime())
