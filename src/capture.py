import os
from scapy.all import sniff
import pandas as pd
from datetime import datetime

packets = []

def process_packet(packet):

    if packet.haslayer("IP"):

        packets.append({
            "timestamp": datetime.now(),
            "source_ip": packet["IP"].src,
            "destination_ip": packet["IP"].dst,
            "protocol": packet["IP"].proto,
            "packet_size": len(packet)
        })

        print(
            packet["IP"].src,
            "->",
            packet["IP"].dst
        )

print("Capturing 500 packets...")

sniff(
    prn=process_packet,
    count=5000
)

df = pd.DataFrame(packets)

import os

output_file = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "packets.csv"
)

df.to_csv(output_file, index=False)

print("Dataset Saved Successfully!")
