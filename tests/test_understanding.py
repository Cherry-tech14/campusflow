import unittest

from unittest.mock import patch

from campusflow.understanding_checks import (
    QUESTIONS,
    check_answer,
    calculate_score,
    run_understanding_check,
)


class TestUnderstandingChecks(unittest.TestCase):

    def test_six_questions(self):
        self.assertEqual(len(QUESTIONS), 6)

    def test_correct_answer(self):
        question = QUESTIONS[0]
        result = check_answer(question, question["answer"])

        self.assertTrue(result)

    def test_lowercase_answer(self):
        question = QUESTIONS[0]
        answer = question["answer"].lower()

        result = check_answer(question, answer)

        self.assertTrue(result)

    def test_wrong_answer(self):
        question = QUESTIONS[0]

        result = check_answer(question, "A")

        self.assertFalse(result)

    def test_perfect_score(self):
        answers = []

        for question in QUESTIONS:
            answers.append(question["answer"])

        score = calculate_score(answers)

        self.assertEqual(score, 6)

    def test_zero_score(self):
        answers = ["A", "B", "A", "A", "B", "A"]

        score = calculate_score(answers)

        self.assertEqual(score, 0)

    def test_invalid_answer_count(self):
        with self.assertRaises(ValueError):
            calculate_score(["A"])

    @patch("builtins.input")
    def test_run_quiz(self, mock_input):
        answers = []

        for question in QUESTIONS:
            answers.append(question["answer"])

        mock_input.side_effect = answers

        score = run_understanding_check()

        self.assertEqual(score, 6)


if __name__ == "__main__":
    unittest.main()