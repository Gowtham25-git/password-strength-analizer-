import socket
from datetime import datetime

print("=" * 50)
print("      SIMPLE VULNERABILITY SCANNER")
print("=" * 50)

target = input("Enter Target IP Address: ").strip()

# Common ports to scan
ports = [
    21,    # FTP
    22,    # SSH
    23,    # Telnet
    25,    # SMTP
    53,    # DNS
    80,    # HTTP
    110,   # POP3
    143,   # IMAP
    443,   # HTTPS
    445,   # SMB
    3306,  # MySQL
    3389,  # RDP
    8080   # Alternative HTTP
]

# Vulnerability knowledge base
vulnerabilities = {
    21: {
        "service": "FTP",
        "risk": "Credentials may be transmitted without encryption.",
        "level": "HIGH",
        "recommendation": "Use SFTP or FTPS instead."
    },

    22: {
        "service": "SSH",
        "risk": "Brute-force attacks may target SSH services.",
        "level": "LOW",
        "recommendation": "Use key-based authentication and strong passwords."
    },

    23: {
        "service": "Telnet",
        "risk": "Traffic is transmitted in plaintext.",
        "level": "HIGH",
        "recommendation": "Disable Telnet and use SSH."
    },

    25: {
        "service": "SMTP",
        "risk": "Mail server may be abused if improperly configured.",
        "level": "MEDIUM",
        "recommendation": "Configure relay restrictions and monitor logs."
    },

    53: {
        "service": "DNS",
        "risk": "DNS information leakage may occur.",
        "level": "MEDIUM",
        "recommendation": "Restrict unnecessary DNS queries."
    },

    80: {
        "service": "HTTP",
        "risk": "Web traffic is not encrypted.",
        "level": "MEDIUM",
        "recommendation": "Redirect users to HTTPS."
    },

    110: {
        "service": "POP3",
        "risk": "Email credentials may be exposed if encryption is absent.",
        "level": "MEDIUM",
        "recommendation": "Use secure email protocols."
    },

    143: {
        "service": "IMAP",
        "risk": "Unencrypted email communication may occur.",
        "level": "MEDIUM",
        "recommendation": "Use IMAPS or TLS."
    },

    443: {
        "service": "HTTPS",
        "risk": "Generally secure when properly configured.",
        "level": "LOW",
        "recommendation": "Keep TLS certificates and software updated."
    },

    445: {
        "service": "SMB",
        "risk": "File-sharing services are frequent attack targets.",
        "level": "HIGH",
        "recommendation": "Disable SMB if not required and patch regularly."
    },

    3306: {
        "service": "MySQL",
        "risk": "Database exposure may lead to data compromise.",
        "level": "HIGH",
        "recommendation": "Restrict database access and use strong credentials."
    },

    3389: {
        "service": "RDP",
        "risk": "Remote Desktop services are common brute-force targets.",
        "level": "HIGH",
        "recommendation": "Use VPN, MFA, and strong passwords."
    },

    8080: {
        "service": "HTTP Alternate",
        "risk": "Web applications may expose additional services.",
        "level": "MEDIUM",
        "recommendation": "Review exposed applications and secure them."
    }
}

open_ports = []

print(f"\nScanning Target: {target}")
print("-" * 50)

start_time = datetime.now()

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        sock.close()

    except socket.error:
        print(f"[ERROR] Unable to scan port {port}")

end_time = datetime.now()

print("\n" + "=" * 50)
print("           VULNERABILITY REPORT")
print("=" * 50)

if not open_ports:
    print("No common open ports detected.")

else:
    for port in open_ports:

        info = vulnerabilities.get(
            port,
            {
                "service": "Unknown Service",
                "risk": "Unknown",
                "level": "Unknown",
                "recommendation": "Investigate manually."
            }
        )

        print(f"\nPort: {port}")
        print(f"Service: {info['service']}")
        print(f"Risk Level: {info['level']}")
        print(f"Risk: {info['risk']}")
        print(f"Recommendation: {info['recommendation']}")

print("\n" + "=" * 50)
print("SCAN SUMMARY")
print("=" * 50)
print(f"Target: {target}")
print(f"Open Ports Found: {len(open_ports)}")
print(f"Scan Started: {start_time}")
print(f"Scan Finished: {end_time}")

# Save report to file
filename = "vulnerability_report.txt"

with open(filename, "w") as report:

    report.write("SIMPLE VULNERABILITY SCANNER REPORT\n")
    report.write("=" * 50 + "\n")
    report.write(f"Target: {target}\n")
    report.write(f"Scan Started: {start_time}\n")
    report.write(f"Scan Finished: {end_time}\n\n")

    if not open_ports:
        report.write("No common open ports detected.\n")

    else:
        for port in open_ports:

            info = vulnerabilities.get(
                port,
                {
                    "service": "Unknown Service",
                    "risk": "Unknown",
                    "level": "Unknown",
                    "recommendation": "Investigate manually."
                }
            )

            report.write(f"Port: {port}\n")
            report.write(f"Service: {info['service']}\n")
            report.write(f"Risk Level: {info['level']}\n")
            report.write(f"Risk: {info['risk']}\n")
            report.write(
                f"Recommendation: {info['recommendation']}\n"
            )
            report.write("-" * 40 + "\n")

print(f"\nReport saved as '{filename}'")
print("Scan Completed Successfully")