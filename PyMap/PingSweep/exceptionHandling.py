import ipaddress
import sys
import psutil

INTERFACE_LIST = psutil.net_if_addrs().keys()

def validate_ip_address(ip_string: str):
    try:
        ip_object = ipaddress.ip_address(ip_string)
    except ValueError:
         print("Ip format is incorrect!\nQuiting PyMap...")
         raise sys.exit(0)


def check_net_type(net_type: str):
    if net_type not in INTERFACE_LIST:
        print("Invalid network type! Quiting PyMap...")
        raise sys.exit(0)