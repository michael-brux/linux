#!/usr/env python3

# configure remote interpreter using SSH
# this script should be executed on the remote host

import socket
import os

print("Hello, World!")

hostname = socket.gethostname()
username = os.getlogin()

# should be from remote host
print(f"Hostname: {hostname}")
print(f"Username: {username}")