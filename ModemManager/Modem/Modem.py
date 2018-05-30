# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from __future__ import absolute_import

import logging
import types

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
from ModemManager._enums import MMModemState, MMModemStateChangeReason


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

        self._state_changed = None

    @property
    def onStateChanged(self):
        return self._state_changed

    @onStateChanged.setter
    def onStateChanged(self, callback):
        if self._state_changed is not None:
            self._state_changed.disconnect()
            del(self._state_changed)

        callback = types.MethodType(callback, self)
        self._state_changed = self._dbus[self._interface].StateChanged.connect(callback)

    @onStateChanged.deleter
    def onStateChanged(self):
        if self._state_changed is not None:
            self._state_changed.disconnect()

        self._state_changed = None

    def connectStateChanged(self, callback=None):
        if callback is not None:
            self.onStateChanged = callback
            return self.onStateChanged
        else:
            return self._dbus[self._interface].StateChanged.connect(self._on_state_changed_cb)

    def _on_state_changed_cb(self, old, new, reason):
        logging.info('{}: {} to {} because {}'.format(self._path, MMModemState(old).name, MMModemState(new).name, MMModemStateChangeReason(reason).name))

    ### get custom objects ###
    @property
    def Sim(self):
        path = self.Get('Sim')
        if path != "/":
            return SIM(self.Get('Sim'))
        else:
            return None

    @Sim.setter
    def Sim(self):
        return

    @Sim.deleter
    def Sim(self):
        return

    def GetBearer(self, path):
        return Bearer(path)

    ### org.freedesktop.ModemManager1.Modem ###
    def Enable(self, enabled):
        self._dbus[self._interface].Enable(enabled)

    def ListBearers(self):
        return self._dbus[self._interface].ListBearers()

    def CreateBearer(self, properties):
        return self._dbus[self._interface].CreateBearer(properties)

    def DeleteBearer(self, bearer):
        self._dbus[self._interface].DeleteBearer(bearer)

    def Reset(self):
        self._dbus[self._interface].Reset()

    def FactoryReset(self, code):
        self._dbus[self._interface].FactoryReset(code)

    def SetPowerState(self, state):
        self._dbus[self._interface].SetPowerState(state)

    def SetCurrentCapabilities(self, capabilities):
        self._dbus[self._interface].SetCurrentCapabilities(capabilities)

    def SetCurrentModes(self, modes):
        self._dbus[self._interface].SetCurrentModes(modes)

    def SetCurrentBands(self, bands):
        self._dbus[self._interface].SetCurrentBands(bands)

    def Command(self, cmd, timeout):
        return self._dbus[self._interface].Command(cmd, timeout)
