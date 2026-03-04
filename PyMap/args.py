import argparse
from PingSweep.exceptionHandling import validate_ip_address


def _args():
    parser = argparse.ArgumentParser(usage="-d <ip> -n <net> -s", 
                                     
    description="PyMap: Network Scanning Tool", 

    epilog="You can give a feedback on my github which my nickname is D43emM0N! Thanks for having me!"

    ,add_help=True)


    parser.add_argument("-d", "--device", 
                        metavar="device ip", 
                        help="Target IP address (e.g., 192.168.1.1)", 
                        required=True
                        )
    
    parser.add_argument("-n", "--net", 
                        metavar="net type", 
                        help="Define network type"
                        )
    
    parser.add_argument("-s", "--scan", 
                        action='store_true' ,
                        help="Scans the LAN network"
                        )
    
    parser.add_argument("-i", "--interface",
                        action="store_true" ,
                        help="Shows Network Information about device"
                        )

    args = parser.parse_args()

    if args.device in ["-h", "--help"]:
        print(parser.print_help())
    else:
        validate_ip_address(args.device)
    

    return args
