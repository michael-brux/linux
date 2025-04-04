#!/usr/bin/env python3

import subprocess
import json

def run_ip_show(command):
    result = subprocess.run(['ip', '-details', '-json', '-pretty', command, 'show'], capture_output=True, text=True)
    return json.loads(result.stdout)

def show_addr():
    return run_ip_show('addr')

def show_link():
    return run_ip_show('link')

def show_neigh():
    return run_ip_show('neigh')

def show_route():
    return run_ip_show('route')

if __name__ == "__main__":
    print()
    print("Link:", show_link())
    print()
    print("Neigh:", show_neigh())
    print()
    print("Route:", show_route())
    print()
    print("Addr:", show_addr())
    print()
