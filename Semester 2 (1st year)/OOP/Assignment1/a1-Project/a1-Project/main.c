#define _CRT_SECURE_NO_WARNINGS
#pragma warning(disable:4996)

#include <stdio.h>

void show_menu() {
	/*
	PRINTS THE MENU!
	*/
	printf("\n MENU \n");
	printf("1. Read sequences and find the current and global maxim.\n");
	printf("2. Determine the longest subsequence.\n");
	printf("0. Exit the application.\n");
}

int insideInterval(int lowerLimit, int upperLimit, int numberToCheck) {
	/*
	Checks if a number is inside an interval.
	*/
	if (numberToCheck >= lowerLimit && numberToCheck <= upperLimit)
		return 1;
	return 0;
}

int determineMaxim(int firstNumber, int secondNumber) {
	/*
	Returns the biggest out of 2 numbers.
	*/
	if (firstNumber > secondNumber)
		return firstNumber;
	return secondNumber;
}

int main() {

	int command = -1, startOfSubsequence = 1, endOfSubsequence = 1, givenVector[1001] = { 0 };
	int currentMaxim = -1, globalMaxim = -1;
	int upperLimit, lowerLimit, vectorLength, currentStartOfSequence = 1, currentEndOfSequence = 1;
	show_menu();
	while (command) {
		printf("\nEnter a command: ");
		scanf("%d", &command);
		if (command > 2 || command < 0) {
			printf("Invalid command!");
		}
		if (command == 0) {
			printf("You\'ve left the app!");
			break;
		}
		else if (command == 2) {
			printf("Enter the length of the vector: ");
			scanf("%d", &vectorLength);
			for (int index = 1; index <= vectorLength; index++) {
				printf("Enter a number: ");
				scanf("%d", &givenVector[index]);
			}
			printf("Enter a start of interval: ");
			scanf("%d", &lowerLimit);
			printf("Enter an end of interval: ");
			scanf("%d", &upperLimit);
			for (int index = 1; index <= vectorLength; index++) {
				if (!insideInterval(lowerLimit, upperLimit, givenVector[index])) { // We check if the number is not in the given interval
					if ((currentEndOfSequence - currentStartOfSequence) > (endOfSubsequence - startOfSubsequence)) {
						// if the number is not in the interval, then we check to see if the current interval is longer than the current longest
						startOfSubsequence = currentStartOfSequence;
						endOfSubsequence = currentEndOfSequence;
					}
					currentEndOfSequence = index + 1;
					currentStartOfSequence = index + 1;
				}
				else { // if the current number is inside the given interval, we update the currentEndOfSequence
					currentEndOfSequence = index;
				}
			}
			printf("The longest subsequence is between %d and %d", startOfSubsequence, endOfSubsequence);
		}
		else {
			int lastRead = 0;
			currentMaxim = -1;
			while (lastRead != -1) {
				printf("\nEnter a number: ");
				scanf("%d", &lastRead);
				// We read a number, then if that number is 0 we compare the global and current maxim to check which one is bigger and we print
				// the current maxim. We then make currentMaxim = -1 and proceed with reading the next sequence
				if (lastRead == 0) {
					globalMaxim = determineMaxim(globalMaxim, currentMaxim);
					printf("The current maxim is %d", currentMaxim);
					currentMaxim = -1;
				}// if the lastRead is not 0 nor -1 then we just check to see if it's bigger than the currentMaxim
				else if (lastRead != -1) {
					currentMaxim = determineMaxim(currentMaxim, lastRead);
				}
				else if (lastRead == -1) {
					printf("The maxim of the current sequence is %d.", currentMaxim);
					globalMaxim = determineMaxim(globalMaxim, currentMaxim);
				}
			}
			printf("\nThe global maxim is %d", globalMaxim);
		}
	}
	return 0;
}