import random
import string
import hashlib
import json
import getpass

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = self._hash_password(master_password)
        self.passwords = {}
        self.filename = "passwords.json"
        self.load_passwords()

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def generate_password(self, length=12):
        characters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(characters) for _ in range(length))

    def add_password(self, service, password):
        self.passwords[service] = password
        self.save_passwords()

    def get_password(self, service):
        return self.passwords.get(service, "Password not found.")

    def list_services(self):
        return list(self.passwords.keys())

    def save_passwords(self):
        with open(self.filename, 'w') as f:
            json.dump(self.passwords, f)

    def load_passwords(self):
        try:
            with open(self.filename, 'r') as f:
                self.passwords = json.load(f)
        except FileNotFoundError:
            self.passwords = {}

    def check_master_password(self, password):
        return self._hash_password(password) == self.master_password

def main():
    print("Welcome to the Password Generator and Manager!")
    master_password = getpass.getpass("Enter your master password: ")
    pm = PasswordManager(master_password)

    while True:
        print("\n1. Generate a new password")
        print("2. Add a password")
        print("3. Get a password")
        print("4. List all services")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            length = int(input("Enter password length: "))
            new_password = pm.generate_password(length)
            print(f"Generated password: {new_password}")
        elif choice == '2':
            service = input("Enter service name: ")
            password = getpass.getpass("Enter password: ")
            pm.add_password(service, password)
            print("Password added successfully!")
        elif choice == '3':
            service = input("Enter service name: ")
            password = pm.get_password(service)
            print(f"Password: {password}")
        elif choice == '4':
            services = pm.list_services()
            print("Services:")
            for service in services:
                print(f"- {service}")
        elif choice == '5':
            print("Thank you for using the Password Generator and Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
