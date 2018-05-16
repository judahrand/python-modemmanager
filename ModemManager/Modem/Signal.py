# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging

from ModemManager.ModemManager import ModemManagerHelper


class Signal(ModemManagerHelper):
    def __init__(self, path):
        super(Signal, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Signal', path=path)

    ### org.freedesktop.ModemManager1.Modem.Signal ###
    def Setup(self, rate):
        self._dbus[self._interface].Setup(rate)
