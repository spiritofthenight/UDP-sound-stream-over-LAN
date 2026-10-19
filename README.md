# UDP Sound Stream Over LAN + End-to-end Encryption

This project allows you to stream your computer's sound output over a UDP socket on your LAN. It is a simple UDP Transmitter/Receiver implementation:

- `UDP_transmitter.py`: Streams your computer's sound output in real-time over your LAN.
- `UDP_receiver.py`: Receives the audio stream from another device running Python.
- `encUDP_transmitter.py`: Encrypts with an encryption key and streams your computer's sound output in real-time over your LAN.
- `encUDP_receiver.py`: Receives the encrypted audio stream from another device and decrypts it on your device with the encryption key.

This project demonstrates how UDP sockets work in practice.

**If you want a simple tool without encryption, use:**
- `UDP_transmitter.py`
- `UDP_receiver.py`

**If you want to stream your sound with end-to-end encryption, use:**
- `encUDP_transmitter.py`
- `encUDP_receiver.py`

**Important notes:**
*Written in Python 3.12*

- Modify the IP and PORT addresses in `UDP_transmitter.py` and `UDP_receiver.py` to match your devices' actual IP/PORT numbers.
- Modify the IP, PORT address, and `user_key` (encryption key) in `encUDP_transmitter.py` and `encUDP_receiver.py` to match your devices' actual IP/PORT numbers.
- This tool is for educational purposes only. Don't use it on other people's PCs without consent.

If you want a simple and clean GUI version of this app, check my other repo:

"https://github.com/spiritofthenight/UDP-sound-stream-over-LAN-GUI/"
