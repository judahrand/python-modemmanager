# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging
import types

from ModemManager.ModemManager import ModemManagerHelper
from ModemManager.SMS import SMS


class Messaging(ModemManagerHelper):
    def __init__(self, path):
        super(Messaging, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Messaging', path=path)
        self._added = None
        self._deleted = None

    @property
    def onAdded(self):
        return self._state_changed

    @onAdded.setter
    def onAdded(self, callback):
        callback = types.MethodType(callback, self)
        self._state_changed = self._dbus[self._interface].Added.connect(callback)

    @onAdded.deleter
    def onAdded(self):
        if self._added is not None:
            self._added.disconnect()

        self._added = None

    def connectAdded(self, callback=None):
        if callback is not None:
            self.onAdded = callback
            return self.onAdded
        else:
            return self._dbus[self._interface].Added.connect(self._on_added_cb)

    def _on_added_cb(self, path, received):
        if received:
            logging.info('{}: {} received from network'.format(self._path, path))
        else:
            logging.info('{}: {} added locally'.format(self._path, path))

    @property
    def onDeleted(self):
        return self._deleted

    @onDeleted.setter
    def onDeleted(self, callback):
        callback = types.MethodType(callback, self)
        self._deleted = self._dbus[self._interface].Deleted.connect(callback)

    @onDeleted.deleter
    def onDeleted(self):
        if self._deleted is not None:
            self._deleted.disconnect()

        self._deleted = None

    def connectDeleted(self, callback=None):
        if callback is not None:
            self.onDeleted = callback
            return self.onDeleted
        else:
            return self._dbus[self._interface].Deleted.connect(self._on_deleted_cb)

    def _on_deleted_cb(self, path):
        logging.info('{}: {} deleted'.format(self._path, path))

    ### org.freedesktop.ModemManager1.Modem.Messaging ###
    def List(self):
        return self._dbus[self._interface].List()

    def Delete(self, path):
        self._dbus[self._interface].Delete(path)

    def Create(self, properties):
        return self._dbus[self._interface].Create(properties)

    ### get interface to Sms ###
    def GetSMS(self, path):
        return SMS(path)
