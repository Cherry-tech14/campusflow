import unittest

from campusflow.tickets import (
    calculate_priority,
    next_ticket_id,
    create_ticket,
)


class TestTickets(unittest.TestCase):

    def test_critical_priority(self):
        result = calculate_priority("high", 15)
        self.assertEqual(result, "critical")

    def test_high_priority(self):
        result = calculate_priority("high", 3)
        self.assertEqual(result, "high")

    def test_medium_priority(self):
        result = calculate_priority("medium", 5)
        self.assertEqual(result, "medium")

    def test_low_priority(self):
        result = calculate_priority("low", 2)
        self.assertEqual(result, "low")

    def test_next_ticket_id(self):
        tickets = [
            {"id": "T001"},
            {"id": "T003"},
        ]

        result = next_ticket_id(tickets)

        self.assertEqual(result, "T004")

    def test_create_ticket(self):
        tickets = []

        ticket = create_ticket(
            tickets,
            "Internet problem",
            "Network",
            "high",
            15,
        )

        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertEqual(ticket["notes"], [])
        self.assertEqual(len(tickets), 1)

    def test_invalid_title(self):
        tickets = []

        with self.assertRaises(ValueError):
            create_ticket(tickets, "", "Network", "high", 5)

        self.assertEqual(tickets, [])

    def test_invalid_affected_users(self):
        tickets = []

        with self.assertRaises(ValueError):
            create_ticket(tickets, "Laptop problem", "Hardware", "low", 0)

        self.assertEqual(tickets, [])


if __name__ == "__main__":
    unittest.main()