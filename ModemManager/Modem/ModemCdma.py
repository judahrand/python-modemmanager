# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging
import types

from ModemManager.ModemManager import ModemManagerHelper
from ModemManager._enums import MMModemCdmaActivationState
from ModemManager._errors import MMCdmaActivationError


class ModemCdma(ModemManagerHelper):
    def __init__(self, path):
        super(ModemCdma, self).__init__(interface='org.freedesktop.ModemManager1.Modem.ModemCdma', path=path)
        self._activation_state_changed = None

    @property
    def onActivationStateChanged(self):
        return self._activation_state_changed

    @onActivationStateChanged.setter
    def onActivationStateChanged(self, callback):
        callback = types.MethodType(callback, self)
        self._activation_state_changed = self._dbus[self._interface].ActivationStateChanged.connect(callback)

    @onActivationStateChanged.deleter
    def onActivationStateChanged(self):
        if self._activation_state_changed is not None:
            self._activation_state_changed.disconnect()

        self._activation_state_changed = None

    def connectStateChanged(self, callback=None):
        if callback is not None:
            self.onActivationStateChanged = callback
            return self.onActivationStateChanged
        else:
            return self._dbus[self._interface].ActivationStateChanged.connect(self._on_activation_state_changed_cb)

    def _on_activation_state_changed_cb(self, activation_state, activation_error, status_changes):
        logging.info('{}: {} because {}'.format(self._path, MMModemCdmaActivationState(activation_state).name, MMCdmaActivationError(activation_error).name))

    ### org.freedesktop.ModemManager1.Modem.ModemCdma ###
    def Activate(self, carrier_code):
        self._dbus[self._interface].Activate(carrier_code)

    def ActivateManual(self, properties):
        self._dbus[self._interface].Activate(properties)
