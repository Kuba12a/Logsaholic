from scapy.all import *
import Evtx.Evtx as evtx
import re


def detect_malware_name(file):    
    condition = False
    keys = ["powershell", "empire", "trojan"]

    #procesowanie pcap
    if(file.split(".")[1] == "pcapng"):
        pkts = sniff(offline=file, pnr=None, filter='tcp port 80')
        for pkt in pkts:
            payload = pkt.sprintf("{Raw:%Raw.load%}\n")
            for key in keys:
                if key in payload: condition = True
 
    #procesowanie evtx
    elif(file.split(".")[1] == "evtx"):
        with evtx.Evtx(file) as log:
            for record in log.records():
                payload = str(record.xml())
                for key in keys:
                    if key in payload: condition = True


    #procesowanie xml, json i txt
    elif(file.split(".")[1] in ["xml","json","txt"]):
        with open(file, 'r') as f:
            payload = f.read()
            for key in keys:
                if key in payload: condition = True

    
    if condition == True:
        action_alert = "local" # akcja: "local", "remote"
        action_block = False # or False
        description = "Opis eventu, low risk" # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description



def detect_malware_ip(file):
    condition = False
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')   #Ip regex
    keys = ["666.666.666.666", "119.189.231.225", "43.128.202.179", "192.168.178.4"]
    #procesowanie pcap
    if(file.split(".")[1] == "pcapng"):
        pkts = sniff(offline=file, pnr=None, filter='tcp port 80')
        for pkt in pkts:
            payload = pkt.sprintf("{Raw:%Raw.load%}\n")
            for key in keys:
                if key in payload: condition = True


        '''
        ips = []
        u=1
        for p in PcapNgReader(file):
            print(p[IPField].dst)
            if IPField in p:    
                u+=1    
                print(p[IPField].dst)      
                ips.append(p[IPField].src)
                ips.append(p[IPField].dst)
            if u==5:
                break
        for ip in ips:
            if ip in keys: 
                condition = True
                print(ip)
            '''

    #procesowanie evtx
    elif(file.split(".")[1] == "evtx"):
        #print("Weszlo do evtx")
        with evtx.Evtx(file) as log:
            for record in log.records():
                payload = str(record.xml())
                for key in keys:
                    if key in payload: condition = True


    #procesowanie xml, json i txt
    elif(file.split(".")[1] in ["xml","json","txt"]):
        #print("Wchodzi do txt")
        result = []
        with open(file, 'r') as f:
            for line in f:
                for l in ip_pattern.findall(line):
                    result.append(l)

            for key in keys:
                if key in result: 
                    condition = True

    if condition==True:
        action_alert = "remote" # akcja: "local", "remote"
        action_block = True # or False
        description = "Opis Eventu, high risk"  # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description





#TODO
def detect_malware_url(file):
    condition = False
    keys = ["http://malware.com", "https://studia.elka.pw.edu.pl/", "http://virus.com"]

    if condition==True:
        action_alert = "remote" # akcja: "local", "remote"
        action_block = False # or False
        description = "Opis eventu, medium risk" # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description

