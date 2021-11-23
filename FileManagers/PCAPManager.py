from scapy.all import *
from scapy.arch import compile_filter
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP

def process_pcap(file_name, filter):
    print('Opening {}...'.format(file_name))
    filtered = sniff(offline=file_name, pnr=None, filter=str(filter))
    print('Showing {} filtered packets'.format(len(filtered)))
    return filtered
    


def display_pkts(packages):
    packages.nsummary()
    while True:
        i = input("enter packet number or exit: ")
        if(i=='exit'): 
            break
        elif(i.isnumeric): 
            packages[int(i)].show()

def validate_filter(filter):
    try:
        compile_filter(filter)
    except:
        return False
    return True