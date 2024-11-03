
"""
Hill cipher encryption algorithm for a 2x2 matrix
"""
def hillCipherEncrypt(plaintext, matrix):
    plaintext = plaintext.upper().replace(" ", "")
    plaintextLength = len(plaintext)

    ciphertext = ""

    for ind in range(0, plaintextLength, 2):
        result = plaintext[ind:ind+2]
        firstLetterOrd = ord(result[0]) - ord('A') + 1
        secondLetterOrd = ord(result[1]) - ord('A') + 1

        firstLetter = chr((firstLetterOrd * matrix[0][0] + secondLetterOrd * matrix[1][0]) % 27 + ord('A') - 1)
        secondLetter = chr((firstLetterOrd * matrix[0][1] + secondLetterOrd * matrix[1][1]) % 27 + ord('A') - 1)
        ciphertext += firstLetter + secondLetter

    return ciphertext

if __name__ == '__main__':
    # Get the matrix and its inverse
    a11 = int(input("Enter int a11: "))
    a12 = int(input("Enter int a12: "))
    a21 = int(input("Enter int a21: "))
    a22 = int(input("Enter int a22: "))
    matrix = [[a11, a12], [a21, a22]]

    # Get the plaintext
    plaintext = input("Enter the plaintext to encrypt: ")

    # Perform encryption
    ciphertext = hillCipherEncrypt(plaintext, matrix)
    print("Ciphertext:", ciphertext)
