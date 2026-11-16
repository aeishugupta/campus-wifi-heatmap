
def classify_wifi(signal, latency, packet_loss):
    """
    Classify Wi-Fi quality using signal strength,
    latency, and packet loss.
    """

    if signal >= 75 and latency <= 100 and packet_loss <= 2:
        return "Good"

    elif signal >= 50 and latency <= 200 and packet_loss <= 5:
        return "Moderate"

    elif signal >= 25 and latency <= 400 and packet_loss <= 20:
        return "Poor"

    else:
        return "Potential Dead Zone"


# Test the classification function
if __name__ == "__main__":
    print(classify_wifi(90, 50, 0))
    print(classify_wifi(65, 150, 3))
    print(classify_wifi(35, 300, 12))
    print(classify_wifi(10, 500, 40))
