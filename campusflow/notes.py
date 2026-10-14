from campusflow.workflow import find_ticket

from campusflow.validation import (
    validate_note_author,
    validate_note_message,
)


def next_note_id(notes):
    highest_number = 0

    for note in notes:
        note_id = note["note_id"]

        number = int(note_id[1:])

        if number > highest_number:
            highest_number = number

    next_number = highest_number + 1

    return f"N{next_number:03d}"


def add_note(tickets, ticket_id, author, message):
    ticket = find_ticket(tickets, ticket_id)

    if ticket["status"] == "resolved":
        raise ValueError("Cannot add notes to a resolved ticket")

    author = validate_note_author(author)
    message = validate_note_message(message)

    note = {
        "note_id": next_note_id(ticket["notes"]),
        "author": author,
        "message": message,
    }

    ticket["notes"].append(note)

    return note


def view_notes(tickets, ticket_id):
    ticket = find_ticket(tickets, ticket_id)

    notes_copy = []

    for note in ticket["notes"]:
        copied_note = note.copy()
        notes_copy.append(copied_note)

    return notes_copy