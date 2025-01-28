//Implement Vigenere Cipher//
# Function to encrypt the plaintext using Vigenère cipher
def vigenere_encrypt(plaintext, key):
    ciphertext = []
    key = key.upper()  # Ensure the key is in uppercase
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char.isalpha():  # Only encrypt alphabetic characters
            # Convert to uppercase and find numeric equivalent
            char_num = ord(char.upper()) - ord('A')
            key_num = ord(key[key_index % key_length]) - ord('A')
            # Apply the Vigenère encryption formula
            encrypted_char = (char_num + key_num) % 26
            # Convert back to a character
            ciphertext.append(chr(encrypted_char + ord('A')))
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext.append(char)
    
    return ''.join(ciphertext)

# Function to decrypt the ciphertext using Vigenère cipher
def vigenere_decrypt(ciphertext, key):
    plaintext = []
    key = key.upper()  # Ensure the key is in uppercase
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char.isalpha():  # Only decrypt alphabetic characters
            # Convert to uppercase and find numeric equivalent
            char_num = ord(char.upper()) - ord('A')
            key_num = ord(key[key_index % key_length]) - ord('A')
            # Apply the Vigenère decryption formula
            decrypted_char = (char_num - key_num + 26) % 26
            # Convert back to a character
            plaintext.append(chr(decrypted_char + ord('A')))
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            plaintext.append(char)
    
    return ''.join(plaintext)

# Example usage:
key = "KEY"
plaintext = "HELLO WORLD"
ciphertext = vigenere_encrypt(plaintext, key)
decrypted_text = vigenere_decrypt(ciphertext, key)

print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted Text: {decrypted_text}")


//Sample Output//
Plaintext: HELLO WORLD
Ciphertext: RIJVS UYVJN
Decrypted Text: HELLO WORLD
