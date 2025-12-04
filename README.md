A command-line password manager that encrypts and stores passwords securely using a master key.

Overview
Password Vault is a secure password management system that allows you to:

Generate strong, customizable passwords

Store encrypted credentials for different platforms

Retrieve and view stored passwords

All data is encrypted with a master key before storage

Features
AES-style Encryption: Custom encryption algorithm using a master key

Secure Storage: Passwords are encrypted before being written to disk

Password Generator: Create strong passwords with custom character sets

Organized Records: View stored passwords in a formatted table

Master Key Protection: All data requires the master key to access

Security Notice
⚠️ Important: This uses a custom encryption algorithm for educational purposes. For real-world password management, consider using established libraries like cryptography or professionally audited password managers.

Installation
Requirements:
Python 3.x

No external dependencies (uses built-in modules only)

Files:
password_vault.py - Main program file

vault.vt - Encrypted password storage file (created automatically)

How to Use
1. First Run
When you run the program for the first time:

text
~~~~~~~~~~~~~~~~~~~~~~~~~~
@@@@@     VAULT     @@@@@
~~~~~~~~~~~~~~~~~~~~~~~~~~

Greetings Master! Please provide the Master Key to proceed!
Master Key -> 
Enter a strong master key (remember this - it's required for all future access)

If you lose the master key, you cannot recover your passwords

2. Main Menu Options
Option 1: Generate New Password
text
How many numbers, letters and special characters
you want to include in a generated password?
Numbers (from 0 to 10) -> 
Letters (from 0 to 10) -> 
Special characters (from 0 to 10) -> 
Creates passwords with customizable character types

Options to: re-generate, store, or discard the password

Option 2: Store Password
text
Provide platform, login and password you want to store.
Platform -> 
Login -> 
Password -> 
Repeat password -> 
Manually enter credentials for storage

All data is encrypted with your master key

Option 3: Preview Stored Passwords
Displays all stored credentials in a formatted table:

text
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ID  |  PLATFORM         |  LOGIN       |  PASSWORD
1   |  example.com      |  user@email  |  P@ssw0rd!
2   |  bank.com         |  john_doe    |  Secure123#
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Option 4: Exit
Safely exits the program

Encryption Details
How It Works:
Master Key Processing: Converts master key characters to ASCII values

Stream Cipher: Uses the master key as a repeating key stream

Encryption: Adds key values to plaintext ASCII values

Decryption: Subtracts key values from ciphertext

Storage: Encrypted values are stored as comma-separated numbers

Example:
text
Plaintext: "hello"
Master Key: "key"
Encryption: h(104) + k(107) = 211, e(101) + e(101) = 202, etc.
Stored as: "211,202,216,216,215"
File Format
vault.vt Structure:
text
encrypted_platform encrypted_login encrypted_password
encrypted_platform encrypted_login encrypted_password
...
Each encrypted field is stored as comma-separated integers:

text
"211,202,216,216,215 198,203,215,219,200 215,198,203,202,216"
Code Structure
Main Functions:
crypt(c_input, master_key, c_mode)

Handles encryption/decryption

Modes: 'encrypt' or 'decrypt'

Uses cyclic key stream

generate_new_password(master_key)

Interactive password generator

Customizable character types and counts

store_password(master_key, password=None)

Stores encrypted credentials

Validates input and handles file operations

preview_records(master_key)

Decrypts and displays stored passwords

Formatted table output

main_menu(master_key)

Primary user interface

Navigation between features

Helper Functions:
input_as_digits(): Validates numeric input with range checking

Password complexity controls: Limits character counts (0-10 each)

Usage Examples
Example Session:
text
Master Key -> MySecretKey123

------ Main Menu ------
What you want to do?
1. Generate new password.
2. Store password.
3. Preview stored passwords.
4. Exit
1/2/3/4) -> 1

Generate new password.
How many numbers, letters and special characters
you want to include in a generated password?
Numbers (from 0 to 10) -> 3
Letters (from 0 to 10) -> 5
Special characters (from 0 to 10) -> 2

Generated password is: aB3#dE9!fG
What you want to do with it?
1. Re-generate.
2. Use it for storing a new record in the Vault.
3. Discard and return to the main menu.
(1,2,3) -> 2

Provide platform and login for the following password: aB3#dE9!fG
Platform -> example.com
Login -> myemail@example.com
Record was added to the Vault!
Security Best Practices
Master Key: Use a long, complex master key you can remember

Regular Backups: Keep backups of your vault.vt file

Local Storage: Keep the vault file on secure, encrypted storage

No Network: This is designed for local use only

Limitations
No password strength checking

No auto-fill or browser integration

No password sharing features

No cloud synchronization

Custom encryption (not industry-standard)

Extending the Vault
Potential enhancements:

Add password strength meter

Implement password expiration reminders

Add import/export functionality

Create a GUI interface

Add two-factor authentication

Implement password sharing (secure)

Troubleshooting
Common Issues:
"Invalid input" errors: Ensure you're entering numbers where required

Can't decrypt passwords: Verify you're using the correct master key

File not found: The program creates vault.vt automatically on first save

Empty vault: Use options 1 or 2 to add passwords first

Data Recovery:
If you lose your vault.vt file, all passwords are lost. If you forget your master key, passwords cannot be recovered.

License
Educational use only. Not recommended for storing sensitive real-world passwords without additional security measures.

Disclaimer
This tool is for educational purposes. The author is not responsible for lost passwords or security breaches. Always use professionally audited password managers for sensitive data.
