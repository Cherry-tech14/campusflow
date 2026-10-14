from campusflow.validation import (
    validate_title,
    validate_category,
    validate_urgency,
    validate_affected_users,
)


def calculate_priority(urgency, affected_users):
    urgency = validate_urgency(urgency)
    affected_users = validate_affected_users(affected_users)

    if urgency == "high" and affected_users >= 10:
        return "critical"

    elif urgency == "high":
        return "high"

    elif urgency == "medium":
        return "medium"

    else:
        return "low"


def next_ticket_id(tickets):
    highest_number = 0

    for ticket in tickets:
        ticket_id = ticket["id"]

        number = int(ticket_id[1:])

        if number > highest_number:
            highest_number = number

    next_number = highest_number + 1

    return f"T{next_number:03d}"


def create_ticket(tickets, title, category, urgency, affected_users):
    title = validate_title(title)
    category = validate_category(category)
    urgency = validate_urgency(urgency)
    affected_users = validate_affected_users(affected_users)

    priority = calculate_priority(urgency, affected_users)

    ticket = {
        "id": next_ticket_id(tickets),
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None,
        "notes": [],
    }

    tickets.append(ticket)

    return ticket