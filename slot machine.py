import random



def shuffle ():
    things = ['🍏','🍎','🍉','🍈','🍍']
    result =[]
    for thing in range(3):
        result.append(random.choice(things))
    return result

def prints_row(row):
    print(" ".join(row))

def payout(row,bet):
    if row[0] == row[1] ==row[2]:
       if row[0] =='🍍':
           return bet *4
       elif row[0] =='🍈':
           return bet*6
       elif row[0] =='🍉':
           return bet*6
       elif row[0] =='🍎':
           return bet*6
       elif row[0] =='🍏':
           return bet*6
    return 0


def main():
    balance = 100
    while True:
        row = shuffle()
        print("-----Welcome To Sll Casino-----")
        print("1. Play Slot Game\n"
              "2. Balance\n"
              "3. Exit Game")
        option = input("Select an option: ")
        print()
        if not option.isdigit() or option <= '0':
            print("Invalid Option")
            continue
        elif option == '1':
            print(f"-----Balance: ${balance: .2f}-----")
            bet = int(input("How much will you like to bet: "))
            if bet <= 0:
                print("Invalid bet")
                bet = int(input("How much will you like to bet: "))
            elif bet > balance:
                print("Insufficient Funds")
            else:
                prints_row(row)
                payout(row,bet)
                if payout(row,bet) > 0:
                    balance += payout(row,bet)
                    print("Congrats you win")
                elif payout(row,bet) <= 0:
                    balance -= bet
                    print(" You lost ")
                continue
        elif option == '2':
            print(f'Your balance is ${balance: .2f}')
            continue
        elif option == '3':
            print("____Goodbye----")
        break


if __name__ == '__main__':
    main()