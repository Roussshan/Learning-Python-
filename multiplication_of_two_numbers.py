"""Multiply two numbers entered by the user."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    print("Welcome to the multiplication program!")

    first_number = get_number("Enter the first number: ")
    second_number = get_number("Enter the second number: ")

    product = first_number * second_number

    print()
    print("First number:", first_number)
    print("Second number:", second_number)
    print("Product:", product)


if __name__ == "__main__":
    main()