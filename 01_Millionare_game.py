#Project 1 : Who wants to be a Millionare

# Used Lists for storing questions and options ...
# Used Conditional statements like if-else for Correct answers ...
# Using loops i.e. fow loops for executing each question from questions ...

questions = [
    ["What is the name of the largest ocean on Earth?","Atlantic Ocean","Indian Ocean","Arctic Ocean","Paciific Ocean",4],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the smallest country in the world?", "San Marino", "Monaco", "Liechtenstein","Vatican City", 4]
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
]
prizes = [100000, 350000, 400000, 450000, 500000, 999999, 2000000, 3000000, 4000000, 5000000, 9999999]

i = 0 
for question in questions:
    print(question[0])
    print(f" A. {question[1]} \n B. {question[2]}\n C. {question[3]}\n D. {question[4]}\n")

    ans = int(input("Enter your answer. 1 for A, 2 for B, 3 for C, 4 for D\n"))
    if(question[5] == ans):
        print("Correct Answer")
        print("Let's move towards the next question ...")
    else:
        print(f"Incorrect, the correct answer was {question[5]}")
        print("Better luck next time!")
        break 
    print(f"Btw ... You won {prizes[i]} $")
    i = i+1   
