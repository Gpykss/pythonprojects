import random


# answers = ["go","be","2","4","5","9","f","7","x","s","3","b","g","0",]
#
# number = random.randint(1, 50)
# number_2 = random.random()
# number_3 = random.choice(answers)
# random.shuffle(answers)
#
# print(number)
# print(number_2)
# print(number_3)
# print(answers)

# we want agme where user deposits money  guess a random number if its wrong it shows debit if its correct it
#adds moneyand it continues until user quit after quit it shows  thier balance

deposit = 0
balance =0
lowest_num = 1
highest_num = 100
token = random.randint(lowest_num,highest_num)

print("------Welcome To TheBetShrine------")
while True:
#formenu
    optionList = int(input("----Choose An Option----\n"
                       "1. Deposit Funds\n"
                       "2. PlayGame \n"
                       "3. check Balance\n"
                       "4. Quit\n"))
#foroption==1
    if optionList == 1:
        amount = int(input("How Much Do You Want To Fund: "))
        deposit += amount
        print(f"${amount} added")
        print()
    elif optionList == 2 :
        print("You win X5 of your stake If you guess correct")
        stake = int(input("Enter a stake: "))
        if stake > deposit:
            print("Insufficient balance ")
        else:
            num = int(input("Enter a Number:  "))
            print(f"Random Result : {token}")
            if num == token:
                print(" You Win ")
                balance += stake * 5
            else:
                print("You Loose")
                deposit -= stake
    elif optionList == 3:
        print(f"Your deposit balane is {deposit}")
        print(f"Your Profit Balance is: ${balance}")
    elif optionList == 4:
        break

totalBalance =  deposit + balance
print("-------------------")
print(f"Goodbye Deposit bal  : ${deposit}  \n Profit Balance ${balance} ")
print(f"Your total Balance is : ${totalBalance: 2F}")