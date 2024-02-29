import socket


def pickWinner(first, second):
    if first == second:
        return 0
    if first == '1' and second == '3' or first == '2' and second == '1' or first == '3' and second == '2':
        return 1
    return 2


def connectClients(server, clients: list):
    while len(clients) < 2:
        clientSocket, clientAddress = server.accept()
        print(f"Connected to {clientAddress}")
        clients.append(clientSocket)


def rockPaperScissors(server, clients: list):
    scores = [0, 0]
    while True:
        clients[0].send("The game is starting... ARE YOU READY?!?".encode())
        clients[1].send("The game is starting... ARE YOU READY?!?".encode())
        clients[0].send(f"Pick your weapon:\n"
                        f"1. Rock\n"
                        f"2. Paper\n"
                        f"3. Scissors".encode())
        clients[1].send(f"Pick your weapon:\n"
                        f"1. Rock\n"
                        f"2. Paper\n"
                        f"3. Scissors".encode())
        firstClient = clients[0].recv(1024).decode().strip()
        secondClient = clients[1].recv(1024).decode().strip()

        if firstClient=="1":
            print("Player 1 picked rock.")
        elif firstClient=="2":
            print("Player 1 picked paper.")
        else:
            print("Player 1 picked scissors.")

        if secondClient=="1":
            print("Player 2 picked rock.")
        elif firstClient=="2":
            print("Player 2 picked paper.")
        else:
            print("Player 2 picked scissors.")

        if pickWinner(firstClient, secondClient) == 0:
            clients[0].send("It's a draw!".encode())
            clients[1].send("It's a draw!".encode())
            print("It's a draw!")
        elif pickWinner(firstClient, secondClient) == 1:
            clients[0].send("You won!".encode())
            clients[1].send("You lost!".encode())
            print("Player 1 won!")
            scores[0] += 1
        else:
            clients[0].send("You lost!".encode())
            clients[1].send("You won!".encode())
            print("Player 2 won!")
            scores[1] += 1

        print(f"The score is {scores[0]} - {scores[1]}!")
        for client in clients:
            client.send(f"The score is {scores[0]} - {scores[1]}!\n Type 'yes' to keep playing".encode())
            response = client.recv(1024).decode().strip()

            if response.lower() != 'yes':
                clients[0].send(f"Game over! Final score: {scores[0]} - {scores[1]}".encode())
                clients[1].send(f"Game over! Final score: {scores[0]} - {scores[1]}".encode())
                server.close()
                exit()


HOST = '192.168.10.209'
PORT = 42069
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)
clients = []

connectClients(server, clients)
rockPaperScissors(server, clients)
