"""ARP Scanner."""
import click
from scapy import all as sc
from scapy import config as conf

conf.verb = 0

@click.option('--ip', required=True, multiple=True, type=(str))
@click.command('arp')
def scan_local_network(ip):
    """Scan local network.

    Pass as many parameters as you want.

    Note:
        `IP` in the ``Args`` section is console `stdin`.

    Args:
        ip (Tuple[str]): Destintaion IP
    """
    ether_layer = sc.Ether(dst='ff:ff:ff:ff:ff:ff')

    for address in ip:
        arp_layer = sc.ARP(pdst=address)
        arp_request = ether_layer / arp_layer

        answered = sc.srp(arp_request, timeout=10)[0]

        if answered:
            click.echo(f'{address} | available')
        else:
            click.echo(f'{address} | not available')


if __name__ == '__main__':
    scan_local_network()
    zero_division = lambda a, b: a / b
    print(zero_division(0, 5))

