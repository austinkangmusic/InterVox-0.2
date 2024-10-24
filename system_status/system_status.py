import psutil
import platform

def get_system_status():
    # Get CPU information
    cpu_info = {
        "Physical Cores": psutil.cpu_count(logical=False),
        "Total Cores": psutil.cpu_count(logical=True),
        "Max Frequency (Mhz)": psutil.cpu_freq().max,
        "Current Frequency (Mhz)": psutil.cpu_freq().current,
        "CPU Usage (%)": psutil.cpu_percent(interval=1)
    }

    # Get RAM information
    ram_info = {
        "Total RAM (GB)": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "Available RAM (GB)": round(psutil.virtual_memory().available / (1024 ** 3), 2),
        "Used RAM (GB)": round(psutil.virtual_memory().used / (1024 ** 3), 2),
        "RAM Usage (%)": psutil.virtual_memory().percent
    }

    # GPU information can be skipped or added depending on the model
    gpu_info = [{"Message": "No dedicated GPU detected, using onboard GPU if available."}]

    # Get OS information
    os_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "OS Release": platform.release()
    }

    return {
        "CPU": cpu_info,
        "RAM": ram_info,
        "GPU": gpu_info,
        "OS": os_info
    }

if __name__ == "__main__":
    status = get_system_status()
    for key, value in status.items():
        print(f"{key}: {value}\n")
