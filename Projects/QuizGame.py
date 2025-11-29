questions = ("Which of the following is a programming language?: ",
             "What does CPU stand for?:",
             "Which planet is known as the Red Planet?: ",
             "Who developed the theory of relativity?: ",
             "Which gas do plants absorb during photosynthesis?: ")
options = (("A. HTML ", "B. CSS ", "C. PYTHON ", "D. HTTP",),
           ("A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Control Processing Unit"),
           ("A. Earth", "B. Jupiter", "C. Mars", "D. Venus"),
           ("A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"),
           ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"))
           
answers = ("C", "B", "C", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT! ")
    else:
        print("INCORRECT!")
    question_num += 1

print("-------------------------")
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
print("-------------------------")
print(f"You got {score} correct!")
percentage = int(score / len(questions) * 100)
print(f"Your score is: {percentage}%")