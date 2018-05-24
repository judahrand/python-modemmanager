# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from __future__ import absolute_import

import logging
import types

from ModemManager.ModemManager import ModemManagerHelper
from ModemManager.Call import Call


class Voice(ModemManagerHelper):
    def __init__(self, path):
        super(Voice, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Voice', path=path)
        self._call_added = None
        self._call_deleted = None

    @property
    def onCallAdded(self):
        return self._call_added

    @onCallAdded.setter
    def onCallAdded(self, callback):
        callback = types.MethodType(callback, self)
        self._call_added = self._dbus[self._interface].CallAdded.connect(callback)

    @onCallAdded.deleter
    def onCallAdded(self):
        if self._call_added is not None:
            self._call_added.disconnect()

        self._call_added = None

    def connectCallAdded(self, callback=None):
        if callback is not None:
            self.onCallAdded = callback
            return self.onCallAdded
        else:
            return self._dbus[self._interface].CallAdded.connect(self._on_call_added_cb)

    def _on_call_added_cb(self, path):
        logging.info('{}: {} added'.format(self._path, path))

    @property
    def onCallDeleted(self):
        return self._call_deleted

    @onCallDeleted.setter
    def onCallDeleted(self, callback):
        callback = types.MethodType(callback, self)
        self._call_deleted = self._dbus[self._interface].CallDeleted.connect(callback)

    @onCallDeleted.deleter
    def onCallDeleted(self):
        if self._call_deleted is not None:
            self._call_deleted.disconnect()

        self._call_deleted = None

    def connectCallDeleted(self, callback=None):
        if callback is not None:
            self.onCallDeleted = callback
            return self.onCallDeleted
        else:
            return self._dbus[self._interface].CallDeleted.connect(self._on_call_deleted_cb)

    def _on_call_deleted_cb(self, path):
        logging.info('{}: {} deleted'.format(self._path, path))

    ### org.freedesktop.ModemManager1.Modem.Voice ###
    def ListCalls(self):
        return self._dbus[self._interface].ListCalls()

    def DeleteCall(self, path):
        self._dbus[self._interface].DeleteCall(path)

    def CreateCall(self, properties):
        return self._dbus[self._interface].CreateCall(properties)

    ### get interface to Call ###
    def GetCall(self, path):
        return Call(path)
