import os
import socket
import soundcard
import sounddevice
import numpy as np
from cryptography.fernet import Fernet
import base64, hashlib

# github:
# https://github.com/spiritofthenight

def clear():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")
    else:
        pass


def kdf_key(user_key: str) -> bytes:
    d = hashlib.sha256(user_key.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(d)


def main():
    UDP_socekt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    samplerate = 48000

    speaker = soundcard.default_speaker()
    loopback = soundcard.get_microphone(id=speaker.id, include_loopback=True)

# *** UNcomment next lines I marked if you want log output ; I commented them out for better runtime performance and better latancy ***

    #count_down = 600

    with loopback.recorder(samplerate=samplerate) as mic:
        while True:
            audio = mic.record(numframes=1024)
            user_key = "my user key" # encryption key , replace this with your own encryption key
            fernet = Fernet(kdf_key(user_key))

            mono = audio.mean(axis=1)
            pcm16 =(mono * 32767).astype(np.int16)
            token = pcm16.tobytes()

            packet = fernet.encrypt(token)     # encrypt bytes (token)

            #print("audio type is: ", type(audio), "\npacket is :", type(packet), "\n", audio, "\n\npacket: ", packet)          # * Uncomment
            UDP_socekt.sendto(packet, ("192.168.1.100", 5000)) # replace it with the IP/PORT number of your destination device  # * Uncomment
            #count_down -= 1                                                                                                    # * Uncomment
            #if count_down <= 0:                                                                                                # * Uncomment
            #    clear()                                                                                                        # * Uncomment
            #    count_down = 600                                                                                               # * Uncomment

if __name__ == "__main__":
    main()
