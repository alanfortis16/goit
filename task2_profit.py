import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа з тексту як float.
    Вважаємо, що числа відокремлені пробілами і записані без помилок.
    """
    # Знаходимо числа типу 100, 100.5, 0.01 тощо
    pattern = r"\d+(?:\.\d+)?"
    for match in re.findall(pattern, text):
        yield float(match)


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Використовує передану функцію-генератор (наприклад, generator_numbers),
    щоб підсумувати всі числа в тексті.
    """
    return sum(func(text))


if __name__ == "__main__":
    text = (
        "Загальний дохід працівника складається з декількох частин: "
        "1000.01 як основний дохід, доповнений додатковими надходженнями "
        "27.45 і 324.00 доларів."
    )
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")
    # Очікувано: 1351.46
