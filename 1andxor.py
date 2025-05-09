s = "Hello World"

print("AND with 127:")
for c in s:
    result = ord(c) & 127
    print(f"{c} & 127 = {result}")

print("\nXOR with 127:")
for c in s:
    result = ord(c) ^ 127
    print(f"{c} ^ 127 = {result}")
