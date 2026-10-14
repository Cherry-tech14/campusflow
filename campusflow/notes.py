from campusflow.workflow import find_ticket
from campusflow.validation import (
    validate_note,
    validate_note_id,
)


def next_note_id(ticket):
    highest_id = 0

    for note in ticket["notes"]:
        note_id = validate_note_id(note["note_id"])
        number = int(note_id[1:])
        highest_id = max(highest_id, number)

    return f"N{highest_id + 1:03d}"


def add_note(tickets, ticket_id, author, message):
    ticket = find_ticket(tickets, ticket_id)

    if ticket["status"] == "resolved":
        raise ValueError("Cannot add notes to a resolved ticket")

    if ticket["status"] not in ("open", "in_progress"):
        raise ValueError("Invalid ticket status")

    author, message = validate_note(author, message)

    note = {
        "note_id": next_note_id(ticket),
        "author": author,
        "message": message,
    }

    ticket["notes"].append(note)

    return note


def view_notes(tickets, ticket_id):
    ticket = find_ticket(tickets, ticket_id)

    return sorted(
        ticket["notes"],
        key=lambda note: int(note["note_id"][1:]),
    )