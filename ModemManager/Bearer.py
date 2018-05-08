# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManager import ModemManagerHelper, ModemManagerError


class Bearer(ModemManagerHelper):
    def __init__(self, path):
        super(Bearer, self).__init__(interface='org.freedesktop.ModemManager1.Bearer', path=path)

    def __getitem__(self, key):
        try:
            return self._bearer[key]
        except KeyError:
            raise ModemManagerError('bearer does not have property named {}'.format(key))

    def Connect(self):
        try:
            self._dbus.Connect()
        except Exception as e:
            raise e

    def Disconnect(self):
        try:
            self._dbus.Disconnect()
        except Exception as e:
            raise e
