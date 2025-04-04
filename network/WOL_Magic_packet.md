# Wake-on-LAN Magic Packet

A **Magic Packet** is a special network frame (a small piece of data) specifically designed to trigger the Wake-on-LAN (WoL) feature in computers. Its sole purpose is to remotely turn on or wake up a computer over a network.

## Key Points

1. **Purpose**:
   - To initiate the Wake-on-LAN process and power up a target computer over the network.

2. **Structure**:
   - The "magic" part lies in its specific payload content:
     - It typically starts with 6 bytes of the value `FF` (hexadecimal), like `FF:FF:FF:FF:FF:FF`. This acts as a synchronization signal.
     - This is immediately followed by the MAC address of the target computer's network interface card (NIC), repeated 16 times consecutively.

3. **How it Works**:
   - The network card of the sleeping/powered-off computer remains partially powered, constantly listening for this specific Magic Packet sequence containing its own unique MAC address.

4. **Transmission**:
   - Magic Packets are usually sent as UDP broadcast packets over the local network (LAN). This ensures the packet reaches the target machine even if it doesn't currently have an IP address assigned.
   - Sending across different networks (WAN) is possible but often requires specific network configuration (like port forwarding).

5. **Requirements**:
   - For a Magic Packet to work, the target computer's hardware (motherboard BIOS/UEFI, network card) must support Wake-on-LAN, and the feature usually needs to be enabled in the BIOS/UEFI settings.

In short, a Magic Packet is a **specially formatted network message containing the target computer's MAC address, used to tell that computer's network card to wake the system up**.

## Sources
- [Wake-on-LAN Wikipedia](https://en.wikipedia.org/wiki/Wake-on-LAN)
