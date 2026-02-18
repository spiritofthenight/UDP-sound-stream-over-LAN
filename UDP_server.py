import socket
import soundcard
import sounddevice
import numpy as np
import os

# github:
# https://github.com/spiritofthenight

def clear():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")
    else:
        pass

def main():
    UDP_socekt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    samplerate = 48000

    speaker = soundcard.default_speaker()
    loopback = soundcard.get_microphone(id=speaker.id, include_loopback=True)
    count_down = 1800

    with loopback.recorder(samplerate=samplerate) as mic:
        while True:
            audio = mic.record(numframes=1024)
            
            mono = audio.mean(axis=1)
            pcm16 =(mono * 32767).astype(np.int16)
            packet = pcm16.tobytes()

            print("audio type is: ", type(audio))
            print("audio is: ", audio)
            UDP_socekt.sendto(packet, ("127.0.0.1", 5000)) # replace it with the IP/PORT number of your destination device
            count_down -= 1
            if count_down <= 0:
                clear()
                count_down = 1800

if __name__ == "__main__":
    main()
