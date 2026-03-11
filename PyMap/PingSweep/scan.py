import asyncio
from ping import ping_by_os 
import ipaddress


async def scan(net_addr: str):
    print("|---------------------------|")

    tasks = []

    #network object
    network = ipaddress.IPv4Network(f"{net_addr}", strict=False)

    #getting all hosts from network
    async with asyncio.TaskGroup() as tg:
        for host in network.hosts():
            #pinging for if they are active or not
            task = tg.create_task(ping_by_os(host))
            tasks.append(task)