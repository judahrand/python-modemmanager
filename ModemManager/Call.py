# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from __future__ import absolute_import

import logging
import types

from ModemManager.ModemManager import ModemManagerHelper
from ModemManager._enums import MMCallState, MMCallStateReason


class Call(ModemManagerHelper):
    def __init__(self, path):
        super(Call, self).__init__(interface='org.freedesktop.ModemManager1.Call', path=path)
        self._dtmf_received = None
        self._state_changed = None

    @property
    def onDtmfReceived(self):
        return self._dtmf_received

    @onDtmfReceived.setter
    def onDtmfReceived(self, callback):
        callback = types.MethodType(callback, self)
        self._dtmf_received = self._dbus[self._interface].DtmfReceived.connect(callback)

    @onDtmfReceived.deleter
    def onDtmfReceived(self):
        if self._dtmf_received is not None:
            self._dtmf_received.disconnect()

        self._dtmf_received = None

    def connectDtmfReceived(self, callback=None):
        if callback is not None:
            self.onDtmfReceived = callback
            return self.onDtmfReceived
        else:
            return self._dbus[self._interface].DtmfReceived.connect(self._on_dtmf_received_cb)

    def _on_dtmf_received_cb(self, dtmf):
        logging.info('{}: {} received'.format(self._path, dtmf))

    @property
    def onStateChanged(self):
        return self._state_changed

    @onStateChanged.setter
    def onStateChanged(self, callback):
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
        logging.info('{}: {} to {} because {}'.format(self._path, MMCallState(old).name, MMCallState(new).name, MMCallStateReason(reason).name))

    def Start(self):
        self._dbus[self._interface].Start()

    def Accept(self):
        self._dbus[self._interface].Accept()

    def Hangup(self):
        self._dbus[self._interface].Hangup()

    def SendDtmf(self, dtmf):
        self._dbus[self._interface].SendDtmf(dtmf)
