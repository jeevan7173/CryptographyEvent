//Implement Affine cipher//
# Function to find modular inverse
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1

# Function to encrypt text using the Affine cipher
def affine_encrypt(plaintext, a, b):
    m = 26  # English alphabet size
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Only encrypt alphabetic characters
            # Convert to uppercase and find numeric equivalent
            x = ord(char.upper()) - ord('A')
            # Apply the encryption formula
            encrypted_char = (a * x + b) % m
            # Convert back to a letter
            ciphertext += chr(encrypted_char + ord('A'))
        else:
            ciphertext += char  # Non-alphabetic characters remain unchanged
    return ciphertext

# Function to decrypt text using the Affine cipher
def affine_decrypt(ciphertext, a, b):
    m = 26  # English alphabet size
    a_inv = mod_inverse(a, m)  # Find the modular inverse of a
    if a_inv == -1:
        return "Inverse of a doesn't exist, decryption impossible."
    
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            y = ord(char.upper()) - ord('A')
            # Apply the decryption formula
            decrypted_char = (a_inv * (y - b)) % m
            plaintext += chr(decrypted_char + ord('A'))
        else:
            plaintext += char  # Non-alphabetic characters remain unchanged
    return plaintext

# Example usage:
a = 5  # Multiplier key
b = 8  # Increment key
plaintext = "HELLO WORLD"
ciphertext = affine_encrypt(plaintext, a, b)
decrypted_text = affine_decrypt(ciphertext, a, b)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")


//Sample Output//
Plaintext: HELLO WORLD
Ciphertext: KHOOR ZRUOG
Decrypted Text: HELLO WORLD
