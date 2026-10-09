import unittest

from campusflow.tickets import create_ticket, calculate_priority


class TestTickets(unittest.TestCase):

    def setUp(self):
        self.tickets = []

    # Test priority calculation
    def test_critical_priority(self):
        self.assertEqual(calculate_priority("high", 12), "critical")

    def test_high_priority(self):
        self.assertEqual(calculate_priority("high", 2), "high")

    def test_medium_priority(self):
        self.assertEqual(calculate_priority("low", 4), "medium")

    def test_low_priority(self):
        self.assertEqual(calculate_priority("low", 1), "low")

    # Test ticket creation
    def test_create_ticket(self):
        ticket = create_ticket(
            self.tickets, "Wi-Fi down", "Network", "high", 12
        )

        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])

    # Test empty title
    def test_empty_title(self):
        with self.assertRaises(ValueError):
            create_ticket(self.tickets, "", "Network", "high", 12)

    # Test invalid category
    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            create_ticket(self.tickets, "Wi-Fi down", "Food", "high", 12)

    # Test invalid urgency
    def test_invalid_urgency(self):
        with self.assertRaises(ValueError):
            create_ticket(self.tickets, "Wi-Fi down", "Network", "urgent", 12)

    # Test zero affected users
    def test_zero_users(self):
        with self.assertRaises(ValueError):
            create_ticket(self.tickets, "Wi-Fi down", "Network", "high", 0)

    # Test negative affected users
    def test_negative_users(self):
        with self.assertRaises(ValueError):
            create_ticket(self.tickets, "Wi-Fi down", "Network", "high", -2)

    # Test decimal affected users
    def test_decimal_users(self):
        with self.assertRaises(ValueError):
            create_ticket(self.tickets, "Wi-Fi down", "Network", "high", 2.5)

    # Test text affected users
    def test_text_users(self):
        with self.assertRaises(ValueError):
            create_ticket(self.tickets, "Wi-Fi down", "Network", "high", "five")

    # Test unique ticket IDs
    def test_unique_ids(self):
        first = create_ticket(
            self.tickets, "Wi-Fi down", "Network", "high", 12
        )

        second = create_ticket(
            self.tickets, "Laptop fault", "Hardware", "low", 1
        )

        self.assertEqual(first["id"], "T001")
        self.assertEqual(second["id"], "T002")

    # Test category and urgency normalization
    def test_case_normalization(self):
        ticket = create_ticket(
            self.tickets, "Laptop fault", "hARDware", "HIGH", 2
        )

        self.assertEqual(ticket["category"], "Hardware")
        self.assertEqual(ticket["urgency"], "high")

    # Test that invalid input doesn't create a ticket
    def test_invalid_input_does_not_add_ticket(self):
        with self.assertRaises(ValueError):
            create_ticket(self.tickets, "", "Network", "high", 12)

        self.assertEqual(len(self.tickets), 0)

    # Test IDs after reloading existing tickets
    def test_id_after_reload(self):
        self.tickets = [
            {
                "id": "T005",
                "title": "Old ticket",
                "category": "Network",
                "urgency": "low",
                "affected_users": 1,
                "priority": "low",
                "status": "open",
                "assigned_to": None
            }
        ]

        ticket = create_ticket(
            self.tickets, "New ticket", "Hardware", "high", 2
        )

        self.assertEqual(ticket["id"], "T006")


if __name__ == "__main__":
    unittest.main()