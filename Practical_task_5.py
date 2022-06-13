revenue = float(input('Укажите полученную выручку: '))
damage = float(input('Укажите полученный убыток: '))
if revenue > damage:
    result = revenue - damage
    print('Вы получили доход в размере', result)
    number_of_staff = float(input('Укажите количество сотрудниковв организации: '))
    revenue_worker = result / number_of_staff
    print('Доход на одного сотрудника составил: ', round(revenue_worker, 2))
elif revenue == damage:
    print('Ваш доход составил: 0')
else:
    print('Вы получили убыток в размере', (revenue - damage) * -1)
