import re

def check_password_strength(password):
    """
    Function to check the strength of a password.
    Returns a string: Weak, Moderate, or Strong
    """

    # Length check
    length_error = len(password) < 8

    # Presence of uppercase, lowercase, digits, and special characters
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Count the number of errors
    errors = sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])

    if errors == 0:
        return "Strong"
    elif errors <= 2:
        return "Moderate"
    else:
        return "Weak"

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Your password strength is: {strength}")

if __name__ == "__main__":
    main()
