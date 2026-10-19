import socket
import sounddevice
import numpy as np
import os

# github : https://github.com/spiritofthenight

IP = "127.0.0.1" # reolace it with your own device's IP

# leave the below port number as it is or replace it with your desired port number 
PORT = 5000 # (be sure to check your firewall since firewalls may block ports for incoming UDP packets !) 


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


print("Reciever started, waiting for audio...")

def main():
    count_down = 1800
    print("\napp is running on ", IP, ":", PORT, "...\n")
    while True:
        try:
            samplerate = 48000
            data, addr = UDP_socket.recvfrom(4096)

            pcm16 = np.frombuffer(data, dtype=np.int16)

            audio = pcm16.astype(np.float32) / 32767

            stream.write(audio)

            print("type audio is: ", type(audio))
            print("Audio is: ", audio)
            count_down -= 1
            if count_down <= 0:
                clear()
                count_down = 1800

        except KeyboardInterrupt as k:
            print("exited ! ", k)
            break
            
        except Exception as e:
            print("Error: ", e)
            break


if __name__ == "__main__":
    main()
