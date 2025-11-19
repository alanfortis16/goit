import sys
from pathlib import Path

from colorama import init, Fore, Style


def print_directory_tree(path: Path, indent: str = ""):
    """
    Рекурсивно виводить структуру директорії:
    - папки одним кольором
    - файли іншим
    """
    try:
        # спочатку папки, потім файли
        items = sorted(
            path.iterdir(),
            key=lambda p: (p.is_file(), p.name.lower())
        )
    except PermissionError:
        print(indent + Fore.RED + "[Немає доступу]" + Style.RESET_ALL)
        return

    for item in items:
        if item.is_dir():
            # Папка — синім
            print(indent + Fore.BLUE + f"[{item.name}]" + Style.RESET_ALL)
            # Рекурсивно обходимо піддиректорію
            print_directory_tree(item, indent + "    ")
        else:
            # Файл — зеленим
            print(indent + Fore.GREEN + item.name + Style.RESET_ALL)


def main():
    # ініціалізація colorama (важливо для Windows)
    init(autoreset=True)

    # очікуємо шлях до директорії як аргумент
    if len(sys.argv) < 2:
        print("Будь ласка, передайте шлях до директорії як аргумент.")
        print(f"Приклад: python {Path(__file__).name} C:/Users/alanf/code")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    # перевірка, що шлях існує
    if not dir_path.exists():
        print(f"Помилка: шлях {dir_path} не існує.")
        sys.exit(1)

    # перевірка, що це саме директорія
    if not dir_path.is_dir():
        print(f"Помилка: шлях {dir_path} не є директорією.")
        sys.exit(1)

    print(f"Структура директорії: {dir_path}\n")
    print_directory_tree(dir_path)


if __name__ == "__main__":
    main()
