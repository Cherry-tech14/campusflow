import unittest

from campusflow.search import (
    search_tickets,
    sort_search_results,
)


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {
                "id": "T001",
                "title": "Internet failure",
                "category": "Network",
                "status": "open",
                "priority": "critical",
            },
            {
                "id": "T002",
                "title": "Laptop broken",
                "category": "Hardware",
                "status": "resolved",
                "priority": "medium",
            },
            {
                "id": "T003",
                "title": "Wi-Fi problem",
                "category": "Network",
                "status": "open",
                "priority": "high",
            },
        ]

    def test_search_by_title(self):
        result = search_tickets(self.tickets, title="internet")

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "T001")

    def test_search_by_category(self):
        result = search_tickets(self.tickets, category="network")
        self.assertEqual(len(result), 2)

    def test_search_by_status(self):
        result = search_tickets(self.tickets, status="resolved")
        self.assertEqual(result[0]["id"], "T002")

    def test_search_by_priority(self):
        result = search_tickets(self.tickets, priority="critical")
        self.assertEqual(result[0]["id"], "T001")

    def test_multiple_filters(self):
        result = search_tickets(
            self.tickets,
            category="Network",
            status="open",
            priority="high",
        )

        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]["id"], "T003")

    def test_no_results(self):
        result = search_tickets(self.tickets, title="printer")
        self.assertEqual(result, [])

    def test_invalid_category(self):
        with self.assertRaises(ValueError):
            search_tickets(self.tickets, category="Unknown")

    def test_sort_results(self):
        result = sort_search_results(self.tickets)

        ids = []

        for ticket in result:
            ids.append(ticket["id"])

        self.assertEqual(ids, ["T001", "T003", "T002"])


if __name__ == "__main__":
    unittest.main()