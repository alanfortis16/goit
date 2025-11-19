from pathlib import Path

def get_cats_info(path: str):
    cats = []

    try:
        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  # пропускаємо порожні рядки

                parts = line.split(",")
                if len(parts) != 3:
                    print(f"Неправильний формат рядка (пропускаю): {line!r}")
                    continue

                cat_id, name, age = parts
                cats.append({
                    "id": cat_id,
                    "name": name,
                    "age": age
                })
        return cats

    except FileNotFoundError:
        print(f"Файл за шляхом {path!r} не знайдено.")
        return []


# --------------------------
# Головна частина
# --------------------------

base_dir = Path(__file__).parent
file_path = base_dir / "cats_file.txt"

print("Шукаю файл тут:", file_path)
print("Файл існує?:", file_path.exists())

# Друкуємо вміст файлу для діагностики
print("\nВміст файлу (repr):")
if file_path.exists():
    print(repr(file_path.read_text(encoding="utf-8")))
else:
    print("(Файл не знайдено)")

# Викликаємо функцію
cats_info = get_cats_info(file_path)
print("\nРезультат get_cats_info():")
print(cats_info)
