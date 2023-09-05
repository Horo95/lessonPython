def  is_year_leap(year):
    try:
        x=int(year)
        if x%4==0:
            print(True)
        else :
            print(False)
    except ValueError:
        print('Это не число,введите другие данные')       
    
year=input('год : ')
is_year_leap(year)       