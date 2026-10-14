from campusflow.validation import (
    CATEGORIES,
    STATUSES,
    PRIORITIES,
)


def generate_report(tickets):
    total = len(tickets)

    by_status = {}
    by_priority = {}
    by_category = {}

    for status in STATUSES:
        by_status[status] = 0

    for priority in PRIORITIES:
        by_priority[priority] = 0

    for category in CATEGORIES:
        by_category[category] = 0

    for ticket in tickets:
        status = ticket["status"]
        priority = ticket["priority"]
        category = ticket["category"]

        by_status[status] += 1
        by_priority[priority] += 1
        by_category[category] += 1

    resolved = by_status["resolved"]
    unresolved = total - resolved

    if total > 0:
        resolution_percentage = (resolved / total) * 100
    else:
        resolution_percentage = 0

    report = {
        "total": total,
        "by_status": by_status,
        "by_priority": by_priority,
        "by_category": by_category,
        "resolved": resolved,
        "unresolved": unresolved,
        "resolution_percentage": resolution_percentage,
    }

    return report