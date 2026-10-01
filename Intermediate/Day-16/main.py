from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Create objects
coffee_machine = CoffeeMaker()
coffee = Menu()
money = MoneyMachine()

machine_on = True
while machine_on:

    #Get user's drink choice
    drink = input(f"What would you like? {coffee.get_items()} : ").lower()

    if drink == "off":
        #exist while loop
        machine_on = False

    elif drink == "report":
        #print report
        coffee_machine.report()
        money.report()

    else:
        #check and get MenuItem obj for chosen drink.
        coffee_type = coffee.find_drink(drink)

        #carry on for existing drink on menu
        if coffee_type is not None:
            sufficient = coffee_machine.is_resource_sufficient(coffee_type)
            if sufficient:
                #Try-Except block to print error message if anything other than float entered and asks user to try again
                try:
                    enough_money = money.make_payment(coffee.menu[coffee.menu.index(coffee_type)].cost)
                    if enough_money:
                        coffee_machine.make_coffee(coffee_type)
                except ValueError:
                    print("Incorrect Input. Try again.\n")