from campusflow.tickets import create_ticket

tickets = []


def main():
    while True:
        print("\nCAMPUSFLOW HELPDESK")
        print("1. Create Ticket")
        print("2. View Tickets")
        print("3. Exit")

        choice = input("Enter your choice: ")

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

                print("\nTicket created successfully!")
                print("Ticket ID:", ticket["id"])
                print("Title:", ticket["title"])
                print("Priority:", ticket["priority"])
                print("Status:", ticket["status"])

            except ValueError as error:
                print("Error:", error)

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

        elif choice == "3":
            print("Thank you for using CampusFlow!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()