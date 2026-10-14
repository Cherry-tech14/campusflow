import unittest

from campusflow.tickets import create_ticket
from campusflow.workflow import assign_ticket, update_status


class TestWorkflow(unittest.TestCase):

    def setUp(self):
        self.tickets = []

        create_ticket(
            self.tickets,
            "Network problem",
            "Network",
            "high",
            5,
        )

    def test_assign_ticket(self):
        ticket = assign_ticket(self.tickets, "T001", "John")
        self.assertEqual(ticket["assigned_to"], "John")

    def test_cannot_start_unassigned_ticket(self):
        with self.assertRaises(ValueError):
            update_status(self.tickets, "T001", "in_progress")

    def test_start_assigned_ticket(self):
        assign_ticket(self.tickets, "T001", "John")

        ticket = update_status(
            self.tickets,
            "T001",
            "in_progress",
        )

        self.assertEqual(ticket["status"], "in_progress")

    def test_resolve_ticket(self):
        assign_ticket(self.tickets, "T001", "John")
        update_status(self.tickets, "T001", "in_progress")

        ticket = update_status(self.tickets, "T001", "resolved")

        self.assertEqual(ticket["status"], "resolved")

    def test_reopen_ticket(self):
        assign_ticket(self.tickets, "T001", "John")
        update_status(self.tickets, "T001", "in_progress")
        update_status(self.tickets, "T001", "resolved")

        ticket = update_status(self.tickets, "T001", "open")

        self.assertEqual(ticket["status"], "open")

    def test_cannot_assign_resolved_ticket(self):
        assign_ticket(self.tickets, "T001", "John")
        update_status(self.tickets, "T001", "in_progress")
        update_status(self.tickets, "T001", "resolved")

        with self.assertRaises(ValueError):
            assign_ticket(self.tickets, "T001", "Mary")


if __name__ == "__main__":
    unittest.main()