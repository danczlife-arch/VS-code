print ("Welcome to Koci quiz game!")
def ask_question (question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print("Correct, you got "+"+1 point!")
        return 1
    else: print("Wrong, the correct answer is", correct_answer)
    return 0

score = 0

score += ask_question ("What is 84 + 73?", "157")
score += ask_question ("What is the capital of Czech Republic?", "Prague")
score += ask_question ("Who is the Greatest football player of all time?", "Ronaldinho")
score += ask_question ("What is the biggest animal in the world?", "Blue whale")
score += ask_question ("What is the fastest land animal?", "Cheetah")

print("Quiz finished! Your score is:", score, "/ 5")

percentage = score / 5 * 100

print ("You got ", int(percentage), "%")
if score == 5:
    print("Perfect!")
elif score >= 4:
    print("Great job!")
elif score >= 3:
    print("Good!")
elif score >= 2:
    print("Keep practicing!")
elif score >= 1:
    print("Try again!")
else:
    print("You need to practise more!")
print("Thank you for playing Koci quiz game!")
answer = input("Do you want to play again? y/n")


                    

