#Variables
money = 300
Deli="Deli"
Bakery="Bakery"
Frozenfood="Frozenfood"
Drinksection="Drinksection"

currentroom = Deli
class food:
    def __init__(self,name,price):
        self.name = name
        self.price = price

def store():
    global name
    global price
    global money

    print("you have "+str(name) +" name and "+str(money) +" money")
