import random
from sympy import isprime, mod_inverse
from sympy.ntheory import nextprime


def generate_large_prime(bits):
    """Generate a large prime number of specified bit length."""
    while True:
        # Ensure the bit length is exactly `bits`
        prime = random.getrandbits(bits)
        # Ensure the prime is odd
        prime |= 1
        if isprime(prime):
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
    n = p * q
    inv_p = mod_inverse(p, q)
    inv_q = mod_inverse(q, p)

    roots = []
    for rp, rq in [(r1, r3), (r1, r4), (r2, r3), (r2, r4)]:
        m = (rp * q * inv_q + rq * p * inv_p) % n
        roots.append(m)
        roots.append(n - m)  # Include the negative root

    # Return unique plaintext candidates
    return list(set(roots))


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
