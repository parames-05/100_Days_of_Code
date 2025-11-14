MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
ON = True

while ON:
    choice = input("\nWhat would you like to have? Type espresso / latte / cappuccino: ").lower()

    if choice == "off":
        print("Switching off... ... ...")
        ON = False

    elif choice == "report":
        print(f"Amount of water left is {resources['water']} ml")
        print(f"Amount of milk left is {resources['milk']} ml")
        print(f"Amount of coffee left is {resources['coffee']} g")
        print(f"Money generated: ${profit:.2f}")

    elif choice in MENU:
        drink = MENU[choice]
        ingredients_needed = drink["ingredients"]
        can_make = True

        #To Check if all ingredients are available
        for item in ingredients_needed:
            if resources[item] < ingredients_needed[item]:
                print(f"Sorry, not enough {item}.")
                can_make = False

        if can_make:
            print(f"Processing your drink... Please pay ${drink['cost']}")
            penny = int(input("Enter number of pennies: "))
            nickel = int(input("Enter number of nickels: "))
            dime = int(input("Enter number of dimes: "))
            quarter = int(input("Enter number of quarters: "))
            total_amt = round((penny * 0.01) + (nickel * 0.05) + (dime * 0.10) + (quarter * 0.25), 2)

            if total_amt < drink["cost"]:
                print("Insufficient amount...Refund initiated.")
            else:
                for item in ingredients_needed:
                    resources[item] -= ingredients_needed[item]

                change = round(total_amt - drink["cost"], 2)
                if change > 0:
                    print(f"Payment successful. Here's your change: ${change}")
                print("Your drink is getting ready!!! Enjoy! ☕")

                profit += drink["cost"]

    else:
        print("Invalid input. Please choose a valid option.")
