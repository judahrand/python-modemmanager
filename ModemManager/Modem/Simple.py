# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from __future__ import absolute_import

import logging

from ModemManager.ModemManager import ModemManagerHelper


class Simple(ModemManagerHelper):
    def __init__(self, path):
        super(Simple, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Simple', path=path)

    ### org.freedesktop.ModemManager1.Modem.Simple ###
    def Connect(self, properties):
        return self._dbus[self._interface].Connect(properties)

    def Disconnect(self, bearer):
        self._dbus[self._interface].Disconnect(bearer)

    def GetStatus(self):
        return self._dbus[self._interface].GetStatus()
