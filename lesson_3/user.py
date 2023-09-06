class User:
    def __init__(self,first_name,last_name):
        print('я создался')
        self.username=first_name
        self.userlastname=last_name

    def Name(self):
        print('меня зовут ',self.username)
        
    def LastName(self):
        print('Моя фамилия',self.userlastname)    

    def all(self):
        print('Ваше имя и фамилия: ',self.username, self.userlastname)    

