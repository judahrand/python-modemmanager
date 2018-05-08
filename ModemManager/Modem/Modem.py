# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManager import ModemManagerHelper
from ModemManager.Modem.Simple import Simple
from ModemManager.Modem.Modem3gpp import Modem3gpp
from ModemManager.Modem.ModemCdma import ModemCdma
from ModemManager.Modem.Messaging import Messaging
from ModemManager.Modem.Location import Location
from ModemManager.Modem.Time import Time
from ModemManager.Modem.Voice import Voice
from ModemManager.Modem.Firmware import Firmware
from ModemManager.Modem.Signal import Signal
from ModemManager.Modem.Oma import Oma
from ModemManager.SIM import SIM
from ModemManager.Bearer import Bearer


class Modem(ModemManagerHelper):

    def __init__(self, path):
        super(Modem, self).__init__(interface='org.freedesktop.ModemManager1.Modem', path=path)
        self.Simple = Simple(self._path)
        self.Modem3gpp = Modem3gpp(self._path)
        self.ModemCdma = ModemCdma(self._path)
        self.Messaging = Messaging(self._path)
        self.Location = Location(self._path)
        self.Time = Time(self._path)
        self.Voice = Voice(self._path)
        self.Firmware = Firmware(self._path)
        self.Signal = Signal(self._path)
        self.Oma = Oma(self._path)

    def __getitem__(self, key):
        return self.Get(key)

    ### get custom objects ###
    def GetSim(self):
        return SIM(self.Get('Sim'))

    def GetBearer(self, path):
        return Bearer(path)

    ### org.freedesktop.ModemManager1.Modem ###
    def Enable(self, enabled):
        self._dbus.Enable(enabled)

    def ListBearers(self):
        return self._dbus.ListBearers()

    def CreateBearer(self, properties):
        return self._dbus.CreateBearer(properties)

    def DeleteBearer(self, bearer):
        self._dbus.DeleteBearer(bearer)

    def Reset(self):
        self._dbus.Reset()

    def FactoryReset(self, code):
        self._dbus.FactoryReset(code)

    def SetPowerState(self, state):
        self._dbus.SetPowerState(state)

    def SetCurrentCapabilities(self, capabilities):
        self._dbus.SetCurrentCapabilities(capabilities)

    def SetCurrentModes(self, modes):
        self._dbus.SetCurrentModes(modes)

    def SetCurrentBands(self, bands):
        self._dbus.SetCurrentBands(bands)

    def Command(self, cmd, timeout):
        return self._dbus.Command(cmd, timeout)
