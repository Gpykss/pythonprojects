import random

if __name__ =='__main__':
    print("yes")
    menu ={"beans" : 6,
           "rice" : 5,
           "garri" : 7}
    cart =[]
    total = 0
    print("------Menu------")

    for key,value  in menu.items():
        print(f"{key} : {value}")

    while True:
        food = input("What do you want (Enter q to quit)? ").lower()
        if food == "q":
            break
        elif food not in menu:
            food_name = input("which food you want to add i will check the amount ?")
            food_amount = random.randint(5,15)
            menu.update({food_name: food_amount})
            cart.append(food)
            print("added to your cart")
        else:
            cart.append(food)



    print("------ Cart ------")
    for food in cart:
        total = menu.get(food)
        print(food, end=" ")
        print()

    print(f"your total is ${total}")