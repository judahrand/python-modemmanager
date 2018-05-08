# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from ModemManager.ModemManager import ModemManagerHelper


class ModemCdma(ModemManagerHelper):
    def __init__(self, path):
        super(ModemCdma, self).__init__(interface='org.freedesktop.ModemManager1.Modem.ModemCdma', path=path)

    ### org.freedesktop.ModemManager1.Modem.ModemCdma ###
    def Activate(self, carrier_code):
        self._dbus.Activate(carrier_code)

    def ActivateManual(self, properties):
        self._dbus.Activate(properties)
