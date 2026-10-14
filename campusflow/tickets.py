from campusflow.validation import (
    validate_title,
    validate_category,
    validate_urgency,
    validate_affected_users,
    validate_ticket_id,
)


def calculate_priority(urgency, affected_users):
    urgency = validate_urgency(urgency)
    affected_users = validate_affected_users(affected_users)

    if urgency == "high" and affected_users >= 10:
        return "critical"

    if urgency == "high" or affected_users >= 10:
        return "high"

    if urgency == "medium" or affected_users >= 3:
        return "medium"

    return "low"


def next_ticket_id(tickets):
    highest_id = 0

    for ticket in tickets:
        ticket_id = validate_ticket_id(ticket["id"])
        number = int(ticket_id[1:])
        highest_id = max(highest_id, number)

    return f"T{highest_id + 1:03d}"


def create_ticket(tickets, title, category, urgency, affected_users):
    # Validate everything before modifying the collection.
    title = validate_title(title)
    category = validate_category(category)
    urgency = validate_urgency(urgency)
    affected_users = validate_affected_users(affected_users)

    priority = calculate_priority(urgency, affected_users)
    ticket_id = next_ticket_id(tickets)

    new_ticket = {
        "id": ticket_id,
        "title": title,
        "category": category,
        "urgency": urgency,
        "affected_users": affected_users,
        "priority": priority,
        "status": "open",
        "assigned_to": None,
        "notes": [],
    }

    tickets.append(new_ticket)

    return new_ticket