def belasoCipherEncrypt(plaintext, keyword):
    plaintext = plaintext.upper().replace(" ", "")
    keyword = keyword.upper()

    encryptedText = ""
    keyLength = len(keyword)

    for i, letter in enumerate(plaintext):
        if letter.isalpha():
            letterShift = ord(keyword[i % keyLength]) - ord('A') + 1
            encryptedLetter = chr((ord(letter) - ord('A') + letterShift) % 27 + ord('A'))
            encryptedText += encryptedLetter
        else:
            encryptedText += letter

    return encryptedText

if __name__ == '__main__':
    plaintext = input("Enter the plaintext to encrypt: ")
    keyword = input("Enter the keyword: ")
    print(belasoCipherEncrypt(plaintext, keyword))
