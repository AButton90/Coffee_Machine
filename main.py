from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1. Print resource

starbucks = CoffeeMaker()
sb_menu = Menu()
sb_till = MoneyMachine()

while True:
    order_input = input(f"What would you like? ({sb_menu.get_items()}):  ")

    if order_input == 'off':
        break
    elif order_input == 'report':
        starbucks.report()
        sb_till.report()
    else:
        order = sb_menu.find_drink(order_input)

        if order == "Sorry that item is not available.":
            break
        
        #continue if valid choice
            #check if resources sufficient
        if starbucks.is_resource_sufficient(order) == True:
            #get payment
            print(order.cost)
            if order.name in sb_menu.get_items():
                
                if sb_till.make_payment(order.cost) == True:
                    #make drink
                    starbucks.make_coffee(order)

            
