from campusflow.validation import (
    validate_category,
    validate_status,
    validate_priority,
)

from campusflow.queue import PRIORITY_ORDER


def search_tickets(
    tickets,
    title="",
    category="",
    status="",
    priority="",
):
    if not isinstance(title, str):
        raise ValueError("Title filter must be text")

    if not isinstance(category, str):
        raise ValueError("Category filter must be text")

    if not isinstance(status, str):
        raise ValueError("Status filter must be text")

    if not isinstance(priority, str):
        raise ValueError("Priority filter must be text")

    title = title.strip().lower()
    category = category.strip()
    status = status.strip()
    priority = priority.strip().lower()

    if category != "":
        category = validate_category(category)

    if status != "":
        status = validate_status(status)

    if priority != "":
        priority = validate_priority(priority)

    results = []

    for ticket in tickets:
        matches = True

        if title != "":
            if title not in ticket["title"].lower():
                matches = False

        if category != "":
            if ticket["category"] != category:
                matches = False

        if status != "":
            if ticket["status"] != status:
                matches = False

        if priority != "":
            if ticket["priority"] != priority:
                matches = False

        if matches:
            results.append(ticket)

    return results


def sort_search_results(tickets):
    results = tickets.copy()

    for i in range(len(results)):
        for j in range(i + 1, len(results)):

            first = results[i]
            second = results[j]

            first_priority = PRIORITY_ORDER[first["priority"]]
            second_priority = PRIORITY_ORDER[second["priority"]]

            should_swap = False

            if first_priority > second_priority:
                should_swap = True

            elif first_priority == second_priority:
                first_id = int(first["id"][1:])
                second_id = int(second["id"][1:])

                if first_id > second_id:
                    should_swap = True

            if should_swap:
                results[i] = second
                results[j] = first

    return results