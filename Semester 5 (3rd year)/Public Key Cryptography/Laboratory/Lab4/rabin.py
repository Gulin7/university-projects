import random
from sympy import isprime, nextprime, mod_inverse


def generate_large_prime(bits):
    """Generate a large prime number of specified bit length."""
    prime = random.getrandbits(bits) | 1  # Ensure the prime candidate is odd
    while not isprime(prime):
        prime = nextprime(prime)
    return prime


def generate_keys(bits=512):
    """Generate public and private keys for the Rabin cryptosystem."""
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)

    # Ensure p and q are distinct
    while p == q:
        q = generate_large_prime(bits)

    n = p * q  # Public key
    return (n, p, q)  # Return public key (n) and private keys (p, q)


def encrypt(message, n):
    """Encrypt a message using the Rabin cryptosystem."""
    if message >= n:
        raise ValueError("Message must be less than n.")
    c = (message ** 2) % n  # Compute ciphertext
    return c


def decrypt(c, p, q):
    """Decrypt a ciphertext using the Rabin cryptosystem."""
    # Compute square roots modulo p and q
    r1 = pow(c, (p + 1) // 4, p)
    r2 = (p - r1) % p
    r3 = pow(c, (q + 1) // 4, q)
    r4 = (q - r3) % q

    # Use Chinese Remainder Theorem to combine results
    roots = [(r1, r3), (r1, r4), (r2, r3), (r2, r4)]
    plaintexts = []

    n = p * q
    for r_p, r_q in roots:
        # Solve using CRT
        m1 = (r_p + p * mod_inverse(p, q) * (r_q - r_p)) % n
        m2 = n - m1  # The negative root is also a valid solution
        plaintexts.extend([m1, m2])

    # Return the unique plaintext candidates
    return list(set(plaintexts))


def main():
    bits = 512  # Bit length for primes
    n, p, q = generate_keys(bits)

    message = 123456789  # Example message (must be less than n)
    print(f"Original Message: {message}")

    ciphertext = encrypt(message, n)
    print(f"Ciphertext: {ciphertext}")

    plaintexts = decrypt(ciphertext, p, q)
    print(f"Possible Decrypted Messages: {plaintexts}")

    # Verify if the original message is among the decrypted candidates
    if message in plaintexts:
        print("Decryption successful!")
    else:
        print("Decryption failed!")


if __name__ == "__main__":
    main()
