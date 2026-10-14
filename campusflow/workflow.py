from campusflow.validation import (
    validate_ticket_id,
    validate_staff,
    validate_status,
)


def find_ticket(tickets, ticket_id):
    validate_ticket_id(ticket_id)

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
    new_status = validate_status(new_status)

    current_status = ticket["status"]

    if current_status == "open":
        if new_status == "in_progress":
            if ticket["assigned_to"] is not None:
                return True

    elif current_status == "in_progress":
        if new_status == "resolved":
            return True

    elif current_status == "resolved":
        if new_status == "open":
            return True

    return False


def update_status(tickets, ticket_id, new_status):
    ticket = find_ticket(tickets, ticket_id)

    new_status = validate_status(new_status)

    allowed = can_transition(ticket, new_status)

    if allowed == False:
        raise ValueError("Invalid ticket status transition")

    ticket["status"] = new_status

    return ticket