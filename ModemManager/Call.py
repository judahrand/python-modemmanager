# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging

from ModemManager.ModemManager import ModemManagerHelper


class Call(ModemManagerHelper):
    def __init__(self, path):
        super(Call, self).__init__(interface='org.freedesktop.ModemManager1.Call', path=path)

    def __getitem__(self, key):
        try:
            return self.Get(key)
        except KeyError:
            raise KeyError('{} does not have property named {}'.format(self._interface, key))

    def Start(self):
        self._dbus.Start()

    def Accept(self):
        self._dbus.Accept()

    def Hangup(self):
        self._dbus.Hangup()

    def SendDtmf(self, dtmf):
        self._dbus.SendDtmf(dtmf)
