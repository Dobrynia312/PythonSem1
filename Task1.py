#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
day_of_week = int(input('Введите номер дня недели: '))
if day_of_week == 6 or day_of_week == 7:
    print('Этот день выходной')
elif day_of_week <= 5 and day_of_week >= 1:
    print('Этот день рабочий')
else:
    print('Это не день недели')