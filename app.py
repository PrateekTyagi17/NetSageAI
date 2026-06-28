import streamlit as st
import pandas as pd
import os
import plotly.express as px

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="NetSage AI",
    page_icon="🌐",
    layout="wide"
)

# -------------------------------
# Load Datasets
# -------------------------------
packets_path = os.path.join("data", "packets.csv")
anomaly_path = os.path.join("data", "anomaly_results.csv")

packets_df = pd.read_csv(packets_path)
anomaly_df = pd.read_csv(anomaly_path)

# -------------------------------
# Calculate Dashboard Metrics
# -------------------------------
total_packets = len(packets_df)

unique_source_ips = packets_df["source_ip"].nunique()

average_packet_size = round(
    packets_df["packet_size"].mean(), 2
)

suspicious_ips = len(
    anomaly_df[anomaly_df["anomaly"] == -1]
)

# -------------------------------
# Dashboard Title
# -------------------------------
st.title("🌐 NetSage AI")

st.subheader(
    "AI-Powered Network Traffic Analytics & Anomaly Detection"
)

st.write("""
Welcome to NetSage AI.

This dashboard provides insights into captured network traffic,
feature engineering results, and machine learning-based anomaly detection.
""")

st.divider()

# -------------------------------
# Dashboard Metrics
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "📦 Total Packets",
        total_packets
    )

with col2:
    st.metric(
        "🌍 Unique Source IPs",
        unique_source_ips
    )

with col3:
    st.metric(
        "📏 Average Packet Size",
        f"{average_packet_size} Bytes"
    )

with col4:
    st.metric(
        "🚨 Suspicious IPs",
        suspicious_ips
    )
    st.divider()

st.subheader("📊 Protocol Distribution")

protocol_counts = (
    packets_df["protocol"]
    .value_counts()
    .reset_index()
)

protocol_counts.columns = [
    "Protocol",
    "Count"
]

# Convert protocol numbers into names
protocol_counts["Protocol"] = protocol_counts["Protocol"].replace({
    6: "TCP",
    17: "UDP"
})

fig = px.bar(
    protocol_counts,
    x="Protocol",
    y="Count",
    color="Protocol",
    text="Count",
    title="Network Protocol Distribution"
)

st.plotly_chart(
    fig,
    use_container_width=True
)
st.divider()

st.subheader("🌍 Top 10 Source IP Addresses")

top_ips = (
    packets_df["source_ip"]
    .value_counts()
    .head(10)
    .reset_index()
)

top_ips.columns = [
    "Source IP",
    "Packet Count"
]

fig2 = px.bar(
    top_ips,
    x="Source IP",
    y="Packet Count",
    color="Packet Count",
    text="Packet Count",
    title="Top 10 Source IPs"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

