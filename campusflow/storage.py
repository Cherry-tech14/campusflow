import json
import os
import tempfile
from pathlib import Path

from campusflow.validation import (
    validate_ticket_id,
    validate_title,
    validate_category,
    validate_urgency,
    validate_affected_users,
    validate_priority,
    validate_status,
    validate_staff,
    validate_note_id,
    validate_note_author,
    validate_note_message,
)

from campusflow.tickets import calculate_priority


DATA_FILE = Path("data/tickets.json")


def validate_ticket_record(ticket):
    if not isinstance(ticket, dict):
        raise ValueError("Invalid ticket record")

    required_fields = [
        "id",
        "title",
        "category",
        "urgency",
        "affected_users",
        "priority",
        "status",
        "assigned_to",
    ]

    for field in required_fields:
        if field not in ticket:
            raise ValueError("Ticket is missing required fields")

    validate_ticket_id(ticket["id"])
    validate_title(ticket["title"])
    validate_category(ticket["category"])
    validate_urgency(ticket["urgency"])
    validate_affected_users(ticket["affected_users"])
    validate_priority(ticket["priority"])
    validate_status(ticket["status"])

    if ticket["assigned_to"] is not None:
        validate_staff(ticket["assigned_to"])

    correct_priority = calculate_priority(
        ticket["urgency"],
        ticket["affected_users"],
    )

    if ticket["priority"] != correct_priority:
        raise ValueError("Incorrect ticket priority")

    if ticket["status"] == "in_progress":
        if ticket["assigned_to"] is None:
            raise ValueError("In-progress ticket must be assigned")

    if "notes" not in ticket:
        ticket["notes"] = []

    if not isinstance(ticket["notes"], list):
        raise ValueError("Notes must be a list")

    note_ids = []

    for note in ticket["notes"]:
        if not isinstance(note, dict):
            raise ValueError("Invalid note")

        if "note_id" not in note:
            raise ValueError("Note ID is missing")

        if "author" not in note:
            raise ValueError("Note author is missing")

        if "message" not in note:
            raise ValueError("Note message is missing")

        validate_note_id(note["note_id"])
        validate_note_author(note["author"])
        validate_note_message(note["message"])

        if note["note_id"] in note_ids:
            raise ValueError("Duplicate note ID")

        note_ids.append(note["note_id"])

    return ticket


def validate_tickets(tickets):
    if not isinstance(tickets, list):
        raise ValueError("Tickets must be a list")

    ticket_ids = []

    for ticket in tickets:
        validate_ticket_record(ticket)

        if ticket["id"] in ticket_ids:
            raise ValueError("Duplicate ticket ID")

        ticket_ids.append(ticket["id"])

    return tickets


def load_tickets(file_path=DATA_FILE):
    file_path = Path(file_path)

    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tickets = json.load(file)

    except json.JSONDecodeError:
        raise ValueError("Invalid JSON file")

    return validate_tickets(tickets)


def save_tickets(tickets, file_path=DATA_FILE):
    file_path = Path(file_path)

    # Work on a copy so validation cannot change the original list.
    import copy
    tickets_copy = copy.deepcopy(tickets)

    validate_tickets(tickets_copy)

    file_path.parent.mkdir(parents=True, exist_ok=True)

    temporary_name = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=file_path.parent,
            delete=False,
        ) as file:
            temporary_name = file.name
            json.dump(tickets_copy, file, indent=4)
            file.flush()
            os.fsync(file.fileno())

        os.replace(temporary_name, file_path)

    finally:
        if temporary_name is not None:
            if os.path.exists(temporary_name):
                os.remove(temporary_name)


def reload_tickets(file_path=DATA_FILE):
    return load_tickets(file_path)