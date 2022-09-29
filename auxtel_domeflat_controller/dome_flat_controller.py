import argparse
import sys
from labjack import ljm # type: ignore
import socket

_DEFAULT_ADDRESS = "auxtel-labjack02.cp.lsst.org"

class DomeFlatController:
    _PINNAME = "FIO0"
    def __init__(self, labjackaddr: str = _DEFAULT_ADDRESS):
        self._labjackaddr = labjackaddr
        #check if we were passed an IP address
        try:
            socket.inet_aton(labjackaddr)
        except OSError:
            #this is not an ip address
            ipaddr = socket.gethostbyname(labjackaddr)
        else:
            #this is an IP address
            ipaddr = labjackaddr

        self._hdl = ljm.open(ljm.constants.dtT7,
                             ljm.constants.ctETHERNET,
                             ipaddr)

    @property
    def domeFlatState(self) -> bool:
        state = ljm.eReadName(self._hdl, self._PINNAME)
        return bool(int(state))

    @domeFlatState.setter
    def domeFlatState(self, state: bool) -> None:
        ljm.eWriteName(self._hdl, self._PINNAME, float(int(state)))


def script():
    ap = argparse.ArgumentParser("dome_flat_controller",
                                 description="manually turn on and off the auxtel dome flat")

    ap.add_argument("state", type=int, nargs="?", help="the state to set the flat to. Ignored if --read provided")
    ap.add_argument("--read", action="store_true", help="if set, read back the value rather than setting it")
    args = ap.parse_args()

    if args.state is None and not args.read:
        print("ERROR: must supply either --read or a state to set")
        sys.exit(-1)
    elif args.state is None:
        dfc = DomeFlatController(_DEFAULT_ADDRESS)
        print(int(dfc.domeFlatState))
    else:
        dfc = DomeFlatController(ADDRESS)
        dfc.domeFlatState = bool(args.state)


if __name__=="__main__":
    script()
