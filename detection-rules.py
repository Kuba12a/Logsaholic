from scapy.all import *
import Evtx.Evtx as evtx
import re
from scapy.layers.inet import IP
from scapy.layers.http import HTTPRequest
import Config
import yara
import FileManagers.FileManager as file_manager


def detect_malware_name(file):    
    condition = False
    keys=[]
    with open(Config.malicious_names, 'r') as f:
        for line in f: keys.append(line.strip()) 

    #procesowanie pcap
    if(file.split(".")[1] == "pcapng"):
        pkts = sniff(offline=file, pnr=None, filter='tcp port 80')
        for pkt in pkts:
            payload = pkt.sprintf("{Raw:%Raw.load%}\n")
            for key in keys:
                if key in payload: condition = True
            if condition: break
 
    #procesowanie evtx
    elif(file.split(".")[1] == "evtx"):
        with evtx.Evtx(file) as log:
            for record in log.records():
                payload = str(record.xml())
                for key in keys:
                    if key in payload: condition = True
                if condition: break


    #procesowanie xml, json i txt
    elif(file.split(".")[1] in ["xml","json","txt"]):
        with open(file, 'r') as f:
            payload = f.read()
            for key in keys:
                if key in payload: 
                    condition = True
                    break

    
    if condition:
        action_alert = Config.local_alert # akcja: "local", "remote"
        action_block = False # or False
        description = "low risk, malware name detected" # format w OFF.8.5
    else:
        return None
    return action_alert, action_block, description


def detect_malware_ip(file):
    condition = False
    ip_pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')   #Ip regex
    keys=[]
    with open(Config.malicious_IPs, 'r') as f:
        for line in f: keys.append(line.strip()) 

    #procesowanie pcap
    if(file.split(".")[1] == "pcapng"):
        pkts = rdpcap(file)
        for pkt in pkts:
            if IP in pkt:
                payload = [pkt[IP].src, pkt[IP].dst]
                for key in keys:
                    if key in payload: 
                        condition = True
            if condition: break

    #procesowanie evtx
    elif(file.split(".")[1] == "evtx"):
        with evtx.Evtx(file) as log:
            for record in log.records():
                payload = str(record.xml())
                for key in keys:
                    if key in payload: condition = True
                if condition: break


    #procesowanie xml, json i txt
    elif(file.split(".")[1] in ["xml","json","txt"]):
        result = []
        with open(file, 'r') as f:
            for line in f:
                for l in ip_pattern.findall(line):
                    result.append(l)

            for key in keys:
                if key in result: 
                    condition = True
                    break

    if condition:
        action_alert = Config.remote_alert # akcja: "local", "remote"
        action_block = True # or False
        description = "high risk, malware ip address detected" # format w OFF.8.5
    else:
        return None
    return action_alert, action_block, description
        

def detect_malware_url(file):
    condition = False
    keys=[]
    with open(Config.malicious_URLs, 'r') as f:
        for line in f: keys.append(line.strip()) 

    #procesowanie pcap
    if(file.split(".")[1] == "pcapng"):
        pkts = rdpcap(file)
        for pkt in pkts:
            if pkt.haslayer(HTTPRequest):
                url = pkt[HTTPRequest].Host.decode() + pkt[HTTPRequest].Path.decode()
                for key in keys:
                    if key in url: condition = True
            if condition: break

    #procesowanie xml, json i txt
    elif(file.split(".")[1] in ["xml","json","txt"]):
        with open(file, 'r') as f:
            payload = f.read()
            for key in keys:
                if key in payload: 
                    condition = True
                    break


    if condition:
        action_alert = Config.remote_alert # akcja: "local", "remote"
        action_block = False # or False
        description = "medium risk, malicious url detected" # format w OFF.8.5
    else:
        return None
    return action_alert, action_block, description


def detect_yara(file):
    condition = False
    path=input("Specify path with set of rules:")
    yar_rules = []
    if os.path.isdir(path):
        for r in file_manager.get_filenames(path,["yar"]):
            yar_rules.append(r)
    elif os.path.isfile(path):
        if path.split('.')[1] == "yar": yar_rules.append(path)
    matches=[]
    for yar_rule in yar_rules:
        rule = yara.compile(filepath=yar_rule)
        matches = rule.match(file)
        if len(matches) > 0: 
            condition = True
            break    

    if condition:
        action_alert = Config.remote_alert # akcja: "local", "remote"
        action_block = True # or False
        description = "high risk, yara detection rules matched" # format w OFF.8.5
    else:
        return None
    return action_alert, action_block, description

