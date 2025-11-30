def input_error(func):
    """
    Декоратор для обробки типових помилок:
    KeyError, ValueError, IndexError.
    Повертає зрозумілі повідомлення замість traceback.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Enter the argument for the command"
    return inner


def parse_input(user_input: str):
    """
    Розбирає введення користувача:
    повертає (command, args)
    """
    user_input = user_input.strip()
    if not user_input:
        return "", []

    parts = user_input.split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args


@input_error
def add_contact(args, contacts: dict) -> str:
    """
    Команда: add [name] [phone]
    """
    name, phone = args  # ValueError / IndexError, якщо недостатньо аргументів
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args, contacts: dict) -> str:
    """
    Команда: change [name] [new_phone]
    """
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."


@input_error
def show_phone(args, contacts: dict) -> str:
    """
    Команда: phone [name]
    """
    name = args[0]  # IndexError, якщо немає імені
    return contacts[name]  # KeyError, якщо немає такого контакту


def show_all(contacts: dict) -> str:
    """
    Команда: all
    Повертає всі контакти одним рядком.
    (Для цієї команди аргументи не потрібні, помилок немає)
    """
    if not contacts:
        return "No contacts saved."

    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "":
            # Просто порожній ввід — просимо ввести команду,
            # а не "Enter the argument for the command"
            print("Please enter a command.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
