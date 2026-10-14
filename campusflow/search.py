from campusflow.validation import (
    CATEGORIES,
    STATUSES,
    PRIORITIES,
)


def search_tickets(
    tickets,
    title="",
    category="",
    status="",
    priority="",
):
    filters = (title, category, status, priority)

    if any(not isinstance(value, str) for value in filters):
        raise ValueError("Search filters must be text")

    title = title.strip().casefold()
    category = category.strip().casefold()
    status = status.strip().casefold()
    priority = priority.strip().casefold()

    if category and category not in {
        item.casefold() for item in CATEGORIES
    }:
        raise ValueError("Invalid category filter")

    if status and status not in STATUSES:
        raise ValueError("Invalid status filter")

    if priority and priority not in PRIORITIES:
        raise ValueError("Invalid priority filter")

    results = []

    for ticket in tickets:
        if title and title not in ticket["title"].casefold():
            continue

        if category and category != ticket["category"].casefold():
            continue

        if status and status != ticket["status"]:
            continue

        if priority and priority != ticket["priority"]:
            continue

        results.append(ticket)

    return results


def sort_search_results(tickets):
    priority_order = {
        "critical": 0,
        "high": 1,
        "medium": 2,
        "low": 3,
    }

    return sorted(
        tickets,
        key=lambda ticket: (
            priority_order[ticket["priority"]],
            int(ticket["id"][1:]),
        ),
    )