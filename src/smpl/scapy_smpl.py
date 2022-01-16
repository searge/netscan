"""Sample Scrapy requests."""
from scapy import all as sc


def main():
    """Sample requests."""
    ether = sc.Ether()
    ether.dst = 'ff:ff:ff:ff:ff:ff'

    # Detailed information
    sc.ls(ether)

    # For more detailed information
    # use this commands: `ether.show()` or `ether.display()`

    # Find MAC address via IP address
    mac_address = sc.ARP(pdst='10.0.0.8')

    # Gather two levels
    arp_request = ether / mac_address
    arp_request.show()
    print(arp_request.layers())
    print(arp_request.summary())

    # Sending & reciving requests
    arp_req_result = sc.srp(arp_request, timeout=10)
    answered, unanswered = arp_req_result

    response = answered[0]
    print(response.query, response.answer, sep='\n')

    response.answer.show()
