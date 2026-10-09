# CampusFlow Design Decisions

## Engineer A: Ticket Creation

### 1. Ticket Creation
I used a dictionary to store ticket details and a list to store multiple tickets.

### 2. Input Validation
I used if statements and ValueError to prevent invalid inputs, such as empty titles, wrong categories, and negative numbers.

### 3. Priority Calculation
I used if, elif, and else to calculate ticket priority based on urgency and the number of affected users.

### 4. Ticket ID
I used a for loop to generate unique ticket IDs like T001, T002, and T003.

### 5. Testing
I used Python's unittest module to test ticket creation, priority calculation, and input validation.

### 6. Code Simplicity
I chose simple Python functions and loops because they are easier to understand, maintain, and explain.