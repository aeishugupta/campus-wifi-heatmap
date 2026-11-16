
import streamlit as st
from analysis import get_wifi_readings


# Configure the dashboard
st.set_page_config(
    page_title="Campus Wi-Fi Intelligence System",
    page_icon="📶",
    layout="wide"
)

# Dashboard heading
st.title("📶 Campus Wi-Fi Dead-Zone Intelligence System")

# Description
st.write(
    "An interactive dashboard for monitoring Wi-Fi "
    "signal strength, network performance, and "
    "potential connectivity dead zones across campus."
)

st.divider()


# Retrieve real Wi-Fi readings from MongoDB
df = get_wifi_readings()

if df.empty:
    st.warning("No Wi-Fi readings available in the database.")

else:
    st.subheader("📊 Network Overview")

    # Calculate overall statistics
    total_readings = len(df)
    average_signal = df["signal_strength"].mean()
    average_latency = df["latency_ms"].mean()
    average_packet_loss = df["packet_loss_percent"].mean()

    # Create four dashboard columns
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Readings", total_readings)

    with col2:
        st.metric("Average Signal Strength", f"{average_signal:.2f}%")

    with col3:
        st.metric("Average Latency", f"{average_latency:.2f} ms")

    with col4:
        st.metric("Average Packet Loss", f"{average_packet_loss:.2f}%")

    st.divider()

    st.subheader("📋 Collected Wi-Fi Readings")
    st.dataframe(df, use_container_width=True)
