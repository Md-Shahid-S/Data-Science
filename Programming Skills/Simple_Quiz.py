quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the largest mammal in the world?", "answer": "Blue Whale"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Which country is known as the Land of the Rising Sun?", "answer": "Japan"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the smallest prime number?", "answer": "2"},
    {"question": "Which gas do plants absorb from the atmosphere?", "answer": "Carbon Dioxide"},
    {"question": "What is the longest river in the world?", "answer": "Nile"},
    {"question": "Which element has the atomic number 1?", "answer": "Hydrogen"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "What is the largest ocean on Earth?", "answer": "Pacific Ocean"},
    {"question": "Which country is famous for inventing pizza?", "answer": "Italy"},
    {"question": "What is the freezing point of water in Celsius?", "answer": "0"},
    {"question": "Which animal is known as the 'King of the Jungle'?", "answer": "Lion"},
    {"question": "What is the main ingredient in bread?", "answer": "Flour"}
]

score = 0
for q in quiz:
    print(q['question'])
    user_answer = input("Enter Your Answer")
    if user_answer.lower() == q['answer'].lower():
        print("Correct")
        score += 1

    else:
        print("Wrong")

print(f'your final score {score} of {len(quiz)}')