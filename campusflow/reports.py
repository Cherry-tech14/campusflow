from campusflow.validation import (
    CATEGORIES,
    STATUSES,
    PRIORITIES,
)


def generate_report(tickets):
    report = {
        "total": len(tickets),
        "by_status": {
            status: 0 for status in STATUSES
        },
        "by_priority": {
            priority: 0 for priority in PRIORITIES
        },
        "by_category": {
            category: 0 for category in CATEGORIES
        },
        "unresolved": 0,
        "resolved": 0,
        "resolution_percentage": 0.0,
    }

    for ticket in tickets:
        status = ticket["status"]
        priority = ticket["priority"]
        category = ticket["category"]

        report["by_status"][status] += 1
        report["by_priority"][priority] += 1
        report["by_category"][category] += 1

    report["unresolved"] = (
        report["by_status"]["open"]
        + report["by_status"]["in_progress"]
    )

    report["resolved"] = report["by_status"]["resolved"]

    if report["total"] > 0:
        report["resolution_percentage"] = round(
            report["resolved"] / report["total"] * 100,
            2,
        )

    return report