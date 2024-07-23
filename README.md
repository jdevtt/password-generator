# Password Generator and Manager

This Python-based Password Generator and Manager helps users create strong, secure passwords and store them safely in a file.

## Features

- Generate strong passwords with customizable length
- Store passwords securely using a master password
- Retrieve stored passwords
- List all stored services
- Simple command-line interface

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository: git clone https://github.com/jdevtt/passwordmanager.git
2. Navigate to the project directory: cd passwordmanager

## Usage

Run the script using Python: python password_manager.py

Follow the prompts to:
1. Set a master password
2. Generate new passwords
3. Add passwords for different services
4. Retrieve stored passwords
5. List all stored services

## Security Notes

- Passwords are stored in a local JSON file
- The master password is hashed using SHA-256
- This is a basic implementation and may not be suitable for storing highly sensitive information
- For production use, consider implementing additional security measures


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.


