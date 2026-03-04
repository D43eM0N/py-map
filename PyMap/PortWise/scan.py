import asyncio
from conn import _conn
from ports import _ports

async def _scan(ip :str):
    print("[+]Starts to port scanning...")
    print("|------------------------------------|")

    bouncer = asyncio.Semaphore(500)

    tasks = [_conn(ip, port, bouncer) for port in range(1024)]

    results =  await asyncio.gather(*tasks)
    
    for port, status in results:
        if status == 0:
            port_name = _ports(port)
            print(f"━━ {port:<8}  open--{port_name} ")
            print("|------------------------------------|")

    
        
            

            

    