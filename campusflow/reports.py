from __future__ import annotations

STATUSES = ("open", "in_progress", "resolved")
PRIORITIES = ("critical", "high", "medium", "low")


def build_report(tickets: list[dict]) -> dict:
    """Return total, status counts, and priority counts (including zero counts)."""
    status_counts = {status: 0 for status in STATUSES}
    priority_counts = {priority: 0 for priority in PRIORITIES}

    for ticket in tickets:
        status = str(ticket.get("status", "")).lower()
        priority = str(ticket.get("priority", "")).lower()
        if status in status_counts:
            status_counts[status] += 1
        if priority in priority_counts:
            priority_counts[priority] += 1

    return {
        "total": len(tickets),
        "by_status": status_counts,
        "by_priority": priority_counts,
    }


def format_report(report: dict) -> str:
    """Convert a report dictionary into readable CLI output."""
    lines = [f"Total tickets: {report['total']}", "By status:"]
    lines.extend(
        f"  {status}: {count}"
        for status, count in report["by_status"].items()
    )
    lines.append("By priority:")
    lines.extend(
        f"  {priority}: {count}"
        for priority, count in report["by_priority"].items()
    )
    return "\n".join(lines)
