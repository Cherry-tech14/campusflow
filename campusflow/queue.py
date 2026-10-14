PRIORITY_ORDER = {
    "critical": 1,
    "high": 2,
    "medium": 3,
    "low": 4,
}


def get_work_queue(tickets):
    open_tickets = []

    for ticket in tickets:
        if ticket["status"] == "open":
            open_tickets.append(ticket)

    # Put tickets in order using simple loops.
    for i in range(len(open_tickets)):
        for j in range(i + 1, len(open_tickets)):

            first = open_tickets[i]
            second = open_tickets[j]

            first_priority = PRIORITY_ORDER[first["priority"]]
            second_priority = PRIORITY_ORDER[second["priority"]]

            should_swap = False

            if first_priority > second_priority:
                should_swap = True

            elif first_priority == second_priority:
                first_id = int(first["id"][1:])
                second_id = int(second["id"][1:])

                if first_id > second_id:
                    should_swap = True

            if should_swap:
                open_tickets[i] = second
                open_tickets[j] = first

    return open_tickets