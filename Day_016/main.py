from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu= Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
ison = True
while ison:
    options=menu.get_items()
    choice = input(f"what would you like to have? {options} \n").lower()
    if choice == "off":
        print("Switching off ... ... ...")
        ison = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        aaa= coffee_maker.is_resource_sufficient(drink)
        if aaa:
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



