import pandas as pd
import matplotlib.pyplot as plt
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "packets.csv"
)

df = pd.read_csv(file_path)

# Convert protocol numbers to names
protocol_map = {
    6: "TCP",
    17: "UDP",
    1: "ICMP"
}

df["protocol"] = df["protocol"].map(protocol_map).fillna("Other")

protocol_counts = df["protocol"].value_counts()

plt.figure(figsize=(8, 5))
protocol_counts.plot(kind="bar")

plt.title("Network Protocol Distribution")
plt.xlabel("Protocol")
plt.ylabel("Number of Packets")
plt.xticks(rotation=0)

for i, value in enumerate(protocol_counts):
    plt.text(i, value + 20, str(value), ha="center")

plt.tight_layout()
plt.show()