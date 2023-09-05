def month_to_season(num):
    if num in range(1,3) or num==12: 
        print('Зима')
    elif num in range(3,6): 
        print('Весна')
    elif num in range(6,9): 
        print('Лето')    
    elif num in range(9,12): 
        print('Осень')
    else:
        print('Введено неправильное значение')     


num=int(input('Введите номер месяца '))
month_to_season(num)    