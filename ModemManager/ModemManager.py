# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManagerHelper import ModemManagerHelper
from ModemManager.Modem.Modem import Modem


class ModemManager(ModemManagerHelper):

    def __init__(self):
        super(ModemManager, self).__init__(interface='org.freedesktop.ModemManager1', path=None)

    def __getitem__(self, path):
        try:
            return Modem(path)
        except KeyError:
            raise KeyError('modem {} does not exist'.format(path))

    def __iter__(self):
            for key in self.ListModems():
                yield self[key]

    ### org.freedesktop.ModemManager1 ###
    def ScanDevices(self):
        try:
            self._dbus.ScanDevices()
        except Exception as e:
            raise e

    def SetLogging(self, level):
        if level in ('ERR', 'WARN', 'INFO', 'DEBUG'):
            try:
                self._dbus.SetLogging(level)
            except Exception as e:
                raise e
        else:
            raise ValueError('invalid logging level')

    def GetManagedObjects(self):
        try:
            return self._dbus.GetManagedObjects()
        except Exception as e:
            raise e

    def ListModems(self):
        return self.GetManagedObjects().keys()
