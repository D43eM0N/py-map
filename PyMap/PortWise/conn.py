import socket
import asyncio

async def _conn(ip: str, port: int, bouncer: asyncio.Semaphore):
    async with bouncer:
        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serv.setblocking(False)

        bouncer = asyncio.Semaphore(500)

        loop = asyncio.get_event_loop()

        async with bouncer:
            try:
                await asyncio.wait_for(loop.sock_connect(serv, (ip, port)), timeout=0.5)
                status = 0
            except:
                status = 1
            finally:
                serv.close()

            return port,status


