#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

#define HOST "192.168.10.209"
#define PORT 42069

void flushInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

int main() {
    int clientSocket;
    struct sockaddr_in serverAddress;
    char buffer[1024];

    clientSocket = socket(AF_INET, SOCK_STREAM, 0);
    if (clientSocket == -1) {
        fprintf(stderr, "Failed to create socket\n");
        return 1;
    }

    serverAddress.sin_family = AF_INET;
    serverAddress.sin_port = htons(PORT);
    if (inet_pton(AF_INET, HOST, &(serverAddress.sin_addr)) <= 0) {
        fprintf(stderr, "Invalid address/Address not supported\n");
        return 1;
    }

    if (connect(clientSocket, (struct sockaddr *)&serverAddress, sizeof(serverAddress)) < 0) {
        fprintf(stderr, "Connection failed\n");
        return 1;
    }

    while (1) {
        memset(buffer, 0, sizeof(buffer));
        if (recv(clientSocket, buffer, sizeof(buffer), 0) <= 0) {
            fprintf(stderr, "Failed to receive start message\n");
            break;
        }
        char *startMessage = buffer;
        printf("%s\n", startMessage);
        if (strstr(startMessage, "ARE YOU READY") == NULL) {
            break;
        }

        memset(buffer, 0, sizeof(buffer));
        if (recv(clientSocket, buffer, sizeof(buffer), 0) <= 0) {
            fprintf(stderr, "Failed to receive start message\n");
            break;
        }
        char *endMessage = buffer;
        printf("%s\n", endMessage);

        memset(buffer, 0, sizeof(buffer));
        if (recv(clientSocket, buffer, sizeof(buffer), 0) <= 0) {
            fprintf(stderr, "Failed to receive message\n");
            break;
        }
        char *message = buffer;
        printf("%s\n", message);

        if (strstr(message, "Pick your weapon:") != NULL) {
            char weapon[2];
            printf("Enter your weapon (1 for Rock, 2 for Paper, 3 for Scissors): ");
            fflush(stdout);
            fgets(weapon, sizeof(weapon), stdin);
            weapon[strcspn(weapon, "\n")] = 0; // Remove the newline character

            // Send the chosen weapon to the server
            if (send(clientSocket, weapon, strlen(weapon), 0) < 0) {
                fprintf(stderr, "Failed to send weapon\n");
                break;
            }
        }
    }

    close(clientSocket);
    return 0;
}
