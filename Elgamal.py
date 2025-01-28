//Implement Elgamal Cryptosystem//
import random

# Function to compute modular exponentiation (base^exponent % modulus)
def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)

# Key generation for ElGamal
def elgamal_keygen(p, g):
    d = random.randint(2, p - 2)  # Private key (d)
    e1 = mod_exp(g, d, p)  # Public key (e1)
    return d, e1

# ElGamal encryption function
def elgamal_encrypt(p, g, e1, m):
    r = random.randint(2, p - 2)  # Random number r (for one-time use)
    c1 = mod_exp(g, r, p)  # c1 = g^r % p
    c2 = (m * mod_exp(e1, r, p)) % p  # c2 = m * e1^r % p
    return c1, c2

# ElGamal decryption function
def elgamal_decrypt(p, d, c1, c2):
    # Compute the modular inverse of c1^d % p
    s = mod_exp(c1, d, p)  # c1^d % p
    s_inv = mod_exp(s, p - 2, p)  # Modular inverse of s % p using Fermat's Little Theorem
    m = (c2 * s_inv) % p  # m = c2 * (s^-1) % p
    return m

# Example usage
p = 467  # Large prime number p (chosen for simplicity)
g = 2    # Primitive root g modulo p

# Key generation
d, e1 = elgamal_keygen(p, g)

print(f"Private key (d): {d}")
print(f"Public key (e1): {e1}")

# Encrypting a message m
m = 123  # Example message (could be an integer)
c1, c2 = elgamal_encrypt(p, g, e1, m)

print(f"Ciphertext: (c1 = {c1}, c2 = {c2})")

# Decrypting the message
decrypted_m = elgamal_decrypt(p, d, c1, c2)

print(f"Decrypted message: {decrypted_m}")


//Sample Output//
Private key (d): 72
Public key (e1): 64
Ciphertext: (c1 = 93, c2 = 291)
Decrypted message: 123
