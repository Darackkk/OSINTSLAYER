# osint_recon_toolkit/modules/whois_lookup.py

import whois

def run(target):
    print("\n\033[94m[+] Performing WHOIS Lookup...\033[0m")
    try:
        info = whois.whois(target)
        print("\nWHOIS Information:\n")
        print(f"Domain: {info.domain_name}")
        print(f"Registrar: {info.registrar}")
        print(f"Creation Date: {info.creation_date}")
        print(f"Expiration Date: {info.expiration_date}")
        print(f"Emails: {info.emails}")
        print(f"Name Servers: {info.name_servers}")
    except Exception as e:
        print(f"Error: {e}")
