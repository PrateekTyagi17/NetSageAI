import pandas as pd
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "packets.csv"
)

df = pd.read_csv(file_path)

print("=" * 50)
print("DATASET SUMMARY")
print("=" * 50)

print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\nProtocol Counts:")
print(df["protocol"].value_counts().head())

print("\nTop 5 Source IPs:")
print(df["source_ip"].value_counts().head())

print("\nTop 5 Destination IPs:")
print(df["destination_ip"].value_counts().head())

print("\nAverage Packet Size:")
print(round(df["packet_size"].mean(), 2))