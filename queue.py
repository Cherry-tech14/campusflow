from __future__ import annotations

PRIORITY_RANK = {
    "critical": 0,
    "high": 1,
    "medium": 2,
    "low": 3,
}


def _numeric_ticket_id(ticket: dict) -> int:
    """Extract the numeric portion of IDs such as T001."""
    ticket_id = str(ticket.get("id", ""))
    digits = ticket_id[1:] if ticket_id[:1].upper() == "T" else ticket_id
    try:
        return int(digits)
    except ValueError:
        return float("inf")


def get_work_queue(tickets: list[dict]) -> list[dict]:
   
    unresolved = [
        ticket for ticket in tickets
        if ticket.get("status") in {"open", "in_progress"}
    ]
    return sorted(
        unresolved,
        key=lambda ticket: (
            PRIORITY_RANK.get(str(ticket.get("priority", "")).lower(), 99),
            _numeric_ticket_id(ticket),
        ),
    )
