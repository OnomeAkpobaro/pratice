def quiz_app():
    questions = [
        {"question": "Who are you?", "options": ["1. Paul", "2. Tony", "3. Mark"], "answer": 1}, 
        {"question": "What is the hottest planet", "options": ["1. Mars", "2. Earth", "3. Mercury"], "answer": 3}

    ]
    score = 0
    for q in questions:
        print(q['question'])
        for opt in q['options']:
            print(opt)
        answer = int(input("Enter your answer (1/2/3): "))
        if answer == q['answer']:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your final scorwe is: {score}/{len(questions)}")

quiz_app()
