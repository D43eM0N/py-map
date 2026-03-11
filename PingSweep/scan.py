import asyncio
from ping import ping_by_os 
import ipaddress


async def scan(net_addr: str):
    print("|---------------------------|")

    tasks = []
    network = ipaddress.IPv4Network(f"{net_addr}", strict=False)
    async with asyncio.TaskGroup() as tg:
        for host in network.hosts():
            task = tg.create_task(ping_by_os(host))
            tasks.append(task)