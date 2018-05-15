# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging

from ModemManager.ModemManager import ModemManagerHelper

class SIM(ModemManagerHelper):
    def __init__(self, path):
        super(SIM, self).__init__(interface='org.freedesktop.ModemManager1.Sim', path=path)

    def __getitem__(self, key):
        try:
            return self.Get(key)
        except KeyError:
            raise KeyError('{} does not have property named {}'.format(self._interface, key))

    def SendPin(self, pin):
        self._dbus.SendPin(pin)

    def SendPuk(self, puk, pin):
        self._dbus.SendPuk(puk, pin)

    def EnablePin(self, pin, enabled):
        self._dbus.EnablePin(pin, enabled)

    def ChangePin(self, old_pin, new_pin):
        self._dbus.ChangePin(old_pin, new_pin)
