import psutil
from exceptionHandling import check_net_type

def get_subnet_mask(net_type: str) -> str:
    """
    this function does this

    net_type str 

    str - what is it
    """
    check_net_type(net_type)
    for interface, addrs in psutil.net_if_addrs().items():
        if interface == net_type:
            for addr in addrs:
                if addr.family == 2:
                    return addr.netmask