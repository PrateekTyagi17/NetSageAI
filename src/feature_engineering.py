import pandas as pd
import os

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "packets.csv"
)

df = pd.read_csv(file_path)

features = df.groupby("source_ip").agg({
    "packet_size": ["count", "mean", "sum"]
})

features.columns = [
    "packet_count",
    "avg_packet_size",
    "traffic_volume"
]

features = features.reset_index()

print("\nGenerated Features:")
print(features.head())

output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "features.csv"
)

features.to_csv(output_path, index=False)

print("\nFeatures saved successfully!")