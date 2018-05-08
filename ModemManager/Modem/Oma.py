# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManager import ModemManagerHelper


class Oma(ModemManagerHelper):
    def __init__(self, path):
        super(Oma, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Oma', path=path)

    ### org.freedesktop.ModemManager1.Modem.Oma ###
    def Setup(self, features):
        self._dbus.Setup(features)

    def StartClientInitiatedSession(self, session_type):
        self._dbus.StartClientInitiatedSession(session_type)

    def AcceptNetworkInitiatedSession(self, session_id, accept):
        self._dbus.AcceptNetworkInitiatedSession(session_id, accept)

    def CancelSession(self):
        self._dbus.CancelSession()
