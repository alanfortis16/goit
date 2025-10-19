import random
def get_numbers_ticket(min_num, max_num, quantity):
    if (
        not isinstance(min_num, int) or
        not isinstance(max_num, int) or
        not isinstance(quantity, int) or
        min_num < 1 or
        max_num > 1000 or
        min_num >= max_num or
        quantity <= 0 or
        quantity > (max_num - min_num + 1)
    ):
        print("Помилка: некоректні параметри.")
        return []

    numbers = random.sample(range(min_num, max_num + 1), quantity)
    numbers.sort() 

    return numbers
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
