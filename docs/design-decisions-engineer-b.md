# Engineer B design notes

- Ticket collection: list of dictionaries, passed into each business-logic function.
- Invalid assignment or lifecycle action: raise `TicketWorkflowError` (a `ValueError` subclass).
- Successful functions return the updated ticket; the queue returns a new sorted list.
- Reports return a dictionary so the CLI and tests can use the data independently of display formatting.
- Persistence is intentionally not implemented in these feature modules; it remains a shared integration task.
