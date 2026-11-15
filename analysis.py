
import pandas as pd
from database import connect_database


def get_wifi_readings():
    # Connect to MongoDB Atlas
    db = connect_database()

    if db is None:
        return pd.DataFrame()

    # Retrieve all Wi-Fi readings
    collection = db["wifi_readings"]
    readings = list(collection.find({}, {"_id": 0}))

    # Convert MongoDB documents into a DataFrame
    df = pd.DataFrame(readings)

    return df


def analyze_wifi_data():
    df = get_wifi_readings()

    if df.empty:
        print("No Wi-Fi readings available.")
        return

    print("\n--- Wi-Fi Readings ---")
    print(df.to_string(index=False))

    print("\n--- Network Statistics ---")

    print(
        "Average Signal Strength:",
        round(df["signal_strength"].mean(), 2),
        "%"
    )

    print(
        "Average Latency:",
        round(df["latency_ms"].mean(), 2),
        "ms"
    )

    print(
        "Average Packet Loss:",
        round(df["packet_loss_percent"].mean(), 2),
        "%"
    )


def analyze_by_location():
    df = get_wifi_readings()

    if df.empty:
        print("No Wi-Fi readings available.")
        return

    required_columns = [
        "location",
        "signal_strength",
        "latency_ms",
        "packet_loss_percent"
    ]

    if not all(col in df.columns for col in required_columns):
        print("Some required columns are missing.")
        return

    location_stats = df.groupby("location").agg(
        average_signal=("signal_strength", "mean"),
        average_latency=("latency_ms", "mean"),
        average_packet_loss=("packet_loss_percent", "mean"),
        total_readings=("location", "count")
    ).reset_index()

    location_stats = location_stats.round(2)

    print("\n--- Location-wise Wi-Fi Analysis ---")
    print(location_stats.to_string(index=False))

    return location_stats



if __name__ == "__main__":
    analyze_wifi_data()
    analyze_by_location()
