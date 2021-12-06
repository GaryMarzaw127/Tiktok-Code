

def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("jawaban (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("BENAR!")
        return 1
    else:
        print("SALAH!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("HASIL")
    print("-------------------------")

    print("Jawaban: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Tebakan: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Score Anda : "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Mau Main Lagi ? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Siapa CEO Facebook ? ": "D",
 "Siapa Pendiri Microsoft ? ": "A",
 "Siapa CEO Tesla ? ": "C",
 "Siapa Founder Gojek ? ": "B"
}

options = [["A. Guido van Rossum", "B. Chris Feng", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. Bill Gates/Paul Allen", "B. Steve Jobs", "C. Jeff Bezos", "D. Mike Krieger"],
          ["A. Leonardo Da Vinci", "B. leonardo dicaprio", "C. Elon Musk", "D. Tom Hanks"],
          ["A. William Tanuwijaya","B. Nadiem Makarim", "C. James Chang", "D. Kevin Systrom"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")