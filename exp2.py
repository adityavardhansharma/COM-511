# Input string
input_string = "Welcome to Python world"

# Count the number of alphabets
num_alphabets = sum(1 for char in input_string if char.isalpha())

# Extract characters in a specific range
start_index = 3
end_index = 10
extracted_characters = input_string[start_index:end_index]

# Check if the string is alphanumeric
is_alphanumeric = input_string.isalnum()

# Print the results
print("Number of alphabets:", num_alphabets)
print("Extracted characters:", extracted_characters)
print("Is alphanumeric:", is_alphanumeric)
