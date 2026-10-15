QUESTIONS = [
    {
        "question": "Ticket T001 is open and unassigned. A user tries to move it to in_progress. What should happen?",
        "options": {
            "A": "Accept",
            "B": "Reject and preserve all data",
            "C": "Resolve it automatically",
            "D": "Remove ticket"
        },
        "answer": "B"
    },
    {
        "question": "The app has zero tickets. What should resolution percentage display?",
        "options": {
            "A": "Crash",
            "B": "100%",
            "C": "0%",
            "D": "Divide by one without explanation"
        },
        "answer": "C"
    },
    {
        "question": "Filter title='wifi', category='Network', status='open'. Which records should match?",
        "options": {
            "A": "Any record matching one filter",
            "B": "Only records matching all supplied filters",
            "C": "All network records",
            "D": "All open records"
        },
        "answer": "B"
    },
    {
        "question": "A resolved ticket receives 'Add note'. What should happen?",
        "options": {
            "A": "Append anyway",
            "B": "Delete old notes",
            "C": "Reject until reopened",
            "D": "Change status silently"
        },
        "answer": "C"
    },
    {
        "question": "The JSON file includes two tickets with the same ID. What should load do?",
        "options": {
            "A": "Keep both",
            "B": "Replace memory with duplicates",
            "C": "Reject the load without changing current memory",
            "D": "Rename IDs silently"
        },
        "answer": "C"
    },
    {
        "question": "A PR changes validation but has no negative-case tests. Best review action?",
        "options": {
            "A": "Approve because it runs",
            "B": "Request focused tests and reasoning",
            "C": "Merge immediately",
            "D": "Ask AI to approve it"
        },
        "answer": "B"
    }
]

def validate_answer(answer):
    if not isinstance(answer, str):
        raise ValueError("Answer must be a string")

    answer = answer.strip().upper()

    if answer not in ("A", "B", "C", "D"):
        raise ValueError("Invalid choice. Enter A, B, C or D.")

    return answer


def check_answer(question, answer):
    answer = validate_answer(answer)

    return answer == question["answer"]


def calculate_score(answers):
    if len(answers) != len(QUESTIONS):
        raise ValueError("You must answer all six questions")

    score = 0

    for question, answer in zip(QUESTIONS, answers):
        if check_answer(question, answer):
            score += 1

    return score


def display_question(question, number):
    print(f"\nQuestion {number}")
    print(question["question"])

    for option, description in question["options"].items():
        print(f"{option}. {description}")


def get_answer():
    while True:
        answer = input("\nEnter your answer (A/B/C/D): ")

        try:
            return validate_answer(answer)

        except ValueError as error:
            print(error)


def get_explanations():
    explanations = []

    print("\n=== EXPLAIN YOUR ANSWERS ===")
    print("Explain why you selected your answers for two questions.")

    for question_number in (1, 5):

        print(f"\nQuestion {question_number}")

        question = QUESTIONS[question_number - 1]

        print(question["question"])

        while True:
            explanation = input("Your explanation: ").strip()

            if explanation:
                explanations.append({
                    "question_number": question_number,
                    "explanation": explanation
                })
                break

            print("Explanation cannot be empty.")

    return explanations


def display_result(score):
    print("\n=== YOUR RESULT ===")

    print(f"Your score: {score} out of {len(QUESTIONS)}")

    if score == 6:
        print("Excellent understanding!")

    elif score >= 4:
        print("Good understanding. Keep improving!")

    elif score >= 2:
        print("Fair attempt. Review the CampusFlow concepts.")

    else:
        print("Keep practicing and reviewing the project.")


def run_understanding_check():

    print("\n=== ENGINEERING UNDERSTANDING CHECK ===")

    answers = []

    for number, question in enumerate(QUESTIONS, start=1):

        display_question(question, number)

        answer = get_answer()

        answers.append(answer)

    score = calculate_score(answers)

    display_result(score)

    explanations = get_explanations()

    print("\n=== YOUR EXPLANATIONS ===")

    for item in explanations:
        print(f"\nQuestion {item['question_number']}")
        print(item["explanation"])

    print("\nDiscuss your explanations with your mentor.")

    return score


