# Open the binary file in read-binary mode
with open('latin.markov', 'rb') as file:
    # Read the entire file into a bytes object
    data = file.read()

# Convert the bytes to a hexadecimal string
hex_data = data.hex()

# Print the hexadecimal string
print(hex_data)