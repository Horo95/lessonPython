from smartphone import Smartphone

catalog = []

copy1=Smartphone('Самсунг','ГАлакси','+79036605336')

copy2=Smartphone('Apple','Айфон','+79085543432')

copy3=Smartphone('Pear','Айфон','+79085543432')

copy4=Smartphone('Pancil','Айфон','+79085543432')

copy5=Smartphone('Run','Айфон','+79085543432')

catalog.insert(0, copy1)
catalog.append(copy2)
catalog.append(copy3)
catalog.append(copy4)
catalog.append(copy5)

for i in range(0, 5):
    print(catalog[i].phoneBrand + " - " + catalog[i].phoneModel + ". " + catalog[i].phoneNumber)

