


def show_balance(deposit_bal):
    print(f"Your Balance is ${deposit_bal: .2f}")
    print(" ")

def deposit(deposit_bal):
    ask_amout = int(input("How Much will you like to add: "))
    while ask_amout <= 0:
        print("Invalid amount ")
        return 0
    else:
        deposit_bal += ask_amout
        print("Deposited Successfully \n")
        print("")
        return None


def withdraw(deposit_bal):
    with_amount = int(input("How much will you like to withdraw: "))
    if with_amount > deposit_bal:
        print("Insufficient Balance please Deposit More")
    else:
        deposit_bal -= with_amount
        print(f"Withdrawal successful Your New balance is ${deposit_bal: .2f}")
    print(" ")



def welcome():
    print("Welcome to the Gpyks bank \n"
          "Select An Option \n"
          "1. Deposit \n"
          "2. Withdraw \n"
          "3. Show my Balance: \n"
          "4. Close App ")


def main():
    deposit_bal = 0
    while True:
        welcome()
        option = input("Choose An Option: ")

        print()
        if option == '1':
            deposit(deposit_bal)
        elif option =='2' :
            withdraw(deposit_bal)
        elif option == '3':
            show_balance(deposit_bal)
        elif option == '4':
            print("-----Bye-----")
            break
        else:
            print("----invalid Option---- \n")

if __name__ == '__main__':
    main()
