from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt(public_key, message):
    ciphertext = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext

def decrypt(private_key, ciphertext):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return plaintext.decode()

if __name__ == "__main__":
    message = "Hello RSA Encryption!"
    print(f"Original Message: {message}")

    # Generate RSA Keys
    private_key, public_key = generate_keys()

    # Encrypt
    encrypted_message = encrypt(public_key, message)
    print(f"Encrypted (hex): {encrypted_message.hex()}")

    # Decrypt
    decrypted_message = decrypt(private_key, encrypted_message)
    print(f"Decrypted Message: {decrypted_message}")
