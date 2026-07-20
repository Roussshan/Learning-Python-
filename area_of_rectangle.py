"""Calculate the area of a rectangle."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate_area(length, width):
    return length * width


def main():
    print("Welcome to the rectangle area calculator!")

    length = get_number("Enter the length: ")
    width = get_number("Enter the width: ")

    area = calculate_area(length, width)

    print()
    print("Length:", length)
    print("Width:", width)
    print("Area of the rectangle:", area)


if __name__ == "__main__":
    main()