result_1 = int(input("Укажите результат первого дня: "))
result_2 = int(input("Укажите желаемый результат: "))
day = 1
if result_1 > result_2:
    print(day)
while result_1 < result_2:
    result_1 = result_1 + result_1/10
    day += 1
print('Желаемого результата вы достигнете через', day, 'дней')
