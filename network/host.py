#!/usr/bin/env python3

import os
import socket
import sys
import json
import time
from wol_magic_packet import MagicPacket  # Import MagicPacket
from ip_neigh import get_ip_neighbours  # Import get_ip_neighbours

class Host:
    def __init__(self, address=None, hostname=None):
        self.address = address
        self.hostname = hostname
        if self.hostname:
            self.address = socket.gethostbyname(self.hostname)
        if self.address:
            self.hostname = socket.gethostbyname(self.address)
        self.mac_address = self.get_mac_address()

    def get_mac_address(self):
        neighbours = json.loads(get_ip_neighbours())
        for neighbour in neighbours:
            if neighbour['dst'] == self.address:
                return neighbour['lladdr']
        return None

    def ping(self):
        response = os.system(f"ping -c 1 {self.address}")
        return response == 0
    
    def arping(self):
        response = os.system(f"sudo arping -c 1 {self.address}")
        return response == 0

    def get_hostname(self):
        try:
            hostname = socket.gethostbyaddr(self.address)[0]
            return hostname
        except socket.herror:
            return None

    def wake_up(self, mac_address=None):
        if mac_address is None:
            mac_address = self.mac_address
        if mac_address is None:
            raise ValueError("MAC address is not available")
        magic_packet = MagicPacket(mac_address)
        magic_packet.send_packet(self.address)

def get_hostname_or_ip():
    if len(sys.argv) > 1:
        host_input = sys.argv[1]
    else:
        host_input = input("Enter a hostname or IP address: ")
    return host_input

if __name__ == "__main__":
    # Get hostname or IP address from user input
    host = Host(get_hostname_or_ip())

    print(f"Hostname: {host.hostname}")
    print(f"IP Address: {host.address}")
    print(f"MAC address: {host.mac_address}")

    pingable = host.ping()
    arp_pingable = host.arping()

    print(f"Host {host.address} is {'reachable' if pingable else 'not reachable'} via ping.")
    print(f"Host {host.address} is {'reachable' if arp_pingable else 'not reachable'} via arping.")
    if not pingable and arp_pingable:
        print("Trying to wake up the host")
        host.wake_up()  # Wake up the host using the provided or detected MAC address
        print("Waiting 5 seconds for the host to wake up...")
        time.sleep(5)
        print("Try again to ping the host.")
        pingable = host.ping()
        print(f"Host {host.address} is now {'reachable' if pingable else 'not reachable'} via ping.")


