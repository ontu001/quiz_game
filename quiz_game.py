def quiz_game():
    print("Welcome to the Quiz Game!")
    questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
        {"question": "What is the largest ocean in the world?", "options": ["Atlantic", "Pacific", "Indian", "Arctic"], "answer": "Pacific"},
        {"question": "What is the currency of Japan?", "options": ["Yen", "Dollar", "Euro", "Pound"], "answer": "Yen"},
        {"question": "What is the highest mountain in the world?", "options": ["Everest", "K2", "Kangchenjunga", "Lhotse"], "answer": "Everest"},
    ]
    score = 0
    for question in questions:
        print(question["question"])
        for i, option in enumerate(question["options"]):
            print(f"{i + 1}. {option}")
        answer = input("Enter your answer (1-4): ")
        if question["options"][int(answer) - 1] == question["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
    print(f"Your final score is: {score}/{len(questions)}")

quiz_game()



#md rohanur rahman ontu