# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging

from ModemManager.ModemManager import ModemManagerHelper
from ModemManager.SMS import SMS


class Messaging(ModemManagerHelper):
    def __init__(self, path):
        super(Messaging, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Messaging', path=path)

    ### org.freedesktop.ModemManager1.Modem.Messaging ###
    def List(self):
        return self._dbus.List()

    def Delete(self, path):
        self._dbus.Delete(path)

    def Create(self, properties):
        return self._dbus.Create(properties)

    ### get interface to Sms ###
    def GetSMS(self, path):
        return SMS(path)
