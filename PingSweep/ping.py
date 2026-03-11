import asyncio
import platform
import sys

async def ping_by_os(ip: str):
    os_name = platform.system().lower()

    if os_name == "windows":
        await ping(ip,"-n","TTL","find")
    elif os_name == "linux":
        await ping(ip,"-c","ttl","grep")
    else:
        print("[-]OS did not match!")
        print("Quiting PyMap...")
        sys.exit(0)


async def ping(ip: str,cmd: str,ttl: str,search_tool: str): 
    try:
        process = await asyncio.create_subprocess_exec('ping', cmd, '1' ,f'{ip}',
        stderr=asyncio.subprocess.DEVNULL, stdout=asyncio.subprocess.PIPE)

        stdout, _ = await process.communicate()
        output = stdout.decode(errors='ignore')

        if f'{ttl}=' in output:
            print(f"[+] {ip} - Host is up") 
            print("|---------------------------|")
    except Exception as e:
        print(e)  