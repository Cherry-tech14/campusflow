import unittest
from copy import deepcopy

from campusflow.queue import get_work_queue


class TestWorkQueue(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {
                "id": "T001",
                "title": "Internet failure",
                "priority": "critical",
                "status": "resolved",
            },
            {
                "id": "T002",
                "title": "Laptop issue",
                "priority": "high",
                "status": "open",
            },
            {
                "id": "T003",
                "title": "Software installation",
                "priority": "medium",
                "status": "in_progress",
            },
            {
                "id": "T004",
                "title": "Wi-Fi connection",
                "priority": "critical",
                "status": "open",
            },
            {
                "id": "T005",
                "title": "Printer issue",
                "priority": "low",
                "status": "open",
            },
        ]

    # TEST 1: Empty list

    def test_empty_ticket_list(self):
        result = get_work_queue([])

        self.assertEqual(result, [])

    # TEST 2: Only open tickets should appear

    def test_only_open_tickets(self):
        result = get_work_queue(self.tickets)

        ticket_ids = []

        for ticket in result:
            ticket_ids.append(ticket["id"])

        self.assertEqual(
            ticket_ids,
            ["T004", "T002", "T005"]
        )

    # TEST 3: Resolved tickets should not appear

    def test_resolved_tickets_excluded(self):
        result = get_work_queue(self.tickets)

        for ticket in result:
            self.assertNotEqual(ticket["status"], "resolved")

    # TEST 4: In-progress tickets should not appear

    def test_in_progress_tickets_excluded(self):
        result = get_work_queue(self.tickets)

        for ticket in result:
            self.assertNotEqual(ticket["status"], "in_progress")

    # TEST 5: Critical tickets should come first

    def test_critical_tickets_first(self):
        result = get_work_queue(self.tickets)

        self.assertEqual(result[0]["id"], "T004")

    # TEST 6: Tickets should be sorted by priority

    def test_priority_order(self):
        result = get_work_queue(self.tickets)

        priorities = []

        for ticket in result:
            priorities.append(ticket["priority"])

        self.assertEqual(
            priorities,
            ["critical", "high", "low"]
        )

    # TEST 7: Tickets with the same priority
    # should be sorted using their ID numbers

    def test_numeric_ticket_id_sorting(self):
        tickets = [
            {
                "id": "T010",
                "title": "Issue 10",
                "priority": "high",
                "status": "open",
            },
            {
                "id": "T002",
                "title": "Issue 2",
                "priority": "high",
                "status": "open",
            },
            {
                "id": "T001",
                "title": "Issue 1",
                "priority": "high",
                "status": "open",
            },
        ]

        result = get_work_queue(tickets)

        ticket_ids = []

        for ticket in result:
            ticket_ids.append(ticket["id"])

        self.assertEqual(
            ticket_ids,
            ["T001", "T002", "T010"]
        )

    # TEST 8: Original ticket list must not change

    def test_original_list_not_modified(self):
        original_tickets = deepcopy(self.tickets)

        get_work_queue(self.tickets)

        self.assertEqual(self.tickets, original_tickets)


if __name__ == "__main__":
    unittest.main()