import hashlib

# Get input from the user
text = input("Enter text to hash: ")

# Create an MD5 hash object
md5_hash = hashlib.md5()

# Update the hash object with the bytes of the text
md5_hash.update(text.encode())

# Get the hexadecimal digest
digest = md5_hash.hexdigest()

# Print the result
print("MD5 hash:", digest)