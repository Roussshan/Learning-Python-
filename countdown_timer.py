"""Print a simple countdown from a given number to 1."""


def get_positive_integer(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("Welcome to the countdown timer!")

    start_number = get_positive_integer("Enter a starting number: ")

    print()
    for number in range(start_number, 0, -1):
        print(number)

    print("Liftoff!")


if __name__ == "__main__":
    main()