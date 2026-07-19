"""Check whether a number is prime."""


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def is_prime(number):
    if number < 2:
        return False

    for divisor in range(2, number):
        if number % divisor == 0:
            return False

    return True


def main():
    print("Welcome to the prime number checker!")
    number = get_integer("Enter a whole number: ")

    if is_prime(number):
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")


if __name__ == "__main__":
    main()