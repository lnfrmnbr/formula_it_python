salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

def num_of_money_capital(salary_, spend_, months_, increase_):
    needed_money = 0
    for i in range(months_):
            needed_money += ((spend_ * ((increase_ + 1) ** i)) - salary_)
    return int(needed_money)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", num_of_money_capital(salary, spend, months, increase))
