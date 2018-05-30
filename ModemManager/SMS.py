# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from __future__ import absolute_import

import logging

from ModemManager.ModemManager import ModemManagerHelper


class SMS(ModemManagerHelper):
    def __init__(self, path):
        super(SMS, self).__init__(interface='org.freedesktop.ModemManager1.Sms', path=path)

    def Send(self):
        self._dbus[self._interface].Send()

    def Store(self, storage):
        self._dbus[self._interface].Store(storage)
