<<<<<<< HEAD
# OSINTSLAYER
=======
# OSINTSLAYER

**OSINTSLAYER** is a powerful and modular **OSINT (Open Source Intelligence)** toolkit written in Python. It allows cybersecurity professionals, ethical hackers, and enthusiasts to perform reconnaissance on domains, IP addresses, and more.

---

## 🚀 Features

- **WHOIS Lookup**: Retrieve WHOIS information about domains or IP addresses.
- **DNS Enumeration**: Perform DNS lookups and scan for common subdomains.
- **IP Geolocation**: Fetch IP address location details using a public API.
- **Shodan Scan**: Query the Shodan API for open ports, vulnerabilities, and service information.

---

## 📂 Project Structure

```
OSINTSLAYER/
│-- main.py                # CLI interface to run the toolkit
│-- modules/
│   ├── whois_lookup.py    # WHOIS lookup module
│   ├── dns_enum.py        # DNS enumeration module
│   ├── ip_geo.py          # IP geolocation module
│   └── shodan_scan.py     # Shodan integration module
│-- requirements.txt       # List of dependencies
└-- README.md              # Project documentation
```

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Darackkk/OSINTSLAYER.git
   cd OSINTSLAYER
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧪 Usage

Run the toolkit using the command-line interface:

```bash
python main.py
```

You will see the following menu:

```
--- OSINTSLAYER ---
1. WHOIS Lookup
2. DNS Enumeration
3. IP Geolocation
4. Shodan Scan (requires API key)
5. Exit
```

### **Example Usage**

1. **WHOIS Lookup**:  
   Enter a domain (e.g., `example.com`) or IP address.  
2. **DNS Enumeration**:  
   Input a domain to retrieve DNS records and common subdomains.  
3. **IP Geolocation**:  
   Provide an IP address to fetch location details.  
4. **Shodan Scan**:  
   Input an IP/domain and provide a valid **Shodan API Key** to retrieve open ports and vulnerabilities.

---

## 🌐 Dependencies

This project requires the following libraries:

- `requests` - For HTTP requests (IP geolocation and APIs)
- `dnspython` - DNS lookups and subdomain checks
- `python-whois` - WHOIS information retrieval
- `shodan` - Shodan API integration

Install them via the requirements file:
```bash
pip install -r requirements.txt
```

---

## 🔑 Shodan API Key  

To use the **Shodan Scan** module, sign up at [Shodan.io](https://shodan.io) and generate your API key.  
Place the API key when prompted in the CLI.

---

## ✨ Future Improvements

- Add support for reverse DNS lookups.
- Integrate email breach checks using HaveIBeenPwned API.
- Develop a web-based interface for the toolkit.

---

## 👤 Author
Developed by **VOLVES**  
GitHub: [Darackkk](https://github.com/Darackkk)

---

## ✨ License
This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it!
>>>>>>> 35b1d79 (README changed)
