#--------------------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    print("")
    print("Welcome to the TRIVIA Game")
    print("")
    for key in questions:
        print(f" ------------------Question {question_num}------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C or D): ").strip().upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1
    display_score(correct_guesses, guesses)
#--------------------------------
def check_answer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0
#--------------------------------
def display_score(correct_guesses, guesses):
    print("---------------------------------------")
    print("Results")
    print("---------------------------------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    i = 20*score//100
    print("Your score is: "+'-'*i+str(score)+"%"+'-'*(20 - i))
    # print("Your score is: ------------------"+str(score)+"%------------------")
    
    if score >= 90:
        print("Wow! You're a trivia genius! You must have a brain the size of a planet.")
    elif score >= 80:
        print("Impressive! You're a trivia pro. Keep up the great work!")
    elif score >= 70:
        print("Good job! You've got a solid grasp of trivia. Keep learning!")
    elif score >= 60:
        print("Not bad! You're on your way to becoming a trivia master. Keep practicing!")
    elif score >= 50:
        print("You're making progress! With a bit more practice, you'll do even better.")
    elif score >= 40:
        print("It's a start! Keep playing and you'll improve.")
    elif score >= 30:
        print("You're getting there! Trivia can be challenging, but don't give up.")
    elif score >= 10:
        print("Don't be discouraged! Everyone starts somewhere. Keep playing and learning.")
    else:
        print("Don't worry, trivia is tricky! Keep playing and you'll improve.")






#--------------------------------
def play_again():
    response = input("Do you want to play again?  (yes or no): ").strip().lower()
    if response == "yes":
        return True
    else:
        return False
    
#--------------------------------
questions = {
    "Who wrote the play 'Hamlet'?:  ": "A",
    "In which year was the Eiffel Tower completed?: ": "B",
    "Which famous physicist formulated the theory of relativity?: ": "A",
    "What is the chemical symbol for oxygen?: ": "A",  
    "What is the largest planet in our solar system?: ": "B",
    "Who painted the 'Starry Night'?: ": "A",
    "What is the national animal of China?: ": "D",  
    "Which gas do plants absorb from the atmosphere during photosynthesis?: ": "C",  
    "What is the capital of Australia?: ": "C",
    "Who was the first man in the world?: ": "A",
    "What is the smallest prime number?: ": "D",
    "Who wrote the novel '1984'?: ": "A",
    "What is the largest ocean on Earth?: ": "B",
    "What is the chemical symbol for gold?: ": "B",
    "Which planet is known as the 'Blue Planet'?: ": "D",
    "Who was the first woman to fly solo across the Atlantic Ocean?: ": "A",
    "Which is the best epic poem in the world?: ": "C",
    "What gas do astronauts breathe inside the International Space Station?: ": "A",
    "How many Olympic rings are there?: ": "D",
    "What is the national flower of Japan?: ": "B"
}


options = [
    ["A. William Shakespeare", "B. Charles Dickens", "C. Jane Austen", "D. Leo Tolstoy"],
    ["A. 1887", "B. 1889", "C. 1900", "D. 1920"],
    ["A. Albert Einstein", "B. Isaac Newton", "C. Galileo Galilei", "D. Charles Darwin"],
    ["A. O", "B. Ox", "C. Oxg", "D. Og"],
    ["A. Earth", "B. Jupiter", "C. Saturn", "D. Mars"],
    ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Michelangelo"],
    ["A. Panda", "B. Dragon", "C. Red Panda", "D. Giant panda"],
    ["A. Oxygen", "B. Hydrogen", "C. Carbon dioxide", "D. Nitrogen"],
    ["A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"],
    ["A. Adam", "B. Sarah", "C. Abraham", "D. Eve"],
    ["A. 0", "B. 1", "C. 3", "D. 2"],
    ["A. George Orwell", "B. F. Scott Fitzgerald", "C. J.D. Salinger", "D. Ernest Hemingway"],
    ["A. Atlantic Ocean", "B. Pacific Ocean", "C. Indian Ocean", "D. Arctic Ocean"],
    ["A. Ag", "B. Au", "C. Fe", "D. Hg"],
    ["A. Mars", "B. Jupiter", "C. Venus", "D. Earth"],
    ["A. Amelia Earhart", "B. Marie Curie", "C. Rosa Parks", "D. Joan of Arc"],
    ["A. Iliad", "B. Paradise lost", "C. knight in a panthers skin", "D. Odyssey"],
    ["A. Oxygen", "B. Nitrogen", "C. Helium", "D. Neon"],
    ["A. Four", "B. Six", "C. Seven", "D. Five"],
    ["A. Rose", "B. Cherry Blossom", "C. Orchid", "D. Lily"]
]

new_game()
while play_again():
    new_game()
print("Bye!")



