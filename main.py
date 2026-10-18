"""Generate a random password with the secrets module."""

import secrets
import string


def main():
    try:
        length = int(input("Password length (minimum 8): "))
        if length < 8:
            raise ValueError
    except ValueError:
        print("Enter a whole number of at least 8.")
        return
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    print("Generated password:", password)


if __name__ == "__main__":
    main()
