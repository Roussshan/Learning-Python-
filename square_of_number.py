"""Calculate the square of a number entered by the user."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate_square(number):
    return number**2


def main():
    print("Welcome to the square calculator!")

    number = get_number("Enter a number: ")
    square = calculate_square(number)

    print()
    print("Number:", number)
    print("Square:", square)


if __name__ == "__main__":
    main()
