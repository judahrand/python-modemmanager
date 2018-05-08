# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManagerHelper import ModemManagerHelper
from ModemManager.ModemManagerError import ModemManagerError
from ModemManager.Modem.Modem import Modem


class ModemManager(ModemManagerHelper):

    def __init__(self):
        super(ModemManager, self).__init__(interface='org.freedesktop.ModemManager1', path=None)

    def __getitem__(self, path):
        try:
            return Modem(path)
        except KeyError:
            raise ModemManagerError('modem {} does not exist'.format(path))

    def __iter__(self):
            for key in self.ListModems():
                yield self[key]

    ### org.freedesktop.ModemManager1 ###
    def ScanDevices(self):
        try:
            self._dbus.ScanDevices()
        except Exception:
            raise ModemManagerError('failed to scan devices')

    def SetLogging(self, level):
        if level in ('ERR', 'WARN', 'INFO', 'DEBUG'):
            try:
                self._dbus.SetLogging(level)
            except Exception:
                ModemManagerError('failed to set logging')
        else:
            raise ModemManagerError('invalid logging level')

    def GetManagedObjects(self):
        try:
            return self._dbus.GetManagedObjects()
        except Exception:
            raise ModemManagerError('failed to get managed objects')

    def ListModems(self):
        return self.GetManagedObjects().keys()
