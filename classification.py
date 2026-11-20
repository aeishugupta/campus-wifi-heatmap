
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


def analyze_location_reliability(quality_list):
    """
    Analyze Wi-Fi consistency using multiple readings
    collected from the same location.
    """

    total_readings = len(quality_list)

    if total_readings < 5:
        return {
            "reliability_score": None,
            "status": "Insufficient Data"
        }

    good_readings = quality_list.count("Good")

    reliability_score = (
        good_readings / total_readings
    ) * 100

    if reliability_score >= 80:
        status = "Consistently Good"

    elif reliability_score >= 50:
        status = "Variable Connectivity"

    else:
        status = "Needs Investigation"

    return {
        "reliability_score": round(reliability_score, 2),
        "status": status
    }


# Test the classification function
if __name__ == "__main__":
    print(classify_wifi(90, 50, 0))
    print(classify_wifi(65, 150, 3))
    print(classify_wifi(35, 300, 12))
    print(classify_wifi(10, 500, 40))
    print(
        analyze_location_reliability(
            ["Good", "Good", "Good", "Good", "Poor"]
        )
    )

    print(
        analyze_location_reliability(
            ["Good", "Poor", "Moderate", "Poor", "Good"]
        )
    )
