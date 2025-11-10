
import re
import bcrypt
import os


USER_DATA_FILE = "users.txt"


def hash_password(plain_text_password):
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
    # TODO: Encode both the plaintext password and the stored hash to byt
    password_bytes = plain_text_password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    # TODO: Use bcrypt.checkpw() to verify the password
    match = bcrypt.checkpw(password_bytes, hashed_password)
    # This function extracts the salt from the hash and compares
    return match


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


def user_exists(username):
    # TODO: Handle the case where the file doesn't exist yet
    try:
        with open(USER_DATA_FILE, "r"):
            pass
    except FileNotFoundError:
        with open(USER_DATA_FILE, "w"):
            pass
# TODO: Read the file and check each line for the username
    finally:
        username = username.strip()
        with open(USER_DATA_FILE, "r") as f:
            for line in f:
                existing_username = line.split(",")[0]
                if existing_username == username:
                    return True
    return False


def register_user(username, password):
    # TODO: Check if the username already exists
    if user_exists(username) == True:
        return print(f"The user {username} already exist.")
    # TODO: Hash the password
    hashed_str = hash_password(password)

    # TODO: Append the new user to the file
    with open(USER_DATA_FILE, "a") as f:
        f.write(f"{username},{hashed_str}\n")
    # Format: username,hashed_password
    return print(f"The user {username} succesfully registered!")


def login_user(username, password):
    # TODO: Handle the case where no users are registered yet
    with open(USER_DATA_FILE, "r") as f:
        user = f.read()
        if not user:
            return print("No users are registered.")
# TODO: Search for the username in the file
    with open(USER_DATA_FILE, "r") as f:
        for line in f:
            existing_username = line.split(",")[0]
            if existing_username == username:
                # TODO: If username matches, verify the password
                existing_password = line.split(",")[1].strip()
                if verify_password(password, existing_password):
                    return print("The user logged in successfully.")
                else:
                    return print("Invalid password.")
# TODO: If we reach here, the username was not found
        return print(f"No user named {username} found.")


def validate_username(username):
    username = username.strip()

    if len(username) < 3:
        return False, "The username has to be more then 5 characters."
    if not username.isalnum():
        return False, "The username has to contain only letters and numbers."
    if len(username) > 20:
        return False, "The username has to be 20 characters long at most."
    return True, "The username is correct."


def validate_password(password):
    if len(password) < 8:
        return False,  "The password must contain 8 characters at least."
    if not re.search(r"[A-Z]", password):
        return False, "The password must contain at least one upper letter."
    if not re.search(r"[a-z]", password):
        return False, "The password must contain at least one lower letter."
    if not re.search(r"\d", password):
        return False, "The password must contain at least one number."
    if not re.search(r"[!@#$%^&*(),.?/\"':{}|<>]", password):
        return False, "The password must contain at least one special character."

    return True, "Password is strong"


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
    while True:
        display_menu()
        choice = input("\nPlease select an option (1-3): ").strip()
        if choice == '1':
            # Registration flow
            print("\n--- USER REGISTRATION ---")
            username = input("Enter a username: ").strip()
    # Validate username
            is_valid, error_msg = validate_username(username)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue
            password = input("Enter a password: ").strip()
    # Validate password
            is_valid, error_msg = validate_password(password)
            if not is_valid:
                print(f"Error: {error_msg}")
                continue
# Confirm password
            password_confirm = input("Confirm password: ").strip()
            if password != password_confirm:
                print("Error: Passwords do not match.")
                continue
# Register the user
            register_user(username, password)
        elif choice == '2':
            # Login flow
            print("\n--- USER LOGIN ---")
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
# Attempt login
            if login_user(username, password):
                print("\nYou are now logged in.")
                print("(In a real application, you would now access the ...")
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
