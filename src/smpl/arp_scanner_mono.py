"""ARP Scanner."""
import click
from scapy import all as sc
from scapy import config as conf

conf.verb = 0


@click.option('--ip', required=True)
@click.command('arp')
def scan_local_network(ip):
    """
    Scan local network.

    Args:
        ip (str): Destintaion IP
    """
    arp_layer = sc.ARP(pdst=ip)
    ether_layer = sc.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request = ether_layer / arp_layer

    answered, _ = sc.srp(arp_request, timeout=10)

    if answered:
        print(f'host {ip} available')
    else:
        print(f'host {ip} not available')
