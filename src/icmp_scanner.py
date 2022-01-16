"""ARP Scanner."""
import asyncio
import logging

import click
from scapy import all as sc
from scapy import config as conf

conf.verb = 0
logger = logging.getLogger(__name__)


@click.command('arp')
@click.option('--quiet', default=False, is_flag=True)
@click.option('-t', '--target', required=True, type=str)
async def scan_local_network(target):
    """
    Scan local network.

    Args:
        target (str): Destintaion IP
    """
    arp_layer = sc.ARP(pdst=target)
    ether_layer = sc.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request = ether_layer / arp_layer

    answered, _ = sc.srp(arp_request, timeout=10)

    if answered:
        print(f'host {target} available')
        logger.setLevel(logging.INFO)
    else:
        print(f'host {target} not available')
        logger.setLevel(logging.ERROR)


if __name__ == '__main__':
    asyncio.run(scan_local_network())
