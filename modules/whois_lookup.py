# osint_recon_toolkit/modules/whois_lookup.py

import whois  # Import the correct python-whois library

def run(target):
    print("\n\033[94m[+] Performing WHOIS Lookup...\033[0m")
    try:
        # Perform the WHOIS lookup
        info = whois.whois(target)
        
        # Display key WHOIS details
        print("\nWHOIS Information:")
        print(f"Domain Name: {info.domain_name}")
        print(f"Registrar: {info.registrar}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Expiration Date: {info.expiration_date}")
        print(f"Emails: {info.emails}")
        print(f"Name Servers: {info.name_servers}")
        
    except Exception as e:
        print(f"Error: {e}")
