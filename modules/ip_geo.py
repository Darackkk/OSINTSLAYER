

import requests

def run(ip):
    print("\n\033[94m[+] Performing IP Geolocation...\033[0m")
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        data = response.json()

        if data['status'] == 'success':
            print(f"\nIP: {ip}")
            print(f"Country: {data['country']}")
            print(f"Region: {data['regionName']}")
            print(f"City: {data['city']}")
            print(f"Latitude: {data['lat']}, Longitude: {data['lon']}")
            print(f"ISP: {data['isp']}")
            print(f"Organization: {data['org']}")
        else:
            print("Error fetching geolocation data.")

    except Exception as e:
        print(f"Error: {e}")
