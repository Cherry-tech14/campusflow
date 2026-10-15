import json
import tempfile
import unittest

from pathlib import Path

from campusflow.tickets import create_ticket
from campusflow.storage import load_tickets, save_tickets


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.file_path = Path(self.folder.name) / "tickets.json"

        self.tickets = []

        create_ticket(
            self.tickets,
            "Wi-Fi problem",
            "Network",
            "high",
            12,
        )

    def tearDown(self):
        self.folder.cleanup()

    def test_save_and_load(self):
        save_tickets(self.tickets, self.file_path)

        loaded = load_tickets(self.file_path)

        self.assertEqual(loaded, self.tickets)

    def test_missing_file(self):
        loaded = load_tickets(self.file_path)

        self.assertEqual(loaded, [])

    def test_invalid_json(self):
        self.file_path.write_text("{invalid json", encoding="utf-8")

        with self.assertRaises(ValueError):
            load_tickets(self.file_path)

    def test_duplicate_ticket_ids(self):
        duplicate = self.tickets + self.tickets

        with self.assertRaises(ValueError):
            save_tickets(duplicate, self.file_path)

    def test_old_ticket_without_notes(self):
        old_ticket = self.tickets[0].copy()
        old_ticket.pop("notes")

        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump([old_ticket], file)

        loaded = load_tickets(self.file_path)

        self.assertEqual(loaded[0]["notes"], [])

    def test_invalid_save_preserves_file(self):
        save_tickets(self.tickets, self.file_path)

        with open(self.file_path, "r", encoding="utf-8") as file:
            original = file.read()

        with self.assertRaises(ValueError):
            save_tickets([{"id": "T002"}], self.file_path)

        with open(self.file_path, "r", encoding="utf-8") as file:
            after = file.read()

        self.assertEqual(original, after)


if __name__ == "__main__":
    unittest.main()