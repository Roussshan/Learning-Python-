"""Find the largest number from three numbers."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def find_largest(first_number, second_number, third_number):
    largest = first_number

    if second_number > largest:
        largest = second_number

    if third_number > largest:
        largest = third_number

    return largest


def main():
    print("Welcome to the largest number finder!")

    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")
    third_number = get_number("Enter the third number: ")

    largest = find_largest(first_number, second_number, third_number)

    print()
    print("The numbers are:", first_number, second_number, third_number)
    print("The largest number is:", largest)


if __name__ == "__main__":
    main()