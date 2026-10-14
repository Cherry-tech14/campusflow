import unittest

from campusflow.queue import get_work_queue


class TestWorkQueue(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {"id": "T001", "priority": "critical", "status": "resolved"},
            {"id": "T002", "priority": "high", "status": "open"},
            {"id": "T003", "priority": "medium", "status": "in_progress"},
            {"id": "T004", "priority": "critical", "status": "open"},
            {"id": "T005", "priority": "low", "status": "open"},
        ]

    def test_empty_list(self):
        result = get_work_queue([])
        self.assertEqual(result, [])

    def test_only_open_tickets(self):
        result = get_work_queue(self.tickets)

        ids = []

        for ticket in result:
            ids.append(ticket["id"])

        self.assertEqual(ids, ["T004", "T002", "T005"])

    def test_resolved_tickets_excluded(self):
        result = get_work_queue(self.tickets)

        for ticket in result:
            self.assertNotEqual(ticket["status"], "resolved")

    def test_in_progress_tickets_excluded(self):
        result = get_work_queue(self.tickets)

        for ticket in result:
            self.assertNotEqual(ticket["status"], "in_progress")

    def test_critical_first(self):
        result = get_work_queue(self.tickets)
        self.assertEqual(result[0]["id"], "T004")

    def test_numeric_ticket_id_sorting(self):
        tickets = [
            {"id": "T010", "priority": "high", "status": "open"},
            {"id": "T002", "priority": "high", "status": "open"},
        ]

        result = get_work_queue(tickets)

        self.assertEqual(result[0]["id"], "T002")
        self.assertEqual(result[1]["id"], "T010")

    def test_original_list_not_reordered(self):
        original_ids = []

        for ticket in self.tickets:
            original_ids.append(ticket["id"])

        get_work_queue(self.tickets)

        after_ids = []

        for ticket in self.tickets:
            after_ids.append(ticket["id"])

        self.assertEqual(original_ids, after_ids)


if __name__ == "__main__":
    unittest.main()