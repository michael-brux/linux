import socket

class MagicPacket:
    def __init__(self, mac_address: str):
        self.mac_address = mac_address

    def create_packet(self) -> bytes:
        # Remove any separators from the MAC address
        mac_address = self.mac_address.replace(":", "").replace("-", "").replace(".", "")
        
        # Ensure the MAC address is 12 hexadecimal digits
        if len(mac_address) != 12:
            raise ValueError("Invalid MAC address format")
        
        # Convert MAC address to bytes
        mac_bytes = bytes.fromhex(mac_address)
        
        # Create the magic packet
        packet = b'\xff' * 6 + mac_bytes * 16
        return packet

    def send_packet(self, target_address: str):
        packet = self.create_packet()
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(packet, (target_address, 9))

# Example usage:
# magic_packet = MagicPacket("00:11:22:33:44:55")
# packet = magic_packet.create_packet()
# print(packet)
# magic_packet.send_packet("192.168.1.255")
