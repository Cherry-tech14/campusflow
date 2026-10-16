from campusflow.tickets import create_ticket

from campusflow.workflow import (
    assign_ticket,
    update_status,
)

from campusflow.notes import (
    add_note,
    view_notes,
)

from campusflow.storage import (
    load_tickets,
    save_tickets,
)

from campusflow.queue import get_work_queue

from campusflow.search import (
    search_tickets,
    sort_search_results,
)

from campusflow.reports import generate_report

from campusflow.understanding_checks import run_understanding_check


def display_ticket(ticket):
    print("\n------------------------------")
    print("Ticket ID:", ticket["id"])
    print("Title:", ticket["title"])
    print("Category:", ticket["category"])
    print("Urgency:", ticket["urgency"])
    print("Affected Users:", ticket["affected_users"])
    print("Priority:", ticket["priority"])
    print("Status:", ticket["status"])
    print("Assigned To:", ticket["assigned_to"])
    print("Number of Notes:", len(ticket.get("notes", [])))
    print("------------------------------")




def display_tickets(tickets):
    if len(tickets) == 0:
        print("\nNo tickets found.")
        return

    for ticket in tickets:
        display_ticket(ticket)


def display_menu():
    print("\n========== CAMPUSFLOW NEXT ==========")
    print("1. Create Ticket")
    print("2. View All Tickets")
    print("3. Assign Ticket")
    print("4. Change Ticket Status")
    print("5. Reopen Resolved Ticket")
    print("6. View Open Work Queue")
    print("7. Add Follow-up Note")
    print("8. View Ticket Notes")
    print("9. Search Tickets")
    print("10. Generate Reports")
    print("11. Engineering Understanding Check")
    print("12. Exit")
    print("=====================================")




def main():
    try:
        tickets = load_tickets()

    except (ValueError, OSError) as error:
        print("Error loading tickets:", error)
        return

    print("\nWelcome to CampusFlow Next!")

    while True:
        display_menu()

        choice = input("\nChoose an option: ").strip()

        
        if choice == "1":
            print("\n=== CREATE TICKET ===")

            title = input("Ticket title: ")
            category = input("Category (Network/Hardware/Software/Other): ")
            urgency = input("Urgency (low/medium/high): ")

            users_input = input("Number of affected users: ")

            try:
                affected_users = int(users_input)

                
                import copy
                updated_tickets = copy.deepcopy(tickets)

                ticket = create_ticket(
                    updated_tickets,
                    title,
                    category,
                    urgency,
                    affected_users,
                )

                save_tickets(updated_tickets)
                tickets = updated_tickets

                print("\nTicket created successfully!")
                display_ticket(ticket)

            except (ValueError, OSError) as error:
                print("Error:", error)

        
        elif choice == "2":
            print("\n=== ALL TICKETS ===")
            display_tickets(tickets)

    
        elif choice == "3":
            print("\n=== ASSIGN TICKET ===")

            ticket_id = input("Ticket ID: ").strip().upper()
            staff_name = input("Staff name: ")

            try:
                import copy
                updated_tickets = copy.deepcopy(tickets)

                ticket = assign_ticket(
                    updated_tickets,
                    ticket_id,
                    staff_name,
                )

                save_tickets(updated_tickets)
                tickets = updated_tickets

                print("\nTicket assigned successfully!")
                display_ticket(ticket)

            except (ValueError, OSError) as error:
                print("Error:", error)

        elif choice == "4":
            print("\n=== CHANGE TICKET STATUS ===")

            ticket_id = input("Ticket ID: ").strip().upper()

            print("1. open")
            print("2. in_progress")
            print("3. resolved")

            status_choice = input("Choose status: ").strip()

            if status_choice == "1":
                new_status = "open"

            elif status_choice == "2":
                new_status = "in_progress"

            elif status_choice == "3":
                new_status = "resolved"

            else:
                print("Invalid status choice.")
                continue

            try:
                import copy
                updated_tickets = copy.deepcopy(tickets)

                ticket = update_status(
                    updated_tickets,
                    ticket_id,
                    new_status,
                )

                save_tickets(updated_tickets)
                tickets = updated_tickets

                print("\nStatus updated successfully!")
                display_ticket(ticket)

            except (ValueError, OSError) as error:
                print("Error:", error)

        elif choice == "5":
            print("\n=== REOPEN TICKET ===")

            ticket_id = input("Ticket ID: ").strip().upper()

            try:
                import copy
                updated_tickets = copy.deepcopy(tickets)

                ticket = update_status(
                    updated_tickets,
                    ticket_id,
                    "open",
                )

                save_tickets(updated_tickets)
                tickets = updated_tickets

                print("\nTicket reopened successfully!")
                display_ticket(ticket)

            except (ValueError, OSError) as error:
                print("Error:", error)

        elif choice == "6":
            print("\n=== OPEN WORK QUEUE ===")

            queue = get_work_queue(tickets)

            display_tickets(queue)

        elif choice == "7":
            print("\n=== ADD FOLLOW-UP NOTE ===")

            ticket_id = input("Ticket ID: ").strip().upper()
            author = input("Author: ")
            message = input("Note message: ")

            try:
                import copy
                updated_tickets = copy.deepcopy(tickets)

                note = add_note(
                    updated_tickets,
                    ticket_id,
                    author,
                    message,
                )

                save_tickets(updated_tickets)
                tickets = updated_tickets

                print("\nNote added successfully!")
                print("Note ID:", note["note_id"])
                print("Author:", note["author"])
                print("Message:", note["message"])

            except (ValueError, OSError) as error:
                print("Error:", error)

        elif choice == "8":
            print("\n=== VIEW TICKET NOTES ===")

            ticket_id = input("Ticket ID: ").strip().upper()

            try:
                notes = view_notes(tickets, ticket_id)

                if len(notes) == 0:
                    print("No notes found.")

                else:
                    for note in notes:
                        print("\nNote ID:", note["note_id"])
                        print("Author:", note["author"])
                        print("Message:", note["message"])

            except ValueError as error:
                print("Error:", error)

        elif choice == "9":
            print("\n=== SEARCH TICKETS ===")
            print("Leave a filter blank to skip it.")

            title = input("Title: ")
            category = input("Category: ")
            status = input("Status: ")
            priority = input("Priority: ")

            try:
                results = search_tickets(
                    tickets,
                    title,
                    category,
                    status,
                    priority,
                )

                results = sort_search_results(results)

                print("\nMatching tickets:", len(results))

                display_tickets(results)

            except ValueError as error:
                print("Error:", error)

    
        elif choice == "10":
            print("\n=== TICKET REPORT ===")

            report = generate_report(tickets)

            print("\nTotal Tickets:", report["total"])

            print("\nTickets by Status:")
            for status in report["by_status"]:
                print(status, ":", report["by_status"][status])

            print("\nTickets by Priority:")
            for priority in report["by_priority"]:
                print(priority, ":", report["by_priority"][priority])

            print("\nTickets by Category:")
            for category in report["by_category"]:
                print(category, ":", report["by_category"][category])

            print("\nResolved Tickets:", report["resolved"])
            print("Unresolved Tickets:", report["unresolved"])

            percentage = report["resolution_percentage"]

            print("Resolution Percentage:", round(percentage, 2), "%")

        elif choice == "11":
            run_understanding_check()

        
        elif choice == "12":
            print("\nThank you for using CampusFlow Next!")
            break

        else:
            print("\nInvalid option. Please choose 1 to 12.")


if __name__ == "__main__":
    main()