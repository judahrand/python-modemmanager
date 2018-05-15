# ModemManager - a library to make interacting with the ModemManager daemon
# easier.
#
# (C)2018 Open Broadcast Systems Ltd
# License: MIT


from enum import Enum


class MMConnectionError(Enum):
    MM_CONNECTION_ERROR_UNKNOWN = 0      # < nick=Unknown    >
    MM_CONNECTION_ERROR_NO_CARRIER = 1   # < nick=NoCarrier  >
    MM_CONNECTION_ERROR_NO_DIALTONE = 2  # < nick=NoDialtone >
    MM_CONNECTION_ERROR_BUSY = 3         # < nick=Busy       >
    MM_CONNECTION_ERROR_NO_ANSWER = 4    # < nick=NoAnswer   >


class MMCoreError(Enum):
    MM_CORE_ERROR_FAILED = 0        # < nick=Failed       >
    MM_CORE_ERROR_CANCELLED = 1     # < nick=Cancelled    >
    MM_CORE_ERROR_ABORTED = 2       # < nick=Aborted      >
    MM_CORE_ERROR_UNSUPPORTED = 3   # < nick=Unsupported  >
    MM_CORE_ERROR_NO_PLUGINS = 4    # < nick=NoPlugins    >
    MM_CORE_ERROR_UNAUTHORIZED = 5  # < nick=Unauthorized >
    MM_CORE_ERROR_INVALID_ARGS = 6  # < nick=InvalidArgs  >
    MM_CORE_ERROR_IN_PROGRESS = 7   # < nick=InProgress   >
    MM_CORE_ERROR_WRONG_STATE = 8   # < nick=WrongState   >
    MM_CORE_ERROR_CONNECTED = 9     # < nick=Connected    >
    MM_CORE_ERROR_TOO_MANY = 10     # < nick=TooMany      >
    MM_CORE_ERROR_NOT_FOUND = 11    # < nick=NotFound     >
    MM_CORE_ERROR_RETRY = 12        # < nick=Retry        >
    MM_CORE_ERROR_EXISTS = 13       # < nick=Exists       >


class MMMessageError(Enum):
    # 0 -> 127 per 3GPP TS 24.011 [6] clause E.2
    # 128 -> 255 per 3GPP TS 23.040 [3] clause 9.2.3.22
    MM_MESSAGE_ERROR_ME_FAILURE = 300  # < nick=MeFailure            >
    MM_MESSAGE_ERROR_SMS_SERVICE_RESERVED   = 301  # < nick=SmsServiceReserved   >
    MM_MESSAGE_ERROR_NOT_ALLOWED = 302             # < nick=NotAllowed           >
    MM_MESSAGE_ERROR_NOT_SUPPORTED = 303           # < nick=NotSupported         >
    MM_MESSAGE_ERROR_INVALID_PDU_PARAMETER  = 304  # < nick=InvalidPduParameter  >
    MM_MESSAGE_ERROR_INVALID_TEXT_PARAMETER = 305  # < nick=InvalidTextParameter >
    MM_MESSAGE_ERROR_SIM_NOT_INSERTED = 310        # < nick=SimNotInserted       >
    MM_MESSAGE_ERROR_SIM_PIN = 311                 # < nick=SimPin               >
    MM_MESSAGE_ERROR_PH_SIM_PIN = 312              # < nick=PhSimPin             >
    MM_MESSAGE_ERROR_SIM_FAILURE = 313             # < nick=SimFailure           >
    MM_MESSAGE_ERROR_SIM_BUSY = 314                # < nick=SimBusy              >
    MM_MESSAGE_ERROR_SIM_WRONG = 315               # < nick=SimWrong             >
    MM_MESSAGE_ERROR_SIM_PUK = 316                 # < nick=SimPuk               >
    MM_MESSAGE_ERROR_SIM_PIN2 = 317                # < nick=SimPin2              >
    MM_MESSAGE_ERROR_SIM_PUK2 = 318                # < nick=SimPuk2              >
    MM_MESSAGE_ERROR_MEMORY_FAILURE = 320          # < nick=MemoryFailure        >
    MM_MESSAGE_ERROR_INVALID_INDEX = 321           # < nick=InvalidIndex         >
    MM_MESSAGE_ERROR_MEMORY_FULL = 322             # < nick=MemoryFull           >
    MM_MESSAGE_ERROR_SMSC_ADDRESS_UNKNOWN = 330    # < nick=SmscAddressUnknown   >
    MM_MESSAGE_ERROR_NO_NETWORK = 331              # < nick=NoNetwork            >
    MM_MESSAGE_ERROR_NETWORK_TIMEOUT = 332         # < nick=NetworkTimeout       >
    MM_MESSAGE_ERROR_NO_CNMA_ACK_EXPECTED = 340    # < nick=NoCnmaAckExpected    >
    MM_MESSAGE_ERROR_UNKNOWN = 500                 # < nick=Unknown              >


class MMMobileEquipmentError(Enum):
    MM_MOBILE_EQUIPMENT_ERROR_PHONE_FAILURE = 0          # < nick=PhoneFailure >
    MM_MOBILE_EQUIPMENT_ERROR_NO_CONNECTION = 1          # < nick=NoConnection >
    MM_MOBILE_EQUIPMENT_ERROR_LINK_RESERVED = 2          # < nick=LinkReserved >
    MM_MOBILE_EQUIPMENT_ERROR_NOT_ALLOWED = 3            # < nick=NotAllowed >
    MM_MOBILE_EQUIPMENT_ERROR_NOT_SUPPORTED = 4          # < nick=NotSupported >
    MM_MOBILE_EQUIPMENT_ERROR_PH_SIM_PIN = 5             # < nick=PhSimPin >
    MM_MOBILE_EQUIPMENT_ERROR_PH_FSIM_PIN = 6            # < nick=PhFsimPin >
    MM_MOBILE_EQUIPMENT_ERROR_PH_FSIM_PUK = 7            # < nick=PhFsimPuk >
    MM_MOBILE_EQUIPMENT_ERROR_SIM_NOT_INSERTED = 10      # < nick=SimNotInserted >
    MM_MOBILE_EQUIPMENT_ERROR_SIM_PIN = 11               # < nick=SimPin >
    MM_MOBILE_EQUIPMENT_ERROR_SIM_PUK = 12               # < nick=SimPuk >
    MM_MOBILE_EQUIPMENT_ERROR_SIM_FAILURE = 13           # < nick=SimFailure >
    MM_MOBILE_EQUIPMENT_ERROR_SIM_BUSY = 14              # < nick=SimBusy >
    MM_MOBILE_EQUIPMENT_ERROR_SIM_WRONG = 15             # < nick=SimWrong >
    MM_MOBILE_EQUIPMENT_ERROR_INCORRECT_PASSWORD   = 16  # < nick=IncorrectPassword >
    MM_MOBILE_EQUIPMENT_ERROR_SIM_PIN2 = 17              # < nick=SimPin2 >
    MM_MOBILE_EQUIPMENT_ERROR_SIM_PUK2 = 18              # < nick=SimPuk2 >
    MM_MOBILE_EQUIPMENT_ERROR_MEMORY_FULL = 20           # < nick=MemoryFull >
    MM_MOBILE_EQUIPMENT_ERROR_INVALID_INDEX = 21         # < nick=InvalidIndex >
    MM_MOBILE_EQUIPMENT_ERROR_NOT_FOUND = 22             # < nick=NotFound >
    MM_MOBILE_EQUIPMENT_ERROR_MEMORY_FAILURE = 23        # < nick=MemoryFailure >
    MM_MOBILE_EQUIPMENT_ERROR_TEXT_TOO_LONG = 24         # < nick=TextTooLong >
    MM_MOBILE_EQUIPMENT_ERROR_INVALID_CHARS = 25         # < nick=InvalidChars >
    MM_MOBILE_EQUIPMENT_ERROR_DIAL_STRING_TOO_LONG = 26  # < nick=DialStringTooLong >
    MM_MOBILE_EQUIPMENT_ERROR_DIAL_STRING_INVALID = 27   # < nick=DialStringInvalid >
    MM_MOBILE_EQUIPMENT_ERROR_NO_NETWORK = 30            # < nick=NoNetwork >
    MM_MOBILE_EQUIPMENT_ERROR_NETWORK_TIMEOUT = 31       # < nick=NetworkTimeout >
    MM_MOBILE_EQUIPMENT_ERROR_NETWORK_NOT_ALLOWED  = 32  # < nick=NetworkNotAllowed >
    MM_MOBILE_EQUIPMENT_ERROR_NETWORK_PIN = 40           # < nick=NetworkPin >
    MM_MOBILE_EQUIPMENT_ERROR_NETWORK_PUK = 41           # < nick=NetworkPuk >
    MM_MOBILE_EQUIPMENT_ERROR_NETWORK_SUBSET_PIN = 42    # < nick=NetworkSubsetPin >
    MM_MOBILE_EQUIPMENT_ERROR_NETWORK_SUBSET_PUK = 43    # < nick=NetworkSubsetPuk >
    MM_MOBILE_EQUIPMENT_ERROR_SERVICE_PIN = 44           # < nick=ServicePin >
    MM_MOBILE_EQUIPMENT_ERROR_SERVICE_PUK = 45           # < nick=ServicePuk >
    MM_MOBILE_EQUIPMENT_ERROR_CORP_PIN = 46              # < nick=CorpPin >
    MM_MOBILE_EQUIPMENT_ERROR_CORP_PUK = 47              # < nick=CorpPuk >
    MM_MOBILE_EQUIPMENT_ERROR_UNKNOWN = 100              # < nick=Unknown >
    # GPRS related errors
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_IMSI_UNKNOWN_IN_HLR = 102            # < nick=GprsImsiUnknownInHlr           >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_ILLEGAL_MS = 103                     # < nick=GprsIllegalMs                  >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_IMSI_UNKNOWN_IN_VLR = 104            # < nick=GprsImsiUnknownInVlr           >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_ILLEGAL_ME = 106                     # < nick=GprsIllegalMe                  >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_NOT_ALLOWED = 107            # < nick=GprsServiceNotAllowed          >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_PLMN_NOT_ALLOWED = 111               # < nick=GprsPlmnNotAllowed             >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_LOCATION_NOT_ALLOWED = 112           # < nick=GprsLocationNotAllowed         >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_ROAMING_NOT_ALLOWED = 113            # < nick=GprsRomaingNotAllowed          >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_NO_CELLS_IN_LOCATION_AREA = 115      # < nick=GprsNoCellsInLocationArea      >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_NETWORK_FAILURE = 117                # < nick=GprsNetworkFailure             >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_CONGESTION = 122                     # < nick=GprsCongestion                 >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_INSUFFICIENT_RESOURCES = 126         # < nick=GprsInsufficientResources      >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_MISSING_OR_UNKNOWN_APN = 127         # < nick=GprsMissingOrUnknownApn        >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_USER_AUTHENTICATION_FAILED = 129     # < nick=GprsUserAuthenticationFailed   >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_NOT_SUPPORTED = 132   # < nick=GprsServiceOptionNotSupported  >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_NOT_SUBSCRIBED = 133  # < nick=GprsServiceOptionNotSubscribed >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_SERVICE_OPTION_OUT_OF_ORDER = 134    # < nick=GprsServiceOptionOutOfOrder    >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_UNKNOWN = 148                        # < nick=GprsUnknown                    >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_PDP_AUTH_FAILURE = 149               # < nick=GprsPdpAuthFailure             >
    MM_MOBILE_EQUIPMENT_ERROR_GPRS_INVALID_MOBILE_CLASS = 150           # < nick=GprsInvalidMobileClass         >


class MMSerialError(Enum):
    MM_SERIAL_ERROR_UNKNOWN = 0                # < nick=Unknown            >
    MM_SERIAL_ERROR_OPEN_FAILED = 1            # < nick=OpenFailed         >
    MM_SERIAL_ERROR_SEND_FAILED = 2            # < nick=SendFailed         >
    MM_SERIAL_ERROR_RESPONSE_TIMEOUT = 3       # < nick=ResponseTimeout    >
    MM_SERIAL_ERROR_OPEN_FAILED_NO_DEVICE = 4  # < nick=OpenFailedNoDevice >
    MM_SERIAL_ERROR_FLASH_FAILED = 5           # < nick=FlashFailed        >
    MM_SERIAL_ERROR_NOT_OPEN = 6               # < nick=NotOpen            >
    MM_SERIAL_ERROR_PARSE_FAILED = 7           # < nick=ParseFailed        >
    MM_SERIAL_ERROR_FRAME_NOT_FOUND = 8        # < nick=FrameNotFound      >


class MMCdmaActivationError(Enum):
    MM_CDMA_ACTIVATION_ERROR_NONE = 0                            # < nick=None                         >
    MM_CDMA_ACTIVATION_ERROR_UNKNOWN = 1                         # < nick=Unknown                      >
    MM_CDMA_ACTIVATION_ERROR_ROAMING = 2                         # < nick=Roaming                      >
    MM_CDMA_ACTIVATION_ERROR_WRONG_RADIO_INTERFACE = 3           # < nick=WrongRadioInterface          >
    MM_CDMA_ACTIVATION_ERROR_COULD_NOT_CONNECT = 4               # < nick=CouldNotConnect              >
    MM_CDMA_ACTIVATION_ERROR_SECURITY_AUTHENTICATION_FAILED = 5  # < nick=SecurityAuthenticationFailed >
    MM_CDMA_ACTIVATION_ERROR_PROVISIONING_FAILED = 6             # < nick=ProvisioningFailed           >
    MM_CDMA_ACTIVATION_ERROR_NO_SIGNAL = 7                       # < nick=NoSignal                     >
    MM_CDMA_ACTIVATION_ERROR_TIMED_OUT = 8                       # < nick=TimedOut                     >
    MM_CDMA_ACTIVATION_ERROR_START_FAILED = 9                    # < nick=StartFailed                  >
