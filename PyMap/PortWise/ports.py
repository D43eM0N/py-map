def _ports(port: int) -> str:
    
    servives = {
        53: "dns",
        80: "http",
        443: "https",
        21: "ftp",
        22: "ssh",
        25: "smtp",
        110: "pop3",
        135: "ms-rce",
        143: "imap",
        139: "smb",
        587: "secure-smtp",
        67: "dhcp",
        23: "telnet",
        69: "tftp",
        123: "ntp",
        161: "snmp",
        137: "net-bios",
        445: "smb",
        389: "ldap",
        636: "ldaps",
        500: "isakmp",
        514: "syslog",
        903: "vmrc",
        913: "apex-edge",
        993: "imaps",
        995: "pop3s"
    }
    return servives.get(port, "unknown-service")
    
