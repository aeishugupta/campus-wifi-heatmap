import ping3
import subprocess
import re
from datetime import datetime


def get_wifi_info():
    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            errors="replace"
        )

        if result.returncode != 0:
            return {"error": "Unable to retrieve Wi-Fi information"}

        output = result.stdout

        ssid_match = re.search(
            r"^\s*SSID\s*:\s*(.+)$",
            output,
            re.MULTILINE
        )

        signal_match = re.search(
            r"^\s*Signal\s*:\s*(\d+)%",
            output,
            re.MULTILINE
        )

        if not ssid_match or not signal_match:
            return {"error": "No connected Wi-Fi network found"}

        return {
            "ssid": ssid_match.group(1).strip(),
            "signal_strength": int(signal_match.group(1)),
            "timestamp": datetime.now().isoformat()
        }

    except Exception as e:
        return {"error": str(e)}


def measure_network_performance(host="1.1.1.1", attempts=5):
    successful_pings = []

    for _ in range(attempts):
        try:
            response = ping3.ping(host, timeout=2, unit="ms")

            if isinstance(response, (int, float)) and not isinstance(response, bool):
                successful_pings.append(response)

        except Exception:
            pass

    packets_received = len(successful_pings)
    packets_lost = attempts - packets_received

    packet_loss = (packets_lost / attempts) * 100

    average_latency = (
        round(sum(successful_pings) / packets_received, 2)
        if packets_received > 0
        else None
    )

    return {
        "latency_ms": average_latency,
        "packet_loss_percent": round(packet_loss, 2),
        "packets_sent": attempts,
        "packets_received": packets_received
    }



if __name__ == "__main__":
    wifi_data = get_wifi_info()
    network_data = measure_network_performance()

    print("Wi-Fi Information:", wifi_data)
    print("Network Performance:", network_data)