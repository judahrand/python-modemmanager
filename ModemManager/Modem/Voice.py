# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManager import ModemManagerHelper
from ModemManager.Call import Call


class Voice(ModemManagerHelper):
    def __init__(self, path):
        super(Voice, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Voice', path=path)

    ### org.freedesktop.ModemManager1.Modem.Voice ###
    def ListCalls(self):
        return self._dbus.ListCalls()

    def DeleteCall(self, path):
        self._dbus.DeleteCall(path)

    def CreateCall(self, properties):
        return self._dbus.CreateCall(properties)

    ### get interface to Call ###
    def GetCall(self, path):
        return Call(path)
