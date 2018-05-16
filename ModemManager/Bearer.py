# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging

from ModemManager.ModemManager import ModemManagerHelper


class Bearer(ModemManagerHelper):
    def __init__(self, path):
        super(Bearer, self).__init__(interface='org.freedesktop.ModemManager1.Bearer', path=path)

    def __getitem__(self, key):
        try:
            return self._bearer[key]
        except KeyError:
            raise KeyError('bearer does not have property named {}'.format(key))

    def Connect(self):
        try:
            self._dbus[self._interface].Connect()
        except Exception as e:
            raise e

    def Disconnect(self):
        try:
            self._dbus[self._interface].Disconnect()
        except Exception as e:
            raise e
