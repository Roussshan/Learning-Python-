# List Operations Program
# This program demonstrates common list operations and manipulations

numbers = []
print("=== List Operations ===")

# Add numbers to the list
print("\nEnter 5 numbers:")
for i in range(5):
    num = int(input(f"Number {i+1}: "))
    numbers.append(num)

# Display the list
print(f"\nOriginal list: {numbers}")

# Sum and average
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}")
print(f"Average: {average}")

# Find minimum and maximum
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")

# Sort the list
sorted_numbers = sorted(numbers)
print(f"Sorted (ascending): {sorted_numbers}")
print(f"Sorted (descending): {sorted(numbers, reverse=True)}")

# Count occurrences
target = int(input("\nEnter a number to count in the list: "))
count = numbers.count(target)
print(f"The number {target} appears {count} times in the list")
