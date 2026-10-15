CATEGORIES = ["Network", "Hardware", "Software", "Other"]
URGENCIES = ["low", "medium", "high"]
STATUSES = ["open", "in_progress", "resolved"]
PRIORITIES = ["critical", "high", "medium", "low"]


def validate_title(title):
    if not isinstance(title, str):
        raise ValueError("Title must be text")

    title = title.strip()

    if title == "":
        raise ValueError("Title cannot be empty")

    return title


def validate_category(category):
    if not isinstance(category, str):
        raise ValueError("Category must be text")

    category = category.strip().capitalize()

    if category not in CATEGORIES:
        raise ValueError("Invalid category")

    return category


def validate_urgency(urgency):
    if not isinstance(urgency, str):
        raise ValueError("Urgency must be text")

    urgency = urgency.strip().lower()

    if urgency not in URGENCIES:
        raise ValueError("Invalid urgency")

    return urgency


def validate_affected_users(affected_users):
    if type(affected_users) != int:
        raise ValueError("Affected users must be a whole number")

    if affected_users <= 0:
        raise ValueError("Affected users must be greater than zero")

    return affected_users


def validate_staff(staff_name):
    if not isinstance(staff_name, str):
        raise ValueError("Staff name must be text")

    staff_name = staff_name.strip()

    if staff_name == "":
        raise ValueError("Staff name cannot be empty")

    return staff_name


def validate_status(status):
    if not isinstance(status, str):
        raise ValueError("Status must be text")

    status = status.strip().lower()

    if status not in STATUSES:
        raise ValueError("Invalid status")

    return status


def validate_priority(priority):
    if not isinstance(priority, str):
        raise ValueError("Priority must be text")

    if priority not in PRIORITIES:
        raise ValueError("Invalid priority")

    return priority


def validate_ticket_id(ticket_id):
    if not isinstance(ticket_id, str):
        raise ValueError("Ticket ID must be text")

    if len(ticket_id) < 4:
        raise ValueError("Invalid ticket ID")

    if ticket_id[0] != "T":
        raise ValueError("Ticket ID must start with T")

    numbers = ticket_id[1:]

    if len(numbers) < 3 or not numbers.isascii() or not numbers.isdigit():
        raise ValueError("Invalid ticket ID")

    return ticket_id


def validate_note_id(note_id):
    if not isinstance(note_id, str):
        raise ValueError("Note ID must be text")

    if len(note_id) < 4:
        raise ValueError("Invalid note ID")

    if note_id[0] != "N":
        raise ValueError("Note ID must start with N")

    numbers = note_id[1:]

    if len(numbers) < 3 or not numbers.isascii() or not numbers.isdigit():
        raise ValueError("Invalid note ID")

    return note_id


def validate_note_author(author):
    if not isinstance(author, str):
        raise ValueError("Author must be text")

    author = author.strip()

    if author == "":
        raise ValueError("Author cannot be empty")

    return author


def validate_note_message(message):
    if not isinstance(message, str):
        raise ValueError("Note message must be text")

    message = message.strip()

    if len(message) < 5:
        raise ValueError("Note must contain at least 5 characters")

    if len(message) > 300:
        raise ValueError("Note cannot exceed 300 characters")

    return message