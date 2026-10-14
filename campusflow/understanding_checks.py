QUESTIONS = [
    {
        "question": "Which file validates user input?",
        "options": [
            "A. reports.py",
            "B. validation.py",
            "C. queue.py",
        ],
        "answer": "B",
    },
    {
        "question": "What does create_ticket() do?",
        "options": [
            "A. Creates a ticket",
            "B. Deletes tickets",
            "C. Generates reports",
        ],
        "answer": "A",
    },
    {
        "question": "Which status comes after open?",
        "options": [
            "A. resolved",
            "B. closed",
            "C. in_progress",
        ],
        "answer": "C",
    },
    {
        "question": "What is JSON used for in CampusFlow?",
        "options": [
            "A. Changing priority",
            "B. Saving ticket data",
            "C. Assigning tickets",
        ],
        "answer": "B",
    },
    {
        "question": "Which tickets appear in the work queue?",
        "options": [
            "A. Open tickets",
            "B. Resolved tickets",
            "C. All tickets",
        ],
        "answer": "A",
    },
    {
        "question": "What is unittest used for?",
        "options": [
            "A. Creating Git branches",
            "B. Designing websites",
            "C. Testing Python code",
        ],
        "answer": "C",
    },
]


def check_answer(question, answer):
    if not isinstance(answer, str):
        return False

    answer = answer.strip().upper()

    if answer == question["answer"]:
        return True

    return False


def calculate_score(answers):
    if len(answers) != len(QUESTIONS):
        raise ValueError("Incorrect number of answers")

    score = 0

    for i in range(len(QUESTIONS)):
        question = QUESTIONS[i]
        answer = answers[i]

        if check_answer(question, answer):
            score += 1

    return score


def run_understanding_check():
    print("\n=== ENGINEERING UNDERSTANDING CHECK ===")

    answers = []

    question_number = 1

    for question in QUESTIONS:
        print()
        print("Question", question_number)
        print(question["question"])

        for option in question["options"]:
            print(option)

        while True:
            answer = input("Your answer (A/B/C): ").strip().upper()

            if answer == "A" or answer == "B" or answer == "C":
                break

            print("Please enter A, B, or C.")

        answers.append(answer)
        question_number += 1

    score = calculate_score(answers)

    print("\nYour score:", score, "out of", len(QUESTIONS))

    if score == 6:
        print("Excellent understanding!")

    elif score >= 4:
        print("Good work!")

    else:
        print("Keep practising!")

    return score