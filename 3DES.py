from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_text = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_text)
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_padded = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_padded, DES.block_size)
    return plaintext.decode()

if __name__ == "__main__":
    key = get_random_bytes(8)  # DES key must be 8 bytes
    plaintext = "Hello DES Encryption!"
    print(f"Original Text: {plaintext}")
    print(f"Key (hex): {key.hex()}")

    encrypted = des_encrypt(plaintext, key)
    print(f"Encrypted (hex): {encrypted.hex()}")

    decrypted = des_decrypt(encrypted, key)
    print(f"Decrypted Text: {decrypted}")
    