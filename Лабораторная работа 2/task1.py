money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

def number_of_mounths(money_capital_, salary_, spend_, increase_):
    num = 0
    while money_capital_ > 0:
        money_capital_ += (salary_ - (spend_ * ((increase_ + 1) ** num)))
        num += 1
    return num - 1

print("Количество месяцев, которое можно протянуть без долгов:", number_of_mounths(money_capital, salary, spend, increase))
