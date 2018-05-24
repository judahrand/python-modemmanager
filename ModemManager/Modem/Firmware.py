# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from __future__ import absolute_import

import logging

from ModemManager.ModemManager import ModemManagerHelper


class Firmware(ModemManagerHelper):
    def __init__(self, path):
        super(Firmware, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Firmware', path=path)

    ### org.freedesktop.ModemManager1.Modem.Firmware ###
    def List(self):
        return self._dbus[self._interface].List()

    def Select(self, uniqueid):
        self._dbus[self._interface].Select(uniqueid)
