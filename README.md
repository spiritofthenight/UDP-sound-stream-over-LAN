# UDP Sound Stream Over LAN + End-to-end Encryption

This project allows you to stream your computer's sound output over a UDP socket on your LAN. It is a simple UDP server/client implementation:

- `UDP_server.py`: Streams your computer's sound output in real-time over your LAN.
- `UDP_client.py`: Receives the audio stream from another device running Python.
- `encUDP_server.py`: Encrypts with an encryption key and streams your computer's sound output in real-time over your LAN.
- `UDP_client.py`: Receives the encrypted audio stream from another device and decrypts it on your device with the encryption key.

This project demonstrates how UDP sockets work in practice.

**If you want a simple tool, use:**
- `UDP_server.py`
- `UDP_client.py`

**If you want to stream your sound with end-to-end encryption, use:**
- `encUDP_server.py`
- `UDP_client.py`

**Important notes:**
*Written in Python 3.12*

- Modify the IP and PORT addresses in `UDP_server.py` and `UDP_client.py` to match your devices' actual IP/PORT numbers.
- Modify the IP, PORT address, and `user_key` (encryption key) in `encUDP_server.py` and `encUDP_client.py` to match your devices' actual IP/PORT numbers.
- This tool is for educational purposes only. Don't use it on other people's PCs without consent.

If you want a simple and clean GUI version of this app, check my other repo:
"https://github.com/spiritofthenight/UDP-sound-stream-over-LAN-GUI/"
