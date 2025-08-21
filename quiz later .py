#  How the Quiz Game Works:
# The user is asked a series of questions.
#
# They input their answers.
#
# You check if it's correct and track the score.
#
# At the end, you show their final score and maybe give feedback.




def quiz_menu ():
    print(
            "Welcome to the quiz Arena \n"
            "Please Select An Option :\n"
            "1. Start Quiz \n"
            "2. End Quiz"
        )


def ask_question(total):
    questions = ["who is the first man to fly ? ",
                     "where is californium ?",
                     "where is nigeria ?"
                     ]
    answer = ["goodwill","usa","west africa"]
    question_num = 0

    for question in questions:
        print(f"Q{question_num +1}. {question}", end="")
        print("")
        guess = input("Answer: ")
        if guess == answer[question_num]:
            print("Correct Answer")
            total += 10
        else:
          print("incorrect Answer")
          total -= 10
    question_num += 1


def main():
    total = 0
    while True:
        quiz_menu()
        user_in = int(input(""))
        match user_in:
            case 1:
                ask_question(total)
                print(f" Your Score  is {total}")
            case 2:
                break
    print("Good bye ")
    print(f"Your Score  is {total}")

if __name__ == '__main__':
    main()


