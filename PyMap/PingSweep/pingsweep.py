import asyncio
import sys
import os

#Finds args module in PyMap folder
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'PyMap')))

from args import _args
from mask import get_subnet_mask
from PingSweep.interface import get_net_info
from scan import scan

async def main():
    #arg: -d
    args = _args()   
    ip = args.device

    #return mask
    mask = get_subnet_mask(args.net)
    #return host,net address,cidr
    host,net_addr,cidr = get_net_info(ip, mask)
    
    #arg: -s
    if args.interface:
        print("Host: ",host)
        print(f"Ip: {ip}{cidr}")
        print(f"Network Address: {net_addr}")
        print("Net Mask: ",mask)
    #arg: -i
    if args.scan:
        print("[+]Starts to scanning...")
        await scan(net_addr)

if __name__ == "__main__":
    asyncio.run(main())