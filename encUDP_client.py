import os
import socket
import sounddevice
import numpy as np

from cryptography.fernet import Fernet
import base64, hashlib

# github : https://github.com/spiritofthenight

IP = "192.168.1.100" # replace it with your own device's IP

# leave the below port number as it is or replace it with your desired port number 
PORT = 5000 # (be sure to check your firewall since firewalls may block ports for incoming UDP packets !) 

user_key = "my user key" # enter your encryption key here

samplerate = 48000

UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_socket.bind((IP, PORT))

stream = sounddevice.OutputStream(samplerate=samplerate, channels=1, dtype='float32')

stream.start()

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

print("Reciever started, waiting for audio...")

# *** UNcomment next lines I marked for you if you want log output ; I commented them out for better performance and better latancy ***


def main():
    #count_down = 200                                                                                                                                   # * Uncomment
    print("\napp is running on ", IP, ":", PORT, "...\n")
    while True:
        try:
            samplerate = 48000
            fernet = Fernet(kdf_key(user_key))

            data, addr = UDP_socket.recvfrom(65507)

            packet_plain = fernet.decrypt(data)

            pcm16 = np.frombuffer(packet_plain, dtype=np.int16)

            audio = pcm16.astype(np.float32) / 32767
            stream.write(audio)

            #print("\naudio type is: ", type(audio), "\n\ndata is :", type(data), "\n\n\npacket plain: ", packet_plain, "\n\nencrypted data: ", data)    # * Uncomment
            #print("type audio is: ", type(audio))                                                                                                       # * Uncomment                                                                                                                  
            #print("streaming...")                                                                                                                       # * Uncomment
            #count_down -= 1                                                                                                                             # * Uncomment
            #if count_down <= 0:                                                                                                                         # * Uncomment
               # clear()                                                                                                                                 # * Uncomment
                #count_down = 200                                                                                                                        # * Uncomment

        except KeyboardInterrupt as k:
            print("exited ! ", k)
            break
            
        except Exception as e:
            print("Error: ", e)
            break


if __name__ == "__main__":
    main()
