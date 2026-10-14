import unittest

from campusflow.tickets import create_ticket
from campusflow.workflow import assign_ticket, update_status
from campusflow.notes import add_note, view_notes


class TestNotes(unittest.TestCase):

    def setUp(self):
        self.tickets = []

        create_ticket(
            self.tickets,
            "Printer problem",
            "Hardware",
            "medium",
            2,
        )

    def test_add_note(self):
        note = add_note(
            self.tickets,
            "T001",
            "John",
            "Printer inspection completed",
        )

        self.assertEqual(note["note_id"], "N001")

    def test_multiple_notes(self):
        add_note(self.tickets, "T001", "John", "Checking printer")
        add_note(self.tickets, "T001", "Mary", "Printer repaired")

        notes = view_notes(self.tickets, "T001")

        self.assertEqual(len(notes), 2)
        self.assertEqual(notes[1]["note_id"], "N002")

    def test_invalid_message(self):
        with self.assertRaises(ValueError):
            add_note(self.tickets, "T001", "John", "Hi")

    def test_cannot_note_resolved_ticket(self):
        assign_ticket(self.tickets, "T001", "John")
        update_status(self.tickets, "T001", "in_progress")
        update_status(self.tickets, "T001", "resolved")

        with self.assertRaises(ValueError):
            add_note(
                self.tickets,
                "T001",
                "John",
                "Another inspection",
            )

    def test_view_notes_returns_copy(self):
        add_note(self.tickets, "T001", "John", "Checking printer")

        notes = view_notes(self.tickets, "T001")
        notes.clear()

        self.assertEqual(len(self.tickets[0]["notes"]), 1)


if __name__ == "__main__":
    unittest.main()