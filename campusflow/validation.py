CATEGORIES = ("Network", "Hardware", "Software", "Other")
URGENCIES = ("low", "medium", "high")
STATUSES = ("open", "in_progress", "resolved")
PRIORITIES = ("critical", "high", "medium", "low")


def validate_title(title):

    if not isinstance(title, str) or not title.strip():
        raise ValueError("Title cannot be empty")

    return title.strip()


def validate_category(category):

    if not isinstance(category, str):
        raise ValueError("Invalid category")

    category = category.strip().capitalize()

    if category not in CATEGORIES:
        raise ValueError("Invalid category")

    return category


def validate_urgency(urgency):

    if not isinstance(urgency, str):
        raise ValueError("Invalid urgency")

    urgency = urgency.strip().lower()

    if urgency not in URGENCIES:
        raise ValueError("Invalid urgency")

    return urgency


def validate_affected_users(affected_users):

    if type(affected_users) is not int or affected_users <= 0:
        raise ValueError("Affected users must be a positive integer")

    return affected_users


def validate_staff(staff_name):

    if not isinstance(staff_name, str) or not staff_name.strip():
        raise ValueError("Staff name cannot be empty")

    return staff_name.strip()


def validate_status(status):

    if status not in STATUSES:
        raise ValueError("Invalid status")

    return status


def validate_ticket_id(ticket_id):

    if not isinstance(ticket_id, str):
        raise ValueError("Invalid ticket ID")

    if not ticket_id.startswith("T"):
        raise ValueError("Invalid ticket ID")

    number = ticket_id[1:]

    if len(number) < 3:
        raise ValueError("Invalid ticket ID")

    if not number.isascii() or not number.isdigit():
        raise ValueError("Invalid ticket ID")

    return ticket_id


def validate_note_id(note_id):

    if not isinstance(note_id, str):
        raise ValueError("Invalid note ID")

    if not note_id.startswith("N"):
        raise ValueError("Invalid note ID")

    number = note_id[1:]

    if len(number) < 3:
        raise ValueError("Invalid note ID")

    if not number.isascii() or not number.isdigit():
        raise ValueError("Invalid note ID")

    return note_id


def validate_note(author, message):

    author = validate_staff(author)

    if not isinstance(message, str):
        raise ValueError("Note message must be text")

    message = message.strip()

    if not 5 <= len(message) <= 300:
        raise ValueError("Note must contain 5 to 300 characters")

    return author, message