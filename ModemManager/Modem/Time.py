# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


import logging
import types

from ModemManager.ModemManager import ModemManagerHelper
from datetime import time


class Time(ModemManagerHelper):
    def __init__(self, path):
        super(Time, self).__init__(interface='org.freedesktop.ModemManager1.Modem.Time', path=path)
        self._network_time_changed = None

    @property
    def onNetworkTimeChanged(self):
        return self._network_time_changed

    @onNetworkTimeChanged.setter
    def onNetworkTimeChanged(self, callback):
        callback = types.MethodType(callback, self)
        self._network_time_changed = self._dbus[self._interface].NetworkTimeChanged.connect(self._on_network_time_changed_cb)

    @onNetworkTimeChanged.deleter
    def onNetworkTimeChanged(self):
        if self._network_time_changed is not None:
            self._network_time_changed.disconnect()

        self._network_time_changed = None

    def connectNetworkTimeChanged(self, callback=None):
        if callback is not None:
            self.onNetworkTimeChanged = callback
            return self.onNetworkTimeChanged
        else:
            return self._dbus[self._interface].NetworkTimeChanged.connect(callback)

    def _on_network_time_changed_cb(self, time):
        logging.info('{}: network time changed to {}'.format(self._path, time))

    ### org.freedesktop.ModemManager1.Modem.Time ###
    def GetNetworkTime(self):
        return time(self._dbus[self._interface].GetNetworkTime())
