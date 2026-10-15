import unittest

from campusflow.reports import generate_report


class TestReports(unittest.TestCase):

    def setUp(self):
        self.tickets = [
            {
                "id": "T001",
                "status": "open",
                "priority": "critical",
                "category": "Network",
            },
            {
                "id": "T002",
                "status": "resolved",
                "priority": "high",
                "category": "Hardware",
            },
            {
                "id": "T003",
                "status": "in_progress",
                "priority": "medium",
                "category": "Software",
            },
        ]

    def test_total_tickets(self):
        report = generate_report(self.tickets)
        self.assertEqual(report["total"], 3)

    def test_status_count(self):
        report = generate_report(self.tickets)
        self.assertEqual(report["by_status"]["open"], 1)

    def test_priority_count(self):
        report = generate_report(self.tickets)
        self.assertEqual(report["by_priority"]["critical"], 1)

    def test_category_count(self):
        report = generate_report(self.tickets)
        self.assertEqual(report["by_category"]["Network"], 1)

    def test_resolved_count(self):
        report = generate_report(self.tickets)
        self.assertEqual(report["resolved"], 1)

    def test_unresolved_count(self):
        report = generate_report(self.tickets)
        self.assertEqual(report["unresolved"], 2)

    def test_resolution_percentage(self):
        report = generate_report(self.tickets)

        self.assertAlmostEqual(
            report["resolution_percentage"],
            33.3333333333,
        )

    def test_empty_list(self):
        report = generate_report([])

        self.assertEqual(report["total"], 0)
        self.assertEqual(report["resolution_percentage"], 0)


if __name__ == "__main__":
    unittest.main()