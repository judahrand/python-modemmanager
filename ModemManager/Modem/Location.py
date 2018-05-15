# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging

from ModemManager.ModemManager import ModemManagerHelper


class Location(ModemManagerHelper):
    def __init__(self, path):
        super(Location, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Location', path=path)

    ### org.freedesktop.ModemManager1.Modem.Location ###
    def SetupLocation(self, sources, signal_location):
        self._dbus.Setup(sources, signal_location)

    def GetLocation(self):
        return self._dbus.GetLocation()

    def SetSuplServer(self, supl):
        self._dbus.SetSuplServer(supl)

    def SetGpsRefreshRate(self, rate):
        self._dbus.SetGpsRefreshRate(rate)
