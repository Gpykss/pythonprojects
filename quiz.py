questions = ["where is nigeria",'what is your name',"how old are yo ?"]
options =(("A.africa","B.china","C. korea"),("A.gp","B.hh","C.hv"),("A.10","B.22","C.21"))
answers = ("A","B","C")
guesses = []
score = 0
question_num =0

for question in questions:
    print(f"{question_num + 1} {question}")
    for option in options[question_num]:
        print(option)


    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        print("Correct answer \n" )
        score += 1
    else:
        print("Answer is incorrect ")
    question_num += 1

total = int((score / len(questions)) *100)
print(f"Your Total Is = {total}%")