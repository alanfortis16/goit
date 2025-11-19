from pathlib import Path


def total_salary(path):
    """
    Читає файл із зарплатами розробників і повертає кортеж:
    (загальна сума, середня зарплата).
    """
    try:
        with open(path, encoding="utf-8") as f:
            total = 0
            count = 0

            for line in f:
                line = line.strip()
                if not line:
                    continue

                try:
                    name, salary_str = line.split(",", maxsplit=1)
                except ValueError:
                    print(f"Неправильний формат рядка (пропускаю): {line!r}")
                    continue

                try:
                    salary = int(salary_str)
                except ValueError:
                    print(f"Неможливо перетворити зарплату на число (пропускаю): {salary_str!r}")
                    continue

                total += salary
                count += 1

        if count == 0:
            return 0, 0

        average = total / count
        return total, average

    except FileNotFoundError:
        print(f"Файл за шляхом {path!r} не знайдено.")
        return 0, 0


if __name__ == "__main__":
    base_dir = Path(__file__).parent
    file_path = base_dir / "salary_file.txt"

    print("Шукаю файл тут:", file_path)
    print("Чи існує salary_file.txt?:", file_path.exists())

    # 🔹 Якщо файлу немає — СТВОРЮЄМО його прямо тут
    if not file_path.exists():
        print("Файл не знайдено. Створюю тестовий salary_file.txt...")
        content = "Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000\n"
        file_path.write_text(content, encoding="utf-8")
        print("Файл створено:", file_path)
        print("Чи існує salary_file.txt тепер?:", file_path.exists())

    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
