from scapy.all import *


def process_pcap(file_name, filter):
    print('Opening {}...'.format(file_name))
    filtered = sniff(offline=file_name, pnr=None, filter=str(filter))
    print('Showing {} filtered packets'.format(len(filtered)))
    return filtered


def display_pkts(packages):
    packages.nsummary()
    while True:
        i = input("enter packet number or exit: ")
        if (i == 'exit'):
            break
        elif (i.isnumeric):
            packages[int(i)].show()


def sum_payload(packets):
    packet_size = 0
    for pkt in packets:
        packet_size += len(pkt)
    return packet_size

def get_inbound_packets(filename, ip_address):
    return process_pcap(filename, f"src host {ip_address}")

def get_outbound_packets(filename, ip_address):
    return process_pcap(filename, f"dst host {ip_address}")


def get_ips(packets):
    ips = []
    dic = {}
    for pkt in packets:
        temp = pkt.sprintf("%IP.src%")
        dic[temp] = 1

    for ip in dic.keys():
        ips.append(ip)
    return ips



def validate_filter(filter):
    #try:
        #arch.compile_filter("tcp")
    #except:
        #return False
    return True
