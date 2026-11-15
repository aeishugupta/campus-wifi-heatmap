
from datetime import datetime
from network import get_wifi_info, measure_network_performance
from database import connect_database


def save_wifi_reading():
    # Step 1: Collect Wi-Fi information
    wifi_data = get_wifi_info()

    if "error" in wifi_data:
        print("Wi-Fi error:", wifi_data["error"])
        return

    # Step 2: Measure network performance
    performance = measure_network_performance()

    # Step 3: Ask for the measurement location
    location = input("Enter your current location: ").strip()

    if not location:
        print("Location cannot be empty.")
        return

    # Step 4: Prepare MongoDB document
    reading = {
        "location": location,
        "ssid": wifi_data["ssid"],
        "signal_strength": wifi_data["signal_strength"],
        "latency_ms": performance["latency_ms"],
        "packet_loss_percent": performance["packet_loss_percent"],
        "packets_sent": performance["packets_sent"],
        "packets_received": performance["packets_received"],
        "timestamp": datetime.now()
    }

    # Step 5: Connect to MongoDB Atlas
    db = connect_database()

    if db is None:
        print("Cannot save: Database connection failed.")
        return

    # Step 6: Insert document
    result = db["wifi_readings"].insert_one(reading)

    print("\nWi-Fi reading saved successfully!")
    print("Document ID:", result.inserted_id)
    print("Saved data:", reading)


if __name__ == "__main__":
    save_wifi_reading()
