# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from __future__ import absolute_import

import logging

from ModemManager.ModemManager import ModemManagerHelper

class SIM(ModemManagerHelper):
    def __init__(self, path):
        super(SIM, self).__init__(interface='org.freedesktop.ModemManager1.Sim', path=path)

    def SendPin(self, pin):
        self._dbus[self._interface].SendPin(pin)

    def SendPuk(self, puk, pin):
        self._dbus[self._interface].SendPuk(puk, pin)

    def EnablePin(self, pin, enabled):
        self._dbus[self._interface].EnablePin(pin, enabled)

    def ChangePin(self, old_pin, new_pin):
        self._dbus[self._interface].ChangePin(old_pin, new_pin)
