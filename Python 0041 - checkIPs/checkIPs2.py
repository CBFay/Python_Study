# A more succinct solution
# Created 12.28.2017 by CB Fay

import ipaddress

def answer(address):
    try:
        addr = ipaddress.ip_address(address)
        if type(addr) == ipaddress.IPv4Address:
            return 'IPv4'
        if type(addr) == ipaddress.IPv6Address:
            return 'IPv6'
    except ValueError:
        return 'Neither'
    
print(answer('192.168.1.67'))
