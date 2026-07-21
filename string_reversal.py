# String Reversal Program
# This program reverses a given string using different methods

# Method 1: Using slicing
string = input("Enter a string: ")
reversed_string = string[::-1]

print(f"Original string: {string}")
print(f"Reversed string: {reversed_string}")

# Method 2: Using a loop (for practice)
print("\nReversed using loop:")
reversed_by_loop = ""
for char in string:
    reversed_by_loop = char + reversed_by_loop
print(reversed_by_loop)
