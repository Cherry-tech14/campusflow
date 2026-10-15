# CampusFlow Baseline Check

## Repository
https://github.com/Cherry-tech14/campusflow

## Audited Commit
7d445178ea95aaccb1527b502db419f0d4c087ba

## Test Command
python3 -m unittest discover -s tests -v

## Test Results

The original CampusFlow application was tested using Python's
unittest framework.

Total Tests: 48 testing 


Result: PASS

## Manual Tests

### Test 1: Valid Ticket Creation

Input:
- Title: Internet connection failure
- Category: Network
- Urgency: high
- Affected Users: 15

Expected:
- Ticket created successfully.
- Priority calculated as critical.
- Status set to open.
- A unique ticket ID generated.


### Test 2: Invalid Ticket Title

Input:
- Title: (empty)
- Category: Hardware
- Urgency: medium
- Affected Users: 3

Expected:
- Ticket creation rejected.
- Error message: Title cannot be empty.
- No new ticket added.


### Test 3: Invalid Affected Users

Input:
- Title: Laptop malfunction
- Category: Hardware
- Urgency: high
- Affected Users: -5

Expected:
- Ticket creation rejected.
- Error message: Affected users must be a positive integer.
- No new ticket added.

## Previous Audit Observations

The previous audit reviewed the following areas:

1. Ticket creation and input validation.
2. Priority calculation and ticket ID generation.
3. Ticket assignment and status transitions.
4. JSON storage and persistence.
5. Automated testing and error handling.
6. GitHub collaboration and code reviews.

The audit recommended further improvements in:

- Edge-case testing.
- JSON storage reliability.
- Integration testing across modules.

These are improvement recommendations and are not
necessarily confirmed defects.

## Conclusion

The original CampusFlow project provides a foundation for
the CampusFlow Next upgrade.

The existing implementation includes ticket creation,
priority calculation, workflow management, reporting,
and JSON persistence.

The baseline test results and manual tests documented above
will be used to verify that the original features continue
working after the new improvements are implemented.

CampusFlow Next will focus on stronger validation,
structured follow-up notes, ticket search, improved reports,
safe JSON loading, and additional automated tests.

Final baseline status: [PASS or FAIL based on actual testing]