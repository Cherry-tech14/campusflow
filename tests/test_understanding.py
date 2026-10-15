import unittest
from unittest.mock import patch
from io import StringIO

from campusflow.understanding_checks import (
    QUESTIONS,
    validate_answer,
    check_answer,
    calculate_score,
    display_question,
    get_answer,
    get_explanations,
    display_result,
    run_understanding_check,
)


class TestUnderstandingChecks(unittest.TestCase):

    # TEST 1: The quiz must contain exactly six questions

    def test_six_questions(self):
        self.assertEqual(len(QUESTIONS), 6)

    # TEST 2: Every question must have four options

    def test_four_options(self):
        for question in QUESTIONS:
            self.assertEqual(
                set(question["options"].keys()),
                {"A", "B", "C", "D"}
            )

    # TEST 3: Correct answers must match the project question

    def test_correct_answers(self):
        expected_answers = ["B", "C", "B", "C", "C", "B"]

        actual_answers = []

        for question in QUESTIONS:
            actual_answers.append(question["answer"])

        self.assertEqual(actual_answers, expected_answers)

    # TEST 4: A correct answer returns True

    def test_correct_answer(self):
        question = QUESTIONS[0]

        result = check_answer(question, "B")

        self.assertTrue(result)

    # TEST 5: A wrong answer returns False

    def test_wrong_answer(self):
        question = QUESTIONS[0]

        result = check_answer(question, "A")

        self.assertFalse(result)

    # TEST 6: Lowercase answers must be accepted

    def test_lowercase_answer(self):
        question = QUESTIONS[0]

        result = check_answer(question, "b")

        self.assertTrue(result)

    # TEST 7: Invalid answers must be rejected

    def test_invalid_answer(self):
        with self.assertRaises(ValueError):
            validate_answer("X")

    # TEST 8: Empty answers must be rejected

    def test_empty_answer(self):
        with self.assertRaises(ValueError):
            validate_answer("")

    # TEST 9: Valid answers must be normalized

    def test_answer_normalization(self):
        result = validate_answer(" b ")

        self.assertEqual(result, "B")

    # TEST 10: All correct answers produce six points

    def test_perfect_score(self):
        answers = ["B", "C", "B", "C", "C", "B"]

        result = calculate_score(answers)

        self.assertEqual(result, 6)

    # TEST 11: All wrong answers produce zero points

    def test_zero_score(self):
        answers = ["A", "A", "A", "A", "A", "A"]

        result = calculate_score(answers)

        self.assertEqual(result, 0)

    # TEST 12: Partially correct answers produce correct score

    def test_partial_score(self):
        answers = ["B", "C", "A", "A", "A", "A"]

        result = calculate_score(answers)

        self.assertEqual(result, 2)

    # TEST 13: Missing answers must be rejected

    def test_invalid_answer_count(self):
        answers = ["B", "C", "B"]

        with self.assertRaises(ValueError):
            calculate_score(answers)

    # TEST 14: Too many answers must be rejected

    def test_too_many_answers(self):
        answers = ["B", "C", "B", "C", "C", "B", "A"]

        with self.assertRaises(ValueError):
            calculate_score(answers)

    # TEST 15: Invalid input must trigger a retry

    @patch("builtins.input", side_effect=["X", "B"])
    def test_invalid_input_retry(self, mock_input):
        result = get_answer()

        self.assertEqual(result, "B")
        self.assertEqual(mock_input.call_count, 2)

    # TEST 16: Two explanations must be collected

    @patch(
        "builtins.input",
        side_effect=[
            "An unassigned ticket cannot enter in_progress.",
            "Duplicate ticket IDs must be rejected."
        ]
    )
    def test_two_explanations(self, mock_input):
        explanations = get_explanations()

        self.assertEqual(len(explanations), 2)

        self.assertEqual(
            explanations[0]["question_number"],
            1
        )

        self.assertEqual(
            explanations[1]["question_number"],
            5
        )

    # TEST 17: Blank explanations must trigger a retry

    @patch(
        "builtins.input",
        side_effect=[
            "",
            "The ticket must be assigned first.",
            "Duplicate IDs must not overwrite existing data."
        ]
    )
    def test_blank_explanation_retry(self, mock_input):
        explanations = get_explanations()

        self.assertEqual(len(explanations), 2)
        self.assertEqual(mock_input.call_count, 3)

    # TEST 18: Questions must be displayed with four options

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_question(self, mock_output):
        display_question(QUESTIONS[0], 1)

        output = mock_output.getvalue()

        self.assertIn("Question 1", output)
        self.assertIn("A.", output)
        self.assertIn("B.", output)
        self.assertIn("C.", output)
        self.assertIn("D.", output)

    # TEST 19: Final result must display the score

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_result(self, mock_output):
        display_result(6)

        output = mock_output.getvalue()

        self.assertIn("6 out of 6", output)

    # TEST 20: Complete quiz must work correctly

    @patch(
        "builtins.input",
        side_effect=[
            "B",
            "C",
            "B",
            "C",
            "C",
            "B",
            "A ticket must be assigned before starting work.",
            "Duplicate IDs would make ticket records unreliable."
        ]
    )
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_understanding_check(
        self,
        mock_output,
        mock_input
    ):
        result = run_understanding_check()

        self.assertEqual(result, 6)

        output = mock_output.getvalue()

        self.assertIn("6 out of 6", output)
        self.assertIn("YOUR EXPLANATIONS", output)


if __name__ == "__main__":
    unittest.main()