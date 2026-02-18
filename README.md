# UDP Sound Stream Over LAN

This project allows you to stream your computer's sound output over a UDP socket on your LAN. It is a simple UDP server/client implementation:

- `UDP_server.py`: Streams your computer's sound output in real-time over your LAN.
- `UDP_client.py`: Receives the audio stream from another device running Python.

This project demonstrates how UDP sockets work in practice.

**Important notes:**
- Modify the IP and PORT addresses in `UDP_server.py` and `UDP_client.py` to match your devices' actual IP/PORT numbers.
- This tool is for educational purposes only.
