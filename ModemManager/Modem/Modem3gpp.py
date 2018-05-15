# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging

from ModemManager.ModemManager import ModemManagerHelper


class Modem3gpp(ModemManagerHelper):
    def __init__(self, path):
        super(Modem3gpp, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Modem3gpp', path=path)
        self.Ussd = Ussd(self._path)

    ### org.freedesktop.ModemManager1.Modem.Modem3gpp ###
    def Register(self, operator_id):
        self._dbus.Register(operator_id)

    def Scan(self):
        return self.Scan()


class Ussd(ModemManagerHelper):
    def __init__(self, path):
        super(Ussd, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd', path=path)

    ### org.freedesktop.ModemManager1.Modem.Modem3gpp.Ussd ###
    def Initiate(self, command):
        return self._dbus.Initiate(command)

    def Respond(self, response):
        return self._dbus.Respond(response)

    def Cancel(self):
        self._dbus.Cancel()
