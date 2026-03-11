import asyncio
from conn import _conn
from ports import _ports

async def _scan(ip :str):
    print("[+]Starts to port scanning...")
    print("|------------------------------------|")

    bouncer = asyncio.Semaphore(500)

    #create asynchronous connection tasks
    tasks = [_conn(ip, port, bouncer) for port in range(1, 1024)]

    #get all task results
    results =  await asyncio.gather(*tasks)
    
    for port, status in results:
        #if port is open
        if status == 0:
            port_name = _ports(port)
            print(f"━━ {port:<8}  open--{port_name} ")
            print("|------------------------------------|")

    
        
            

            

    