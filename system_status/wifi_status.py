# system_status/wifi_status.py
import subprocess

def check_wifi_status():
    try:
        # Run a command to check Wi-Fi status (works for Unix-based systems)
        result = subprocess.run(['nmcli', 'radio', 'wifi'], stdout=subprocess.PIPE)
        wifi_status = result.stdout.decode().strip()
        return wifi_status
    except Exception as e:
        return f"Error checking Wi-Fi status: {str(e)}"
