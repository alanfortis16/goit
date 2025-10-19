from datetime import datetime
def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        difference = today - given_date
        print("Різниця ", difference.days, "днів")
        return difference.days
    except ValueError:
        print("Помилка: дата має бути у форматі 'РРРР-ММ-ДД'.")
        return None


get_days_from_today("2021-05-05")