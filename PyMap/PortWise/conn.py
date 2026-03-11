import socket
import asyncio

async def _conn(ip: str, port: int, bouncer: asyncio.Semaphore):
    async with bouncer:
        #Create socket object
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setblocking(False)
        #limit 
        bouncer = asyncio.Semaphore(500)

        #Creates a asynchronous event loop for tasks
        loop = asyncio.get_event_loop()

        async with bouncer:
            try:
                #wait for connection
                await asyncio.wait_for(loop.sock_connect(serv, (ip, port)), timeout=0.5)
                status = 0
            
            #Checks for an error expect port is closed or timeout
            except (ConnectionRefusedError, asyncio.TimeoutError, OSError):
                status = 1
            finally:
                serv.close()

            return port,status


