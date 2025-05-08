def encrypt_transposition(plaintext, key):
    """
    Encrypts plaintext using a transposition cipher with the given key (number of columns).
    """
    ciphertext = [''] * key

    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)


def decrypt_transposition(ciphertext, key):
    """
    Decrypts ciphertext using a transposition cipher with the given key (number of columns).
    """
    num_of_rows = key
    num_of_cols = len(ciphertext) // key
    num_of_shaded_boxes = (num_of_rows * num_of_cols) - len(ciphertext)

    plaintext = [''] * num_of_cols
    col = 0
    row = 0

    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1

        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)


# Example Usage
if __name__ == "__main__":
    message = "Hello World"
    message = message.replace(" ", "")  # remove spaces and capitalize
    key = 2

    print(f"Original Message: {message}")

    encrypted = encrypt_transposition(message, key)
    print(f"Encrypted Message: {encrypted}")

    decrypted = decrypt_transposition(encrypted, key)
    print(f"Decrypted Message: {decrypted}")

