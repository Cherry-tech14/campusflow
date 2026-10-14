from campusflow.validation import (
    validate_staff,
    validate_status,
)


def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    raise ValueError("Ticket not found")


def assign_ticket(tickets, ticket_id, staff_name):
    ticket = find_ticket(tickets, ticket_id)

    if ticket["status"] == "resolved":
        raise ValueError("Cannot assign a resolved ticket")

    staff_name = validate_staff(staff_name)

    ticket["assigned_to"] = staff_name

    return ticket


def can_transition(ticket, new_status):
    validate_status(new_status)

    current_status = ticket["status"]

    if current_status == "open":
        return (
            new_status == "in_progress"
            and ticket["assigned_to"] is not None
        )

    if current_status == "in_progress":
        return new_status == "resolved"

    if current_status == "resolved":
        return new_status == "open"

    return False


def update_status(tickets, ticket_id, new_status):
    ticket = find_ticket(tickets, ticket_id)

    if not isinstance(new_status, str):
        raise ValueError("Invalid status")

    new_status = new_status.strip().lower()

    validate_status(new_status)

    if not can_transition(ticket, new_status):
        raise ValueError("Invalid ticket status transition")

    ticket["status"] = new_status

    return ticketfrom campusflow.validation import (
    validate_staff,
    validate_status,
)


def find_ticket(tickets, ticket_id):
    for ticket in tickets:
        if ticket["id"] == ticket_id:
            return ticket

    raise ValueError("Ticket not found")


def assign_ticket(tickets, ticket_id, staff_name):
    ticket = find_ticket(tickets, ticket_id)

    if ticket["status"] == "resolved":
        raise ValueError("Cannot assign a resolved ticket")

    staff_name = validate_staff(staff_name)

    ticket["assigned_to"] = staff_name

    return ticket


def can_transition(ticket, new_status):
    validate_status(new_status)

    current_status = ticket["status"]

    if current_status == "open":
        return (
            new_status == "in_progress"
            and ticket["assigned_to"] is not None
        )

    if current_status == "in_progress":
        return new_status == "resolved"

    if current_status == "resolved":
        return new_status == "open"

    return False


def update_status(tickets, ticket_id, new_status):
    ticket = find_ticket(tickets, ticket_id)

    if not isinstance(new_status, str):
        raise ValueError("Invalid status")

    new_status = new_status.strip().lower()

    validate_status(new_status)

    if not can_transition(ticket, new_status):
        raise ValueError("Invalid ticket status transition")

    ticket["status"] = new_status

    return ticket