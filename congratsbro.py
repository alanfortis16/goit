from datetime import datetime, date, timedelta

def _safe_birthday_this_year(birth_dt: date, year: int) -> date:
    try: return date(year, birth_dt.month, birth_dt.day)
    except ValueError:
        if birth_dt.month == 2 and birth_dt.day == 29:
            return date(year, 2, 28)
        raise

def get_upcoming_birthdays(users):
    today = date.today()
    horizon = today + timedelta(days=7)
    result = []
    
    for user in users:
        
        birth_dt = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        this_year = _safe_birthday_this_year(birth_dt, today.year)
        

        if this_year < today:
            this_year = _safe_birthday_this_year(birth_dt, today.year + 1)

        if today <= this_year <= horizon:
            congr_date = this_year

            if congr_date.weekday() == 5:
                congr_date += timedelta(days=2)

            elif congr_date.weekday() == 6:
                congr_date += timedelta(days=1)

            result.append({
            "name": user ["name"],
            "congratulation_date": congr_date.strftime("%Y.%m.%d")
        })
    
    result.sort(key=lambda x: x["congratulation_date"])
    return result



users = [
    {"name": "Alan", "birthday": "1999.10.20"},
    {"name": "Lena", "birthday": "1998.10.25"},
]
print(get_upcoming_birthdays(users))

