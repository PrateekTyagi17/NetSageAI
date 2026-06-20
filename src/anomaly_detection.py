import pandas as pd
import os
from sklearn.ensemble import IsolationForest

file_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "features.csv"
)

df = pd.read_csv(file_path)

X = df[[
    "packet_count",
    "avg_packet_size",
    "traffic_volume"
]]

model = IsolationForest(
    contamination=0.1,
    random_state=42
)

df["anomaly"] = model.fit_predict(X)

print(df[[
    "source_ip",
    "packet_count",
    "avg_packet_size",
    "traffic_volume",
    "anomaly"
]])

output_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "anomaly_results.csv"
)

df.to_csv(output_path, index=False)

print("\nAnomaly Detection Complete!")