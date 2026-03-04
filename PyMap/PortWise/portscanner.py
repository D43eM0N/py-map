import sys ; sys.path.insert(0, r'..\PyMap')
from args import _args
from scan import _scan
from PortWise.ports import _ports
import asyncio

async def main():

    args = _args()

    if args.scan == True:
        await _scan(args.device)

    if args.interface == True:
        #_interface()
        None

if __name__ == "__main__":
    asyncio.run(main())