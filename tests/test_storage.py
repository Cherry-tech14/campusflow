import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

from campusflow.tickets import create_ticket
from campusflow.notes import add_note
from campusflow.storage import (
    save_tickets,
    load_tickets,
    reload_tickets,
)


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()

        self.file_path = (
            Path(self.temp_dir.name) / "tickets.json"
        )

        self.tickets = []

        create_ticket(
            self.tickets,
            "Network issue",
            "Network",
            "high",
            10,
        )

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_save_and_load(self):
        save_tickets(self.tickets, self.file_path)

        loaded = load_tickets(self.file_path)

        self.assertEqual(loaded, self.tickets)

    def test_notes_survive_reload(self):
        add_note(
            self.tickets,
            "T001",
            "Technician A",
            "Router inspected",
        )

        save_tickets(self.tickets, self.file_path)

        loaded = load_tickets(self.file_path)

        self.assertEqual(
            loaded[0]["notes"][0]["note_id"],
            "N001",
        )

    def test_corrupted_json_preserves_memory(self):
        self.file_path.write_text(
            "{invalid json",
            encoding="utf-8",
        )

        before = deepcopy(self.tickets)

        with self.assertRaises(ValueError):
            reload_tickets(self.tickets, self.file_path)

        self.assertEqual(self.tickets, before)

    def test_duplicate_ids_preserve_memory(self):
        duplicate = deepcopy(self.tickets[0])

        self.file_path.write_text(
            json.dumps([self.tickets[0], duplicate]),
            encoding="utf-8",
        )

        before = deepcopy(self.tickets)

        with self.assertRaises(ValueError):
            reload_tickets(self.tickets, self.file_path)

        self.assertEqual(self.tickets, before)

    def test_ids_continue_after_reload(self):
        save_tickets(self.tickets, self.file_path)

        loaded = load_tickets(self.file_path)

        new_ticket = create_ticket(
            loaded,
            "Software issue",
            "Software",
            "low",
            1,
        )

        self.assertEqual(new_ticket["id"], "T002")


if __name__ == "__main__":
    unittest.main()