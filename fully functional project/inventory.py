goods = []
price =[]
total = 0


while True:
    print("Welcome To this Store")
    print("1. Add product\n"
          "2. Remove Product\n"
          "3  List product\n"
          "4  Quit")
    option = int(input("please Select An Option"))

    if option == 1:
        option1 = input("What is the name of your Product ? ")
        goods.append(option1)
        print("Product Added")
    elif option == 2:
        option2 =input("Which product do you want to remove ? ")
        if option2 in goods:
            goods.remove(option2)
            print(" Product Removed")
        else:
            print("Product not found ")
    elif option == 3:
        print(goods)
    elif option == 4:
        break

print("Goodbye")