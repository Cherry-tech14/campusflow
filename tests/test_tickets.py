import unittest
from copy import deepcopy

from campusflow.tickets import (
    create_ticket,
    calculate_priority,
    next_ticket_id,
)


class TestTickets(unittest.TestCase):

    def test_create_ticket(self):
        tickets = []

        ticket = create_ticket(
            tickets, "Wi-Fi failure", "Network", "high", 15
        )

        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertEqual(ticket["notes"], [])

    def test_priority_rules(self):
        cases = [
            ("high", 10, "critical"),
            ("high", 9, "high"),
            ("low", 10, "high"),
            ("medium", 3, "medium"),
            ("low", 2, "low"),
        ]

        for urgency, users, expected in cases:
            with self.subTest(urgency=urgency, users=users):
                self.assertEqual(
                    calculate_priority(urgency, users),
                    expected,
                )

    def test_invalid_affected_users(self):
        for value in (0, -1, 2.5, True, "10"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    calculate_priority("high", value)

    def test_invalid_create_does_not_modify_tickets(self):
        tickets = []
        before = deepcopy(tickets)

        with self.assertRaises(ValueError):
            create_ticket(
                tickets, "", "Network", "high", 10
            )

        self.assertEqual(tickets, before)

    def test_next_ticket_id_with_gap(self):
        tickets = [
            {"id": "T001"},
            {"id": "T003"},
        ]

        self.assertEqual(next_ticket_id(tickets), "T004")


if __name__ == "__main__":
    unittest.main()