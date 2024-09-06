questions = ['What is the capital of France?', 
             'What is 2+2?',
            'What is the capital of the United States?', 
            'What is the largest planet in our solar system?', 
            'Who painted the Mona Lisa?', 
            'What is the chemical symbol for gold?', 
            'What is the square root of 64?',
            'What is the tallest mountain in the world?',
            'Who wrote the play "Romeo and Juliet"?']
options = [('A.Paris', 'B.London', 'C.Berlin', 'D.Madrid'),
            ('A.3', 'B.4', 'C.5', 'D.6'),
           ( 'A.Los Angeles', 'B.New York City', 'C.Washington D.C.', 'D.Chicago'),
           ( 'A.Earth', 'B.Jupiter', 'C.Saturn', 'D.Mars'),
           ( 'A.Vincent van Gogh', 'B.Leonardo da Vinci', 'C.Pablo Picasso', 'D.Claude Monet]'),
           ( 'A.Gd', 'B.Gl', 'C.Ga', 'D.Au'),
           ( 'A.6', 'B.7', 'C.8', 'D.9'),
           ( 'A.Mount Everest', 'B.K2', 'C.Mount Kilimanjaro', 'D.Mount Fuji'),
           ( 'A.William Shakespeare', 'B.George Bernard Shaw', 'C.Anton Chekhov', 'D.Henrik Ibsen')]
score = 0
guesses = []
question_number = 1
# question_number = 0
answers = ['A', 'B', 'C', 'D', 'A', 'D', 'C', 'A', 'A']
for question in questions:
    print("-----------------------------")
    print(question_number,end='.')
    print(question)
    for option in options[questions.index(question)]:
        print(option)
    guess = input("Enter your answer: ").upper()
    guesses.append(guess)
    if guess == answers[questions.index(question)]:
            score += 1
            print("Correct!")
    else:
            print("Incorrect!")
    
    question_number += 1
print("-----------------------------")
print(f"Your score is {score} out of {len(questions)}")
print("-----------------------------")