

import shodan

def run(target, api_key):
    print("\n\033[94m[+] Performing Shodan Scan...\033[0m")
    try:
        api = shodan.Shodan(api_key)
        result = api.host(target)

        print(f"\nTarget: {target}")
        print(f"Organization: {result.get('org', 'N/A')}")
        print(f"ISP: {result.get('isp', 'N/A')}")
        print(f"Country: {result.get('country_name', 'N/A')}")

        print("\nOpen Ports:")
        for port in result['ports']:
            print(f"  Port: {port}")

        print("\nVulnerabilities:")
        vulns = result.get('vulns', {})
        if vulns:
            for vuln in vulns:
                print(f"  {vuln}")
        else:
            print("  No vulnerabilities found.")

    except shodan.APIError as e:
        print(f"Shodan Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
