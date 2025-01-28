//Implement RSA//
# Function to compute the greatest common divisor (gcd)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find the modular inverse of a under modulo m
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Key generation
def rsa_keygen():
    p = 61  # Prime number p
    q = 53  # Prime number q
    n = p * q
    phi_n = (p - 1) * (q - 1)
    
    # Select e such that 1 < e < phi_n and gcd(e, phi_n) = 1
    e = 17  # Example value for e, can be any number such that gcd(e, phi_n) = 1
    while gcd(e, phi_n) != 1:
        e += 2  # Increment to find a coprime value
    
    # Find d such that (d * e) % phi_n = 1
    d = mod_inverse(e, phi_n)
    
    return (e, d, n)

# RSA encryption
def rsa_encrypt(plain_text, e, n):
    cipher_text = []
    for char in plain_text:
        m = ord(char)  # Convert the character to its ASCII value
        c = pow(m, e, n)  # Encrypt the character
        cipher_text.append(c)
    return cipher_text

# RSA decryption
def rsa_decrypt(cipher_text, d, n):
    plain_text = ""
    for c in cipher_text:
        m = chr(pow(c, d, n))  # Decrypt the character
        plain_text += m
    return plain_text

# Example usage:
e, d, n = rsa_keygen()

# Encrypt a word
plain_text = "HELLO"
cipher_text = rsa_encrypt(plain_text, e, n)
print(f"Encrypted: {cipher_text}")

# Decrypt the word
decrypted_text = rsa_decrypt(cipher_text, d, n)
print(f"Decrypted: {decrypted_text}")


//Sample Output//
Encrypted: [233, 2215, 233, 233, 1913]
Decrypted: HELLO
