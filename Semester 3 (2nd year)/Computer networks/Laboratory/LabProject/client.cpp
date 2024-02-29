#include <iostream>
#include <string>
#include <cstring>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <cstdlib>

#define HOST "192.168.10.209"
#define PORT 42069

int main() {
    int clientSocket;
    struct sockaddr_in serverAddress;
    char buffer[1024];

    // Create socket
    clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == -1) {
        std::cerr << "Failed to create socket" << std::endl;
        return 1;
    }

    // Set server address
    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(PORT);
    if (inet_pton(AF_INET, HOST, &(serverAddress.sin_addr)) <= 0) {
        std::cerr << "Invalid address/Address not supported" << std::endl;
        return 1;
    }

    // Connect to server
    if (connect(clientSocket, (struct sockaddr *)&serverAddress, sizeof(serverAddress)) < 0) {
        std::cerr << "Connection failed" << std::endl;
        return 1;
    }

    while (true) {
        // Receive start message
        memset(buffer, 0, sizeof(buffer));
        if (recv(clientSocket, buffer, sizeof(buffer), 0) <= 0) {
            std::cerr << "Failed to receive start message" << std::endl;
            break;
        }
        std::string startMessage(buffer);
        std::cout << startMessage << std::endl;

        if (startMessage.find("ARE YOU READY") == std::string::npos) {
            break;
        }

        // Receive message
        memset(buffer, 0, sizeof(buffer));
        if (recv(clientSocket, buffer, sizeof(buffer), 0) <= 0) {
            std::cerr << "Failed to receive message" << std::endl;
            break;
        }
        std::string message(buffer);

        std::string weapon = "0";
        if (message.find("weapon") != std::string::npos) {
            std::cout << message << std::endl;
            //std::cout << "Enter your weapon: ";
            //std::cin >> weapon;
            int weap = rand()%3;
            if(weap==0){
            	weapon="1";
            	std::cout<<"You got rock!\n";
            }
            else if(weap==1){
            	weapon="2";
            	std::cout<<"You got paper!\n";
            }
            else{
            	weapon="3";
            	std::cout<<"You got scissors!\n";
            }
        }

        // Send weapon
        if (send(clientSocket, weapon.c_str(), weapon.length(), 0) < 0) {
            std::cerr << "Failed to send weapon" << std::endl;
            break;
        }

        // Receive message2
        memset(buffer, 0, sizeof(buffer));
        if (recv(clientSocket, buffer, sizeof(buffer), 0) <= 0) {
            std::cerr << "Failed to receive message2" << std::endl;
            break;
        }
        std::string message2(buffer);
        std::cout << message2 << std::endl;

        // Receive message3
        memset(buffer, 0, sizeof(buffer));
        if (recv(clientSocket, buffer, sizeof(buffer), 0) <= 0) {
            std::cerr << "Failed to receive message3" << std::endl;
            break;
        }
        std::string message3(buffer);
        std::cout << message3 << std::endl;

        // Send play again option
        std::cout << "Do you want to play again?: ";
        std::string playAgain;
        std::cin >> playAgain;
        if (send(clientSocket, playAgain.c_str(), playAgain.length(), 0) < 0) {
            std::cerr << "Failed to send play again option" << std::endl;
            break;
        }
    }

    close(clientSocket);
    return 0;
}
