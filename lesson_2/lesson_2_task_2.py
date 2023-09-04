def  is_year_leap(year):
    
    if year%4==0:
        print(True)
    else:
        print(False)   


year=int(input('год :'))
is_year_leap(year)       