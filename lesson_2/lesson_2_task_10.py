

def bank(x,y):
    for i in range(1,y+1):
        p=x*0.1
        x+=p
        summa=x
    print('Через', i, 'год/лет','на счету будет',summa)
            
x=int(input('Сумма первоначального вклада: '))
y=int(input('Срок вклада(в годах): '))

bank(x,y)
