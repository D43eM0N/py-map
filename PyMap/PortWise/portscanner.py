from scan import _scan
from ports import _ports
import asyncio
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), '..', 'PyMap')))

from args import _args

async def main():

    args = _args()

    if args.scan == True:
        await _scan(args.device)

    if args.interface == True:
        #_interface()
        None

if __name__ == "__main__":
    asyncio.run(main())
