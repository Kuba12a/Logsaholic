from scapy.all import *
import Evtx.Evtx as evtx


def detectMalwareName(file):    
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



def detectMalwareURL(file):
    condition = True

    if condition==True:
        action_alert = "remote" # akcja: "local", "remote"
        action_block = False # or False
        description = "Opis eventu, medium risk" # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description\

    
def detectMalwareIP(file):
    # ciało funkcji - właściwa reguła operująca na danych z args
    # procesowanie pcap
    # for pcap in kwargs[pcap]:
    # procesowanie evtx
    # for evtx in kwargs[evtx]:
    # procesowanie xml
    # for xml in kwargs[xml]:
    # procesowanie json
    # for json in kwargs[json]:
    # procesowanie txt
    # for txt in kwargs[txt]:
    # ostateczna reguła - tj. co ma się wykonać

    condition = True

    if condition==True:
        action_alert = "remote" # akcja: "local", "remote"
        action_block = True # or False
        description = "opis Eventu, high risk" # format w OFF.8.5
    else:
        action_alert = None
        action_block = None
        description = None
    return action_alert, action_block, description
