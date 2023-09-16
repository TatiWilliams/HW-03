num_tickets = int(input("Введите количество билетов: "))
total_cost = 0
count_discounted = 0
for i in range(num_tickets):
    age = int(input("Введите возраст посетителя: "))
    if age < 18:
        cost = 0  
    elif age >= 18 and age < 25:
        count_discounted += 1 
        cost = 990  
    else:
        cost = 1390  
    total_cost += cost  
if num_tickets > 3:
    total_cost *= 0.9  
print("Сумма к оплате: ", total_cost, "руб.")