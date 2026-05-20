class GmailAccount:
    def __init__(self):
        self._name= None
        self._email = None
        self._password = None
        self._is_logged_in = False

    def create_account(self):
        self._name = input("Enter your name: ")

        while True:
            email = input("Enter your email: ")

            if not email.endswith("@gmail.com"):
                print("Please add '@gmail.com' to your email.")
                continue

            if email.count("@") != 1:
                print("Only one '@' is allowed.")
                continue
            break

        self._email = email
        self._password = input("Enter your password: ")

        print("Account created successfully.")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email == self._email and password == self._password:
            self._is_logged_in = True
            print("Login successful.")
        else:
            print("Invalid email or password.")
    
    def change_password(self):
        password = input("Enter your old password: ")
        if password == self._password:
            new_password = input("Enter your new password: ")
            self._password = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")

account = GmailAccount()
while True:

    if not account._is_logged_in:
        print("1. Create account")
        print("2. Login")
    else:
        print("3. Change password")
        print("4. Logout")

    choice = input("Choose: ")

    if choice == "1" and not account._is_logged_in:
        print("\n==== CREATE ACCOUNT ====")
        account.create_account()

    elif choice == "2" and not account._is_logged_in:
        print("\n==== LOGIN ====")
        account.login()

    elif choice == "3" and account._is_logged_in:
        print("\n==== CHANGE PASSWORD ====")
        account.change_password()

    elif choice == "4" and account._is_logged_in:
        account._is_logged_in = False
        print("Logged out successfully.")

    else:
        print("Invalid choice.")