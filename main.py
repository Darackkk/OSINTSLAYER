# osint_recon_toolkit/main.py

import sys
from modules import whois_lookup, dns_enum, ip_geo, shodan_scan

def menu():
    print("\n\033[92m--- OSINT Recon Toolkit ---\033[0m")
    print("1. WHOIS Lookup")
    print("2. DNS Enumeration")
    print("3. IP Geolocation")
    print("4. Shodan Scan (requires API key)")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("\nSelect an option (1-5): ").strip()
        
        if choice == '1':
            domain = input("Enter domain or IP: ").strip()
            whois_lookup.run(domain)
        elif choice == '2':
            domain = input("Enter domain: ").strip()
            dns_enum.run(domain)
        elif choice == '3':
            ip = input("Enter IP address: ").strip()
            ip_geo.run(ip)
        elif choice == '4':
            ip = input("Enter IP or domain: ").strip()
            api_key = input("Enter your Shodan API Key: ").strip()
            shodan_scan.run(ip, api_key)
        elif choice == '5':
            print("\nGoodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
