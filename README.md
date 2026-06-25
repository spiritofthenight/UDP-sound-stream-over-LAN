# UDP Sound Stream Over LAN + end to end ecryption

This project allows you to stream your computer's sound output over a UDP socket on your LAN. It is a simple UDP server/client implementation:

- `UDP_server.py`: Streams your computer's sound output in real-time over your LAN.
- `UDP_client.py`: Receives the audio stream from another device running Python.
- `encUDP_server.py`: Encrypt with a encryption key and streams your computer's sound output in real-time over your LAN.
- `UDP_client.py`: Receives the encrypted audio stream from another device and decrypts it on your device with encryption key and stream .

This project demonstrates how UDP sockets work in practice.


**if you want a simple tool, use :**
- UDP_server.py
- UDP_client.py

**if you want to stream your sound with end to end encryption, use :**
- encUDP_server.py
- UDP_client.py

**Important notes:**

 *written in python 3.12*

- Modify the IP and PORT addresses in `UDP_server.py` and `UDP_client.py` to match your devices' actual IP/PORT numbers.
- Modify the IP, PORT address and user_key (encryption key) in `encUDP_server.py` and `encUDP_client.py` to match your devices' actual IP/PORT numbers.
- This tool is for educational purposes only dont use it on other people's PC without contest.

if you want a simple and clean GUI version of this app you can check my other repo :
"https://github.com/spiritofthenight/UDP-sound-stream-over-LAN-GUI/"
