
import secrets
import re
import bcrypt
import os
import time
from pathlib import Path

USER_DATA_PATH = Path("DATA").resolve()
USER_DATA_FILE = USER_DATA_PATH / "users.txt"



def hash_password(plain_text_password):
    """Returns a hashed password, created from plain text password."""
# TODO:Encode the password to bytes (bcrypt requires byte strings)
    password_bytes = plain_text_password.encode('utf-8')
# TODO: Generate a salt using bcrypt.gensalt()
    salt = bcrypt.gensalt()
# TODO: Hash the password using bcrypt.hashpw()
    hashed_password = bcrypt.hashpw(password_bytes, salt)
# TODO: Decode the hash back to a string to store in a text file
    hashed_str = hashed_password.decode('utf-8')
    return hashed_str


def verify_password(plain_text_password, hashed_password):
    """It returns True, if password matches and False, if not."""
    # TODO: Encode both the plaintext password and the stored hash to byt
    password_bytes = plain_text_password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    # TODO: Use bcrypt.checkpw() to verify the password
    match = bcrypt.checkpw(password_bytes, hashed_password)
    # This function extracts the salt from the hash and compares
    return match


"""
# TEMPORARY TEST CODE - Remove after testing
test_password = "SecurePassword123"
# Test hashing
hashed = hash_password(test_password)
print(f"Original password: {test_password}")
print(f"Hashed password: {hashed}")
print(f"Hash length: {len(hashed)} characters")
# Test verification with correct password
is_valid = verify_password(test_password, hashed)
print(f"\nVerification with correct password: {is_valid}")
# Test verification with incorrect password
is_invalid = verify_password("WrongPassword", hashed)
print(f"Verification with incorrect password: {is_invalid}")
"""


def user_exists(username):
    """Returns True, if a user exists in a database and False, if not."""
    # TODO: Handle the case where the file doesn't exist yet
    try:
        with open(USER_DATA_FILE, "r"):
            pass
    except FileNotFoundError:
        with open(USER_DATA_FILE, "w"):
            pass
# TODO: Read the file and check each line for the username
    finally:
        # striping username
        username = username.strip()
        with open(USER_DATA_FILE, "r") as f:
            # loop for checking if the user is in the database
            for line in f:
                existing_username = line.split(",")[0]
                if existing_username == username:
                    return True
    return False


def register_user(username, password):
    """Returns if the user has been registered."""
    # TODO: Check if the username already exists
    if user_exists(username) == True:
        return False, print(f"The user {username} already exists.")
    # TODO: Hash the password
    hashed_str = hash_password(password)

    role = input("Please enter a role of this user:")

    # TODO: Append the new user to the file
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{hashed_str}, {role}\n")
    # Format: username,hashed_password
    return True, print(f"The user {username} succesfully registered!")


def login_user(username, password):
    """Returns if the has been registered successfully."""
    # TODO: Handle the case where no users are registered yet
    try:
        with open(USER_DATA_FILE, "r") as f:
            user = f.read()
            if not user:
                return False, print("No users are registered.")
    except FileNotFoundError:
        return "No users are registered."
    # TODO: Search for the username in the file
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            existing_username = line.split(",")[0]
            if existing_username == username:
                # TODO: If username matches, verify the password
                existing_password = line.split(",")[1].strip()
                if verify_password(password, existing_password):
                    print("The user logged in successfully.")
                    return True
                else:
                    print("Invalid password.")
                    return False
    # TODO: If we reach here, the username was not found
        print(f"No user named {username} was not found.")
        return False


def validate_username(username):
    """Returns if the username is valid."""
    # striping the username
    username = username.strip()
    # checking the username
    if len(username) < 3:
        return False, "Your username is to short. The username has to be more then 2 characters."
    if not username.isalnum():
        return False, "Your username contain special characters. The username has to contain only letters and numbers."
    if len(username) > 20:
        return False, "Your username is to long. The username has to be 20 characters long at most."
    return True, "The given username is valid."


def validate_password(password):
    """Returns if the password is valid."""
    if len(password) < 8:
        return False,  "The password must contain 8 characters at least."
    if len(password) >= 24:
        return False, "The password must contain 24 characters at most."
    if not re.search(r"[A-Z]", password):
        return False, "The password must contain at least one upper letter."
    if not re.search(r"[a-z]", password):
        return False, "The password must contain at least one lower letter."
    if not re.search(r"\d", password):
        return False, "The password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?/\"':{}|<>]", password):
        return False, "The password must contain at least one special character."

    return True, "Password is strong"


def check_password_strength(password):
    """Returns how strong the password is(weak, medium, strong)."""
    # Implement logic based on:
    # creating variable to store score for password strenght
    score = 0
    # - Length
    # checking length
    if len(password) > 16:
        if len(password) > 20:
            score += 10
        else:
            score += 5

    # creating variables for checking what characters are in the password
    numb = 0
    sc = 0
    ul = 0
    # - Presence of uppercase, lowercase, digits, special characters
    # counting how many of each characters are in the password
    for digit in password:
        if digit.isdigit():
            numb += 1
        if digit.isupper():
            ul += 1
        if not digit.alnum():
            sc += 1

    # adding to score based on each character variable value
    if numb > 2:
        score += 10
    if sc > 1:
        score += 10
    if ul > 2:
        score += 10

# - Common password patterns
    common_passwords = [
        "Password1!",
        "Welcome123!",
        "Admin@123",
        "Qwerty123!",
        "Summer2024!",
        "Winter2023@",
        "HelloWorld1!",
        "Test@1234",
        "ILoveYou2!",
        "Sunshine@9",
        "Abc12345!",
        "Football2025#",
        "London2024$",
        "Chocolate1!",
        "MyPass@123",
        "Secure123#",
        "HappyDay7@",
        "Dragon99!",
        "Freedom#22",
        "Monkey@88",
        "StarLight7!",
        "Galaxy2025!",
        "BlueSky@11",
        "Rainbow#123"
    ]

    # checking if password match one of the most common ones
    for item in common_passwords:
        if password == item:
            return False, "Your password is one of the most used. Try another."

    if score >= 25:
        return True, "Strong password"
    elif score >= 10:
        return True, "Medium password"
    else:
        return True, "Weak password"


def create_session(username):
    """Returns token for the user."""
    token = secrets.token_hex(16)
    # Store token with timestamp
    return token


def display_menu():
    """Displays the main menu options."""
    print("\n" + "="*50)
    print(" MULTI-DOMAIN INTELLIGENCE PLATFORM")
    print(" Secure Authentication System")
    print("="*50)
    print("\n[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-"*50)


def main():
    """Main program loop."""
    print("\nWelcome to the Week 7 Authentication System!")
    # variables for counting login attempts
    login_count = 0
    wait_time = 0

    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()

        if choice == '1':

            while True:
                # Registration flow
                print("\n--- USER REGISTRATION ---")
                username = input("Enter a username: ").strip()
        # Validate username
                is_valid, error_msg = validate_username(username)
                if not is_valid:
                    print(f"Error: {error_msg}")
                    continue
                else:
                    break

            while True:
                password = input("Enter a password: ").strip()
            # Validate password
                is_valid, error_msg = validate_password(password)
                if not is_valid:
                    print(f"Error: {error_msg}")
                    continue
                else:
                    break
            while True:
                # Confirm password
                password_confirm = input("Confirm password: ").strip()
                if password != password_confirm:
                    print("Error: Passwords do not match.")
                    continue
                else:
                    # Register the user
                    if not register_user(username, password):
                        print(register_user(username, password))
                        break
                    else:
                        break

        elif choice == '2':
            while True:
                if login_count < 3:
                    login_count += 1
                    # Login flow
                    print("\n--- USER LOGIN ---")
                    username = input("Enter your username: ").strip()
                    password = input("Enter your password: ").strip()
                    # Attempt login
                    if login_user(username, password):
                        create_session(username)
                        print("\nYou are now logged in.")
                        print("(In a real application, you would now access the ...")
                        break
                    else:
                        continue
                else:
                    print("You attempted to login 3 times unsuccessfully. Wait for 5 minutes to try again.")
                    wait_time = time.time() + 5 * 60
                    count = 0
                    while True:
                        if wait_time > time.time():
                            wait_min = (wait_time - time.time()) // 60
                            wait_sec = (wait_time - time.time()) % 60
                            if count == 0:
                                wait_sec = 0
                                wait_min = 5
                                count = 1
                                input(f"Please wait for another {wait_min:.0f} minutes and {wait_sec:.0f} seconds. Press enter after the timer reaches 0.")
                            else:
                                input(f"Please wait for another {wait_min:.0f} minutes and {wait_sec:.0f} seconds. Press enter after the timer reaches 0.")

                        else:
                            login_count = 0
                            break

# Optional: Ask if they want to logout or exit
                input("\nPress Enter to return to main menu...")

        elif choice == '3':
            # Exit
            print("\nThank you for using the authentication system.")
            print("Exiting...")
            break
        else:
            print("\nError: Invalid option. Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
