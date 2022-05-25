"""Scapy tutorial."""
from smpl import arp_scanner_mono as ascan

def main():
    """General function for all."""
    print('I will rule them all')
    # 1. `scsmpl.main()`
    # add desired IP via `--ip`
    ascan.scan_local_network()


if __name__ == '__main__':
    main()

