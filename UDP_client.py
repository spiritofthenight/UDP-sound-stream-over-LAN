import socket
import os
import time

def clear():
    if os.name == 'nt':
        os.system("cls")
    elif os.name == 'posix':
        os.system("clear")
    else:
        pass

def main():
    UDP_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    IP = "127.0.0.1"
    PORT = 5000
    print("\n app is running on ", IP,":", PORT, "...\n")
    count_down = 60
    while True:
        try:
            msg = input("> ")
            UDP_socket.sendto(msg.encode(), (IP, PORT))
            data, addr = UDP_socket.recvfrom(1024)
            print("Echo:", data.decode())
            time.sleep(0.5)
            count_down -= 1
            if count_down <= 0:
                clear()
                count_down = 30

        except KeyboardInterrupt as k :
            print("\nyou exited the app with keyboard interruption !", k)
            break
        
        except Exception as e:
            print("we ran into a error : ", e)
            break

if __name__ == "__main__":
    main()
