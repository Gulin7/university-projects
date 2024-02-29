import socket
import random

HOST = '192.168.10.209'
PORT = 42069


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        startMessage = client.recv(1024).decode()
        print(startMessage)
        if 'ARE YOU READY' not in startMessage:
            break
        message = client.recv(1024).decode()

        weapon = '0'
        if 'weapon' in message:
            print(message)
            randomNumber = random.randint(1,3)
            weapon = str(randomNumber)
            if weapon=='1':
                print('You got rock')
            elif weapon=='2':
                print('You got paper')
            else:
                print('You got scissors')
            #weapon = input('Enter your weapon: ')

        client.send(weapon.encode())
        message2 = client.recv(1024).decode()
        print(message2)
        message3 = client.recv(1024).decode()
        print(message3)
        client.send("yes".encode())

    client.close()


main()
