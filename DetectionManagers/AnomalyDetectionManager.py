import Config
import FileManagers.PCAPManager as pcap_manager

threshold = 10

def detect_anomaly(file):
    event_number = 1
    log_message = []
    packets = pcap_manager.process_pcap(file, "tcp")
    ips = pcap_manager.get_ips(packets)
    keys = []
    with open(Config.malicious_IPs, 'r') as f:
        for line in f: keys.append(line.strip())

    for ip in ips:
        if ip in keys:
            inp = pcap_manager.get_inbound_packets(file, ip)
            outp = pcap_manager.get_outbound_packets(file, ip)

            if pcap_manager.sum_payload(inp) > threshold * pcap_manager.sum_payload(outp):
                print("ANOMALY DETECTED!")
                print("Event number:" + str(event_number))
                print("Alert source : " + file)
                print("Alert type : Anomaly")
                print(f"Alert description : Possible data exfiltration detected")
