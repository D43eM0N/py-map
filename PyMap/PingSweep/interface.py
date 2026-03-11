import socket
import ipaddress


def get_net_info(ip: str, mask: str) -> str:
    host = socket.gethostname()
    net = ipaddress.IPv4Network(f"{ip}/{mask}", strict=False)

    return host,net,f"/{net.prefixlen}"