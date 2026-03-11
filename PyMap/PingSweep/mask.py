import psutil
from exceptionHandling import check_net_type

def get_subnet_mask(net_type: str) -> str:

    #checks if entered net(like wifi, etc.) is exist
    check_net_type(net_type)

    #gets interface, and addresses from psutil output
    for interface, addrs in psutil.net_if_addrs().items():
        if interface == net_type:
            for addr in addrs:
                #Checks for IPv4
                if addr.family == 2:
                    return addr.netmask