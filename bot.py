def parse_input(user_input: str):
    """
    Приймає рядок від користувача, повертає:
    command (str), args (list[str])
    """
    user_input = user_input.strip()
    if not user_input:
        return "", []

    parts = user_input.split()
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts: dict) -> str:
    """
    Команда: add [name] [phone]
    Додає новий контакт у словник contacts.
    """
    if len(args) < 2:
        return "Not enough arguments. Usage: add [name] [phone]"

    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts: dict) -> str:
    """
    Команда: change [name] [new_phone]
    Змінює номер телефону існуючого контакту.
    """
    if len(args) < 2:
        return "Not enough arguments. Usage: change [name] [new_phone]"

    name, phone = args[0], args[1]

    if name not in contacts:
        return "Contact not found."

    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts: dict) -> str:
    """
    Команда: phone [name]
    Повертає номер телефону за ім'ям.
    """
    if len(args) < 1:
        return "Not enough arguments. Usage: phone [name]"

    name = args[0]
    if name not in contacts:
        return "Contact not found."

    return contacts[name]


def show_all(contacts: dict) -> str:
    """
    Команда: all
    Повертає всі збережені контакти у вигляді рядка.
    """
    if not contacts:
        return "No contacts found."

    lines = []
    for name, phone in contacts.items():
        lines.append(f"{name}: {phone}")
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
            result = add_contact(args, contacts)
            print(result)

        elif command == "change":
            result = change_contact(args, contacts)
            print(result)

        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)

        elif command == "all":
            result = show_all(contacts)
            print(result)

        elif command == "":
            print("Please enter a command.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
