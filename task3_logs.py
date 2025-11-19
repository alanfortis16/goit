import sys
from pathlib import Path
from typing import List, Dict


def parse_log_line(line: str) -> dict:
    """
    Парсить один рядок логу у словник:
    {
        "date": ...,
        "time": ...,
        "level": ...,
        "message": ...
    }
    """
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        return {}

    date, time, level, message = parts
    # level у файлі типу "INFO", "ERROR", "DEBUG", "WARNING"
    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message,
    }


def load_logs(file_path: str) -> List[dict]:
    """
    Завантажує лог-файл і повертає список розібраних записів.
    """
    logs = []
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Файл {file_path!r} не знайдено")

    with path.open(encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            record = parse_log_line(line)
            if record:
                logs.append(record)

    return logs


def filter_logs_by_level(logs: List[dict], level: str) -> List[dict]:
    """
    Повертає список логів заданого рівня.
    Використовує списковий вираз (функціональний стиль).
    """
    level = level.upper()
    return [log for log in logs if log.get("level") == level]


def count_logs_by_level(logs: List[dict]) -> Dict[str, int]:
    """
    Підраховує кількість записів для кожного рівня логування.
    """
    counts: Dict[str, int] = {}
    for log in logs:
        lvl = log.get("level")
        counts[lvl] = counts.get(lvl, 0) + 1
    return counts


def display_log_counts(counts: Dict[str, int]) -> None:
    """
    Виводить таблицю з кількістю записів по рівнях логування.
    """
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        value = counts.get(level, 0)
        print(f"{level:<16} | {value}")


def main():
    if len(sys.argv) < 2:
        print("Використання: python task3_logs.py path/to/logfile.log [level]")
        sys.exit(1)

    file_path = sys.argv[1]
    level_filter = sys.argv[2].upper() if len(sys.argv) >= 3 else None

    try:
        logs = load_logs(file_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit(1)

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if level_filter:
        filtered = filter_logs_by_level(logs, level_filter)
        print(f"\nДеталі логів для рівня '{level_filter}':")
        for log in filtered:
            print(f"{log['date']} {log['time']} - {log['message']}")


if __name__ == "__main__":
    main()
