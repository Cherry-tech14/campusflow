# CampusFlow AI Learning Log

## Engineer A
**Responsibilities:** Ticket creation, input validation, priority engine, persistence storage 
and automated tests.

### Log 1: Ticket Creation
**Problem:** Generate unique ticket IDs (T001, T002, etc.).

**AI Assistance:** AI explained how to use loops, string slicing, and f-strings to generate sequential IDs.

**What I Learned:** How `f"T{highest_id + 1:03d}"` generates ticket IDs.

**Verification:** Tested ticket creation and unique IDs using unittest. Tests passed.

### Log 2: Input Validation and Priority Engine
**Problem:** Validate ticket information and calculate priority correctly.

**AI Assistance:** AI explained conditional statements, ValueError, and priority rules.

**What I Learned:** How to reject invalid inputs and calculate critical, high, medium, and low priorities.

**Verification:** Tested valid and invalid inputs and all four priority levels. Tests passed.

### Log 3: Automated Testing
**Problem:** Verify that ticket creation, validation, and priority calculation work correctly.

**AI Assistance:** AI explained unittest, assertEqual(), assertRaises(), and setUp().

**What I Learned:** How to write automated tests and check expected results.

**Verification:** Ran `python3 -m unittest discover -s tests -v`. All 16 Engineer A ticket tests passed.

### Summary
AI helped me understand Python concepts, improve my implementation, and write automated tests. I verified my work through testing.