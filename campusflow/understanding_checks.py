QUESTIONS = [
    {
        "question": (
            "Ticket T001 is open and unassigned. "
            "A user tries to move it to in_progress."
        ),
        "options": {
            "A": "Accept",
            "B": "Reject and preserve all data",
            "C": "Resolve it automatically",
            "D": "Remove ticket",
        },
        "answer": "B",
    },
    {
        "question": (
            "The app has zero tickets. "
            "What should resolution percentage display?"
        ),
        "options": {
            "A": "Crash",
            "B": "100%",
            "C": "0%",
            "D": "Divide by one without explanation",
        },
        "answer": "C",
    },
    {
        "question": (
            "Filter title='wifi', category='Network', "
            "status='open'. Which records should match?"
        ),
        "options": {
            "A": "Any record matching one filter",
            "B": "Only records matching all supplied filters",
            "C": "All network records",
            "D": "All open records",
        },
        "answer": "B",
    },
    {
        "question": (
            "A resolved ticket receives 'Add note'. "
            "What should happen?"
        ),
        "options": {
            "A": "Append anyway",
            "B": "Delete old notes",
            "C": "Reject until reopened",
            "D": "Change status silently",
        },
        "answer": "C",
    },
    {
        "question": (
            "The JSON file includes two tickets with the same ID. "
            "What should load do?"
        ),
        "options": {
            "A": "Keep both",
            "B": "Replace memory with duplicates",
            "C": "Reject the load without changing current memory",
            "D": "Rename IDs silently",
        },
        "answer": "C",
    },
    {
        "question": (
            "A PR changes validation but has no negative-case tests. "
            "What is the best review action?"
        ),
        "options": {
            "A": "Approve because it runs",
            "B": "Request focused tests and reasoning",
            "C": "Merge immediately",
            "D": "Ask AI to approve it",
        },
        "answer": "B",
    },
]


def calculate_score(answers, questions=QUESTIONS):
    if len(answers) != len(questions):
        raise ValueError("Incorrect number of answers")

    score = 0

    for answer, question in zip(answers, questions):
        if not isinstance(answer, str):
            raise ValueError("Invalid quiz answer")

        choice = answer.strip().upper()

        if choice not in ("A", "B", "C", "D"):
            raise ValueError("Invalid quiz answer")

        if choice == question["answer"]:
            score += 1

    return score


def get_answer(prompt="Your answer (A/B/C/D): "):
    while True:
        answer = input(prompt).strip().upper()

        if answer in ("A", "B", "C", "D"):
            return answer

        print("Invalid answer. Enter A, B, C or D.")


def run_understanding_check():
    print("\nENGINEERING UNDERSTANDING CHECK")
    print("-" * 40)

    answers = []

    for number, question in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {number}: {question['question']}")

        for letter, option in question["options"].items():
            print(f"{letter}. {option}")

        answer = get_answer()

        answers.append(answer)

        if answer == question["answer"]:
            print("Correct!")
        else:
            print(f"Incorrect. Correct answer: {question['answer']}")

    score = calculate_score(answers)

    print(f"\nFinal Score: {score}/{len(QUESTIONS)}")

    print("\nExplain your reasoning for two questions.")

    explanations = []

    for number in (1, 2):
        while True:
            explanation = input(
                f"Explain your answer to Question {number}: "
            ).strip()

            if explanation:
                explanations.append({
                    "question": number,
                    "explanation": explanation,
                })
                break

            print("Please provide an explanation.")

    print("\nExplanations recorded for mentor discussion.")

    return {
        "score": score,
        "answers": answers,
        "explanations": explanations,
    }