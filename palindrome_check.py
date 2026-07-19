"""Check whether a word or sentence is a palindrome."""


def normalize_text(text):
    return "".join(character.lower() for character in text if character.isalnum())


def is_palindrome(text):
    cleaned_text = normalize_text(text)
    return cleaned_text == cleaned_text[::-1]


def main():
    print("Welcome to the palindrome checker!")
    text = input("Enter a word or sentence: ")

    if is_palindrome(text):
        print("It is a palindrome.")
    else:
        print("It is not a palindrome.")


if __name__ == "__main__":
    main()