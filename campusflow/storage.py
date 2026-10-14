import json
import os
import tempfile
from pathlib import Path

from campusflow.tickets import calculate_priority
from campusflow.validation import (
    CATEGORIES,
    PRIORITIES,
    STATUSES,
    URGENCIES,
    validate_affected_users,
    validate_category,
    validate_note_id,
    validate_ticket_id,
    validate_title,
    validate_urgency,
)

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data" / "tickets.json"

REQUIRED_FIELDS = {
    "id",
    "title",
    "category",
    "urgency",
    "affected_users",
    "priority",
    "status",
    "assigned_to",
    "notes",
}


def validate_ticket(ticket):
    if not isinstance(ticket, dict):
        raise ValueError("Ticket must be a dictionary")

    if not REQUIRED_FIELDS.issubset(ticket):
        raise ValueError("Ticket is missing required fields")

    validate_ticket_id(ticket["id"])
    validate_title(ticket["title"])

    if (
        ticket["category"] not in CATEGORIES
        or validate_category(ticket["category"]) != ticket["category"]
    ):
        raise ValueError("Invalid stored category")

    if (
        ticket["urgency"] not in URGENCIES
        or validate_urgency(ticket["urgency"]) != ticket["urgency"]
    ):
        raise ValueError("Invalid stored urgency")

    validate_affected_users(ticket["affected_users"])

    if ticket["status"] not in STATUSES:
        raise ValueError("Invalid stored status")

    if ticket["priority"] not in PRIORITIES:
        raise ValueError("Invalid stored priority")

    expected_priority = calculate_priority(
        ticket["urgency"],
        ticket["affected_users"],
    )

    if ticket["priority"] != expected_priority:
        raise ValueError("Ticket priority does not match its inputs")

    assigned_to = ticket["assigned_to"]

    if assigned_to is not None:
        if not isinstance(assigned_to, str) or not assigned_to.strip():
            raise ValueError("Invalid assigned staff")

    if ticket["status"] == "in_progress" and assigned_to is None:
        raise ValueError("In-progress ticket must be assigned")

    if not isinstance(ticket["notes"], list):
        raise ValueError("Notes must be a list")

    note_ids = set()

    for note in ticket["notes"]:
        if not isinstance(note, dict):
            raise ValueError("Invalid note structure")

        if not {"note_id", "author", "message"}.issubset(note):
            raise ValueError("Note is missing required fields")

        note_id = validate_note_id(note["note_id"])

        if note_id in note_ids:
            raise ValueError("Duplicate note ID")

        note_ids.add(note_id)

        author = note["author"]
        message = note["message"]

        if not isinstance(author, str) or not author.strip():
            raise ValueError("Invalid note author")

        if not isinstance(message, str):
            raise ValueError("Invalid note message")

        if not 5 <= len(message.strip()) <= 300:
            raise ValueError("Invalid note message length")

    return True


def validate_collection(tickets):
    if not isinstance(tickets, list):
        raise ValueError("Ticket data must be a list")

    ticket_ids = set()

    for ticket in tickets:
        validate_ticket(ticket)

        ticket_id = ticket["id"]

        if ticket_id in ticket_ids:
            raise ValueError("Duplicate ticket ID")

        ticket_ids.add(ticket_id)

    return True


def save_tickets(tickets, path=FILE_PATH):
    validate_collection(tickets)

    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    temporary_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            dir=file_path.parent,
            prefix=".tickets-",
            suffix=".tmp",
            delete=False,
        ) as file:
            temporary_path = Path(file.name)
            json.dump(tickets, file, indent=4)
            file.flush()
            os.fsync(file.fileno())

        os.replace(temporary_path, file_path)

    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


def load_tickets(path=FILE_PATH):
    file_path = Path(path)

    if not file_path.exists():
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            tickets = json.load(file)

    except (json.JSONDecodeError, UnicodeError) as error:
        raise ValueError("Ticket data file contains invalid JSON") from error

    validate_collection(tickets)

    return tickets


def reload_tickets(tickets, path=FILE_PATH):
    
    loaded_tickets = load_tickets(path)

    tickets[:] = loaded_tickets

    return tickets