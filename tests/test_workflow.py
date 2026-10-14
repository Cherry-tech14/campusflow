import unittest
from copy import deepcopy

from campusflow.tickets import create_ticket
from campusflow.workflow import (
    assign_ticket,
    update_status,
)


class TestWorkflow(unittest.TestCase):

    def setUp(self):
        self.tickets = []

        create_ticket(
            self.tickets,
            "Network failure",
            "Network",
            "high",
            10,
        )

    def test_unassigned_ticket_cannot_start(self):
        before = deepcopy(self.tickets)

        with self.assertRaises(ValueError):
            update_status(
                self.tickets,
                "T001",
                "in_progress",
            )

        self.assertEqual(self.tickets, before)

    def test_valid_ticket_lifecycle(self):
        assign_ticket(self.tickets, "T001", "Technician A")

        update_status(
            self.tickets, "T001", "in_progress"
        )

        self.assertEqual(
            self.tickets[0]["status"], "in_progress"
        )

        update_status(
            self.tickets, "T001", "resolved"
        )

        self.assertEqual(
            self.tickets[0]["status"], "resolved"
        )

        update_status(
            self.tickets, "T001", "open"
        )

        self.assertEqual(
            self.tickets[0]["status"], "open"
        )

    def test_resolved_ticket_cannot_be_assigned(self):
        assign_ticket(self.tickets, "T001", "Technician A")
        update_status(self.tickets, "T001", "in_progress")
        update_status(self.tickets, "T001", "resolved")

        before = deepcopy(self.tickets)

        with self.assertRaises(ValueError):
            assign_ticket(
                self.tickets, "T001", "Technician B"
            )

        self.assertEqual(self.tickets, before)

    def test_invalid_transition_preserves_data(self):
        before = deepcopy(self.tickets)

        with self.assertRaises(ValueError):
            update_status(self.tickets, "T001", "resolved")

        self.assertEqual(self.tickets, before)


if __name__ == "__main__":
    unittest.main()