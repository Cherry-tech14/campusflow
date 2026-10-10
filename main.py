from campusflow.tickets import create_ticket
from campusflow.storage import save_tickets, load_tickets


def main():

    try:
        tickets = load_tickets()

    except (ValueError, OSError) as error:
        print("Error loading tickets:", error)
        print("Please fix the data file before starting CampusFlow.")
        return

    while True:
        print("\nCAMPUSFLOW HELPDESK")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("\nCreate Ticket")

            title = input("Enter ticket title: ")
            category = input("Enter category (Network/Hardware/Software/Other): ")
            urgency = input("Enter urgency (low/medium/high): ")
            users = input("Enter number of affected users: ")

            try:
                affected_users = int(users)

                ticket = create_ticket(
                    tickets,
                    title,
                    category,
                    urgency,
                    affected_users
                )

                save_tickets(tickets)

                print("\nTicket created successfully!")
                print("Ticket ID:", ticket["id"])
                print("Title:", ticket["title"])
                print("Priority:", ticket["priority"])
                print("Status:", ticket["status"])

            except ValueError as error:
                print("Error:", error)

            except OSError as error:
                print("Error saving ticket:", error)

        elif choice == "2":
            print("\nAll Tickets")

            if len(tickets) == 0:
                print("No tickets available.")

            else:
                for ticket in tickets:
                    print("\nID:", ticket["id"])
                    print("Title:", ticket["title"])
                    print("Category:", ticket["category"])
                    print("Urgency:", ticket["urgency"])
                    print("Affected users:", ticket["affected_users"])
                    print("Priority:", ticket["priority"])
                    print("Status:", ticket["status"])
                    print("Assigned to:", ticket["assigned_to"])

        elif choice == "3":
            print("Thank you for using CampusFlow!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()