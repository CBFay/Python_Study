# A more succinct solution
# Created on 12.30.2017 by CB Fay

import ipaddress

def answer(addresses):
    results = []
    for x in addresses:
        try:
            addr = ipaddress.ip_address(x)
            if type(addr) == ipaddress.IPv4Address:
                results.append('IPv4')
            elif type(addr) == ipaddress.IPv6Address:
                results.append('IPv6')
        except ValueError:
            results.append('Neither')
    return results

# Test Case
a = '132.1.222.80'
b = '2001:0DBB:FA01:D33E:DB8:3333:93DA:3ED1'
c = '267.23.554.9'

print(answer([a, b, c]))
