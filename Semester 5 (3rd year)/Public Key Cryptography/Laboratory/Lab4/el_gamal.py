import random
from sympy import isprime, primerange

# Define the alphabet
alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def generate_keys():
    # Choose a large prime number p
    primes = list(primerange(1000, 5000))
    p = random.choice(primes)

    # Choose g, a primitive root modulo p
    g = random.choice(range(2, p - 1))

    # Choose a private key x
    x = random.choice(range(2, p - 1))

    # Compute the public key y
    y = pow(g, x, p)

    # Public key (p, g, y) and private key x
    return (p, g, y), x

def encrypt(plaintext, public_key):
    p, g, y = public_key
    k = random.choice(range(2, p - 1))
    C1 = pow(g, k, p)
    encrypted_msg = []
    for char in plaintext:
        # Validate the character
        if char not in alphabet:
            raise ValueError("Invalid character in plaintext.")
        m = alphabet.index(char)
        C2 = (m * pow(y, k, p)) % p
        encrypted_msg.append((C1, C2))
    return encrypted_msg

def decrypt(encrypted_msg, private_key, public_key):
    p, _, _ = public_key
    plaintext = ''
    for C1, C2 in encrypted_msg:
        m = (C2 * pow(C1, p - 1 - private_key, p)) % p
        plaintext += alphabet[m]
    return plaintext


def main():
    public_key, private_key = generate_keys()

    plaintext = "HELLO WORLD"
    encrypted_msg = encrypt(plaintext, public_key)
    decrypted_msg = decrypt(encrypted_msg, private_key, public_key)

    print(f"Original Message: {plaintext}")
    print(f"Encrypted Message: {encrypted_msg}")
    print(f"Decrypted Message: {decrypted_msg}")


if __name__ == "__main__":
    main()