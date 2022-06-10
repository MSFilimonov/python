sec = int(input('Введите время в секундах: '))
hour = (sec // 3600) % 24
minutes = (sec // 60) % 60
second = sec % 60
if minutes < 10:
    minutes = str('0' + str(minutes))
else:
    minutes = str(minutes)
if second < 10:
    second = str('0' + str(second))
else:
    s = str(second)
print(str(hour) + ':' + str(minutes) + ':' + str(second))
