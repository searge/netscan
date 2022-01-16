"""Sample Scrapy requests."""
from scapy import all as sc


def main():
    """Sample requests."""
    ether = sc.Ether()
    ether.dst = 'ff:ff:ff:ff:ff:ff'

    # Detailed information
    sc.ls(ether)

    # More detailed information
    ether.show()
    ether.display()
