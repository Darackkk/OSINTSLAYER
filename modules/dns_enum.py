

import dns.resolver

def run(domain):
    print("\n\033[94m[+] Performing DNS Enumeration...\033[0m")
    try:
        # DNS record types
        record_types = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT']
        
        for record in record_types:
            try:
                answers = dns.resolver.resolve(domain, record)
                print(f"\n{record} Records:")
                for rdata in answers:
                    print(f"  {rdata}")
            except dns.resolver.NoAnswer:
                print(f"No {record} records found.")
        
        # Simple subdomain check
        subdomains = ["www", "mail", "ftp", "dev", "test"]
        print("\n\033[92m[+] Checking common subdomains...\033[0m")
        for sub in subdomains:
            try:
                target = f"{sub}.{domain}"
                answers = dns.resolver.resolve(target, 'A')
                print(f"  Found: {target} → {answers[0]}")
            except:
                pass
        
    except Exception as e:
        print(f"Error: {e}")
