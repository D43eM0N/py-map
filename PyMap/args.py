import argparse
from PingSweep.exceptionHandling import validate_ip_address


def _args():
    parser = argparse.ArgumentParser(usage="<module> -n <net> -d <ip> -s", description="PyMap is a tool for basic networking stuff. Which could able to do ip and port scan " \
    "or many kind of specific jobs!", 
    epilog="You can give a feedback on my github which my nickname is D43emM0N! Thanks for having me!")

    parser.add_argument("-d", "--device", metavar="device ip", help="Enter your devices ip", required=True)
    parser.add_argument("-n", "--net", metavar="net type", help="Define network type")
    parser.add_argument("-s", "--scan", action='store_true' ,help="Scans the LAN network")
    parser.add_argument("-i", "--interface",action="store_true" ,help="Shows Network Information about device")
    parser.add_argument("-p", "--port", metavar="port")

    args = parser.parse_args()

    validate_ip_address(args.device)
    
    
    return args