class CoffeeMachine:
    def __init__(self , water , milk , coffe_bean , money , no_of_cups):
        self.water = 400
        self.milk = 540
        self.coffe_bean = 120
        self.money = 550
        self.no_of_cups = 9

    def buy(self):
        coffetype = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu :")
        if coffetype == '1':
            if self.water >= 250 and self.coffe_bean >= 16:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffe_bean -= 16
                self.money +=4
                self.no_of_cups -= 1
            else:
                #resc = [water // 250, coffe_bean // 16]
                lst = [self.water, self.milk, self.coffe_bean]
                min_resc = min(lst)
                print("Sorry, not enough", lst.index(min_resc), '!')

        elif coffetype == '2':
            if self.water >= 350 and self.milk>= 75 and self.coffe_bean >= 20:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.coffe_bean -= 20
                self.milk -=  75
                self.money += 7
                self.no_of_cups -=1
            else:
               #resc = [water // 350 ,coffe_bean // 75 , milk // 7]
                lst =[self.water ,self.milk , self.coffe_bean]
                min_resc = min(lst)
                print("Sorry, not enough", lst.index(min_resc), '!')

        elif coffetype == '3':
            if self.water >= 200 and self.milk>= 100 and self.coffe_bean >= 12:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffe_bean -= 12
                self.money += 6
                self.no_of_cups -= 1
            else:
                #resc = [water // 200 ,]
                lst = [self.water, self.milk, self.coffe_bean]
                min_resc = min(lst)
                print("Sorry, not enough",lst.index(min_resc), '!')

        elif coffetype == 'back':
            pass



    def fill(self):
        water_add = int(input('Write how many ml of water do you want to add:'))
        milk_add = int(input("Write how many ml of milk do you want to add:"))
        coffe_add = int(input("Write how many grams of coffee beans do you want to add:"))
        no_of_cups_add = int(input("Write how many disposable cups of coffee do you want to add:"))

        self.water += water_add
        self.milk += milk_add
        self.coffe_bean += coffe_add
        self.no_of_cups += no_of_cups_add

    def take(self):

        self.money = 0
        print("I gave you $", self.money)


    def show(self):
        print("The coffee machine has:")
        print(self.water ,'of water')
        print(self.milk , "of milk")
        print(self.coffe_bean ,'of coffe beans')
        print(self.no_of_cups , 'of disposable cups')
        print('$', self.money , 'of money')




obj = CoffeeMachine(400 , 540 , 120 , 550 , 9)
while True:
    action = input("Write action (buy, fill, take,remaining, exit)):")
    if action == 'buy':
        obj.buy()
    elif action == 'fill':
        obj.fill()
    elif action == 'take':
        obj.take()
    elif action == 'remaining':
        obj.show()
    elif action == 'exit':
        break
