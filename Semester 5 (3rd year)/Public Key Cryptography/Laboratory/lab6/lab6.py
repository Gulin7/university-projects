import random
import hashlib

# Alphabet configuration
ALPHABET = " abcdefghijklmnopqrstuvwxyz"
ALPHABET_SIZE = len(ALPHABET)


def validate_plaintext(plaintext):
    for char in plaintext:
        if char not in ALPHABET:
            raise ValueError(f"Invalid character '{char}' in plaintext. Only characters from the alphabet are allowed.")


def validate_ciphertext(ciphertext):
    if len(ciphertext) != 4 or not isinstance(ciphertext[2], list):
        raise ValueError("Invalid ciphertext format. Ciphertext must be a tuple of (u1, u2, e_list, v).")

# Utility functions
def mod_exp(base, exp, mod):
    """Modular exponentiation: (base^exp) % mod."""
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def hash_values(u1, u2, e):
    """Compute a hash value combining u1, u2, and e."""
    data = f"{u1}{u2}{e}".encode()
    return int(hashlib.sha256(data).hexdigest(), 16)

# Key generation
def generate_keys():
    """Generate public and private keys for the Cramer-Shoup cryptosystem."""
    p = 467  # A large prime number
    q = 233  # A smaller prime divisor of p - 1
    g1 = random.randint(2, p - 1)
    g2 = random.randint(2, p - 1)

    x1 = random.randint(1, q - 1)
    x2 = random.randint(1, q - 1)
    y1 = random.randint(1, q - 1)
    y2 = random.randint(1, q - 1)
    z = random.randint(1, q - 1)

    c = (mod_exp(g1, x1, p) * mod_exp(g2, x2, p)) % p
    d = (mod_exp(g1, y1, p) * mod_exp(g2, y2, p)) % p
    h = mod_exp(g1, z, p)

    public_key = (p, g1, g2, c, d, h)
    private_key = (x1, x2, y1, y2, z)
    return public_key, private_key

# Encryption
def encrypt(public_key, plaintext):
    """Encrypt the plaintext using the public key."""
    p, g1, g2, c, d, h = public_key

    # Validate the plaintext
    validate_plaintext(plaintext)

    # Convert plaintext to numeric representation
    plaintext_numeric = [ALPHABET.index(char) for char in plaintext.lower() if char in ALPHABET]

    # Random r
    r = random.randint(1, p - 1)

    # Compute u1, u2, and e
    u1 = mod_exp(g1, r, p)
    u2 = mod_exp(g2, r, p)
    e = [(mod_exp(h, r, p) * char) % p for char in plaintext_numeric]

    # Compute hash and v
    alpha = hash_values(u1, u2, str(plaintext_numeric)) % p

    v = (mod_exp(c, r, p) * mod_exp(d, r * alpha, p)) % p

    return (u1, u2, e, v, plaintext_numeric)

# Decryption
def decrypt(private_key, ciphertext, public_key):
    """Decrypt the ciphertext using the private key."""
    x1, x2, y1, y2, z = private_key
    p, g1, g2, c, d, h = public_key
    u1, u2, e, v, plaintext_numeric = ciphertext

    # Validate the cypertext
    validate_ciphertext(ciphertext[:-1])

    # Compute alpha
    alpha = hash_values(u1, u2, str(plaintext_numeric)) % p
    #print ("alpha:", alpha)

    # Validate v
    v_prime = (mod_exp(u1, x1 + alpha * y1, p) * mod_exp(u2, x2 + alpha * y2, p)) % p

    if v != v_prime:
        raise ValueError("Ciphertext validation failed.")

    # Decrypt each character in e
    plaintext_numeric = [(char * mod_exp(u1, p - 1 - z, p)) % p for char in e]

    # Convert numeric representation back to plaintext
    plaintext = ''.join(ALPHABET[char] for char in plaintext_numeric)
    return plaintext

# Example usage
def main():
    # Generate keys
    public_key, private_key = generate_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    # Plaintext input
    plaintext = "hello!"
    print("Plaintext:", plaintext)

    # Encrypt
    ciphertext = encrypt(public_key, plaintext)
    print("Ciphertext:", ciphertext)

    # Decrypt
    decrypted_text = decrypt(private_key, ciphertext, public_key)
    print("Decrypted Text:", decrypted_text)



if _name_ == "_main_":
    main()