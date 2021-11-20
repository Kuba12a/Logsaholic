from scapy.all import *
from scapy.layers.l2 import Ether
from scapy.layers.inet import IP, TCP

def process_pcap(file_name, filt):
    print('Opening {}...'.format(file_name))
    filtered = sniff(offline=file_name,pnr=None,filter=str(filt))
    print('Showing {} filtered packets'.format(len(filtered)))
    return filtered
    


def display_pkts(pkts):
    pkts.nsummary()
    while True:
        i = input("enter packet number or exit: ")
        if(i=='exit'): 
            break
        elif(i.isnumeric): 
            pkts[int(i)].show()

def validate_filter(filter):
    try:
        compile_filter(filter)
    except:
        return False
    return True