# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from __future__ import absolute_import

import logging
import types

from ModemManager.ModemManager import ModemManagerHelper
from ModemManager._enum import MMOmaSessionState, MMOmaSessionStateFailedReason


class Oma(ModemManagerHelper):
    def __init__(self, path):
        super(Oma, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Oma', path=path)
        self._session_state_changed = None

    @property
    def onSessionStateChanged(self):
        return self._session_state_changed

    @onSessionStateChanged.setter
    def onSessionStateChanged(self, callback):
        callback = types.MethodType(callback, self)
        self._session_state_changed = self._dbus[self._interface].SessionStateChanged.connect(callback)

    @onSessionStateChanged.deleter
    def onSessionStateChanged(self):
        if self._session_state_changed is not None:
            self._session_state_changed.disconnect()

        self._session_state_changed = None

    def connectSessionStateChanged(self, callback=None):
        if callback is not None:
            self.onSessionStateChanged = callback
            return self.onSessionStateChanged
        else:
            return self._dbus[self._interface].SessionStateChanged.connect(self._on_session_state_changed_cb)

    def _on_session_state_changed_cb(self, old_session_state, new_session_state, session_state_failed_reason):
        if session_state_failed_reason:
            logging.info('{}: {} to {} because {}'.format(self._path, MMOmaSessionState(old_session_state).name,
                                                          MMOmaSessionState(new_session_state).name,
                                                          MMOmaSessionStateFailedReason(session_state_failed_reason).name))
        else:
            logging.info('{}: {} to {}'.format(self._path, MMOmaSessionState(old).name, MMOmaSessionState(new).name))

    ### org.freedesktop.ModemManager1.Modem.Oma ###
    def Setup(self, features):
        self._dbus[self._interface].Setup(features)

    def StartClientInitiatedSession(self, session_type):
        self._dbus[self._interface].StartClientInitiatedSession(session_type)

    def AcceptNetworkInitiatedSession(self, session_id, accept):
        self._dbus[self._interface].AcceptNetworkInitiatedSession(session_id, accept)

    def CancelSession(self):
        self._dbus[self._interface].CancelSession()
