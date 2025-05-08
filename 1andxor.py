# Define the input string
input_string = "Hello World"

# Apply AND and XOR operations with 127
and_results = [ord(char) & 127 for char in input_string]
xor_results = [ord(char) ^ 127 for char in input_string]

# Display results
print("Original String:", input_string)
print("AND with 127:", ' '.join(map(str, and_results)))
print("XOR with 127:", ' '.join(map(str, xor_results)))
