import random
import string
from itertools import cycle

def crypt(c_input, master_key, c_mode):
    c_mk = [ord(ch) for ch in master_key]
    if c_mode == 'encrypt':
        c_input = [ord(ch) for ch in c_input]
        cycled = cycle(c_mk)
        c_output = [ch + next(cycled) for ch in c_input]
        return c_output
    elif c_mode == 'encrypt':
        c_input = [int(x) for x in c_input.split(',')]
        cycled = cycle(c_mk)
        c_output = [ x if x >= 0 else 0 for x in [ch - next(cycled) for ch in c_input]]
        c_output = ''.join([chr(ch) for ch in c_output])
        return c_output
    else:
        pass

def preview_records(master_key):
    with open('vault.vt', 'r') as f:
        records = f.readline()

    records = [record.strip('\n') for record in records]

    for i in range(len(records)):
        records[i] = ' '. join([
            crypt(records[i].split()[0], master_key=master_key,
                  c_mode='decrypt'),
            crypt(records[i].split()[1], master_key=master_key,
                  c_mode='decrypt'),
            crypt(records[i].split()[2], master_key=master_key,
                  c_mode='decrypt')
        ])

        if len(records) == 0:
            print("\nUnfortunately there are no passwords in the Vault.")
            return False

        id_max_width = len(max([str(len(records)),"ID"]))
        separator = ' '
        platform_max_width = len(
            max([r.split()[0]for r in records] + ["PLATFORM"], key=len))
        login_max_width = len(
            max([r.split()[1] for r in records] + ["LOGIN"], key=len))
        password_max_width = len(
            max([r.split()[2] for r in records] + ["PASSWORD"], key=len))

        print("\n3. Preview stored passwords.")
        print("~" * (id_max_width + platform_max_width + login_max_width + password_max_width + 9))
        print("ID" + separator * (id_max_width - len("ID")),end=' | ')
        print("PLATFORM" + separator * (platform_max_width - len("PLATFORM")), end=' | ')
        print("LOGIN" + separator * (login_max_width - len("LOGIN")), end=' | ')
        print("PASSWORD" + separator * (password_max_width - len("PASSWORD")))

        iterator = 1
        for r in records:
            id = str(iterator) + separator * (id_max_width - len(str(iterator))) + '  |  '
            platform = r.split()[0] + separator * (
                    platform_max_width - len(r.split()[0])) + '  |  '
            login = r.split()[1] + separator * (
                    platform_max_width - len(r.split()[1])) + '  |  '
            password = r.split()[2] + separator * (
                    platform_max_width - len(r.split()[2]))

            line = id + platform + login + password
            print(line)
            iterator += 1

        print("~" * (id_max_width + platform_max_width + login_max_width + password_max_width + 9))



def store_password(master_key, password=None):
    prompt = [
        "Platform -> ",
        "Login -> ",
        "Password -> ",
        "Repeat password -> "
    ]
    if password is None:
        print("\nProvide platform, login and password you want to store.")
        str_platform = ''.join(input(prompt[0]).split())
        str_login = ''.join(input([1]).split())
        password = ''.join(input([2]).split())
    else:
        print(f"\nProvide platform and login for the following password: {password}")
        str_platform = ''.join(input(prompt[0]).split())
        str_login = ''.join(input([1]).split())

    encrypted = [
        ','.join([str(x) for x in
                  crypt(c_input=str_platform, master_key=master_key,
                        c_mode='encrypt')]),
        ','.join([str(x) for x in
                  crypt(c_input=str_login, master_key=master_key,
                        c_mode='encrypt')]),
        ','.join([str(x) for x in
                  crypt(c_input=password, master_key=master_key,
                        c_mode='encrypt')])
    ]

    str_line = ' '.join(x for x in encrypted)

    with open('vault.vt', 'a') as f:
        f.write(str_line + '\n')

        print("Record was added to the Vault!")


def input_as_digits(user_input, display_string, lower_thr, higher_thr):
    while True:
        if user_input.isdigit():
            if lower_thr <= int(user_input) <= higher_thr:
                return int(user_input)
            else:
                print("Invalid input, Try again.")
                user_input - input(display_string)
                continue
        else:
            print("Invalid input. Try again.")
            user_input = input(display_string)
            continue

def generate_new_password(master_key):
    print(
        "\n1.Generate new password."
        "\nHow many numbers, letters and special characters\n"
        "you want to include in a generated password?"
    )
    prompt = [
        "Numbers (from 0 to 10) -> ",
        "Letters (from 0 to 10) -> ",
        "Special characters ( from 0 to 10) -> ",
    ]
    while True:
        n_numbers = input_as_digits(input(prompt[0]), prompt[0], 0, 10 )
        n_letters = input_as_digits(input(prompt[1]), prompt[1], 0, 10)
        n_special_chars = input_as_digits(input(prompt[2]), prompt[2], 0, 10)

        str_numbers = ''.join([str(random.randint(0, 10)) for _ in range(n_numbers)])
        str_letters = ''.join([random.choice(string.ascii_letters) for _ in range(n_letters)])
        str_special_cahrs = ''.join([random.choice(string.punctuation)for _ in range(n_special_chars)])

        password = list(str_numbers + str_letters + str_special_cahrs)
        random.shuffle(password)
        password = ''.join(password)

        if password == '':
            password = 'None'

        print("\nGenerate password is:", password)
        print("What you want to do with it?")
        print(
            "1.Re-generate.\n"
            "2. Use it for storing a new records in the Vault. \n"
            "3. Discard and return to the manin menu."
        )

        user_input = input_as_digits(input("(1,2,3) -> "),"(1,2,3) -> ",1,3)

        if user_input == 1:
            print()
            continue
        elif user_input == 2:
            store_password(master_key, password)
            break
        else:
            break

def main_menu(master_key):
    while True:
        print(
            "\n------ Main Menu ------\n"
            "What you want to do?\n"
            "1. Generate new passwod.\n"
            "2. Store password.\n"
            "3. Preview stored passwords.\n"
            "4.Exit"
        )
        user_input = input("1/2/3/4) -> ")
        if user_input == '1':
            generate_new_password(master_key)
            continue
        elif user_input == '2':
            store_password(master_key)
            continue
        elif user_input == '3':
            preview_records(master_key)
            continue
        elif user_input == '4':
            print("Your passwords are safe with me! Have a nice day!")
            exit()
        else:
            print("Invalid input. Try again.")


print(
    "\n~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    "@@@@@     VAULT     @@@@@"
    "\n~~~~~~~~~~~~~~~~~~~~~~~~~~"
)

print("\nGreeting Master! Please provide the Master Key to proceed!")
master_key = input("Master Key -> ")
if master_key != "":
    main_menu(master_key)
else:
    print("No Key, no entry.")