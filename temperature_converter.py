"""Convert a temperature from Celsius to Fahrenheit."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    print("Welcome to the temperature converter!")

    celsius = get_number("Enter temperature in Celsius: ")
    fahrenheit = celsius_to_fahrenheit(celsius)

    print()
    print("Celsius:", celsius)
    print("Fahrenheit:", fahrenheit)


if __name__ == "__main__":
    main()