import unittest
from copy import deepcopy

from campusflow.tickets import create_ticket
from campusflow.notes import add_note, view_notes
from campusflow.workflow import assign_ticket, update_status


class TestNotes(unittest.TestCase):

    def setUp(self):
        self.tickets = []

        create_ticket(
            self.tickets,
            "Laptop failure",
            "Hardware",
            "medium",
            3,
        )

    def test_add_valid_note(self):
        note = add_note(
            self.tickets,
            "T001",
            "Technician A",
            "Laptop inspected",
        )

        self.assertEqual(note["note_id"], "N001")
        self.assertEqual(len(view_notes(self.tickets, "T001")), 1)

    def test_invalid_note_does_not_consume_id(self):
        before = deepcopy(self.tickets)

        with self.assertRaises(ValueError):
            add_note(self.tickets, "T001", "Tech", "Hi")

        self.assertEqual(self.tickets, before)

        note = add_note(
            self.tickets,
            "T001",
            "Tech",
            "Laptop inspected",
        )

        self.assertEqual(note["note_id"], "N001")

    def test_resolved_ticket_rejects_note(self):
        assign_ticket(self.tickets, "T001", "Tech")
        update_status(self.tickets, "T001", "in_progress")
        update_status(self.tickets, "T001", "resolved")

        before = deepcopy(self.tickets)

        with self.assertRaises(ValueError):
            add_note(
                self.tickets,
                "T001",
                "Tech",
                "Another update",
            )

        self.assertEqual(self.tickets, before)

    def test_note_after_reopening(self):
        first = add_note(
            self.tickets, "T001", "Tech", "Initial inspection"
        )

        assign_ticket(self.tickets, "T001", "Tech")
        update_status(self.tickets, "T001", "in_progress")
        update_status(self.tickets, "T001", "resolved")
        update_status(self.tickets, "T001", "open")

        second = add_note(
            self.tickets, "T001", "Tech", "Follow-up inspection"
        )

        self.assertEqual(first["note_id"], "N001")
        self.assertEqual(second["note_id"], "N002")
        self.assertEqual(len(view_notes(self.tickets, "T001")), 2)


if __name__ == "__main__":
    unittest.main()