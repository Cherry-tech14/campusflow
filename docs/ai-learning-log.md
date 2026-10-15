# CampusFlow Next — AI Learning Log

## Project Information

Project: CampusFlow Next
Team Members:
- Engineer A: Mariam Mohammed
- Engineer B: Onah Samuel

## Purpose of the AI Learning Log

This document records how AI assistance was used during
the development of CampusFlow Next.

It explains:
- The problems encountered.
- The questions asked.
- The AI suggestions received.
- The solutions implemented.
- How the solutions were tested.
- What each engineer learned.


## Engineer A — Mariam Mohammed

### Learning Entry 1: Input Validation

**Problem Encountered:**
Ensuring that invalid ticket information was rejected.

**AI Assistance:**
Received guidance on validating ticket titles, categories,
urgency levels, and affected users.

**Implementation:**
Implemented validation functions in validation.py.

**Verification:**
Tested valid and invalid ticket inputs using unittest.

**What I Learned:**
How to validate user input before modifying application data.

### Learning Entry 2: Follow-up Notes

**Problem Encountered:**
Implementing notes without allowing invalid operations
to modify tickets.

**AI Assistance:**
Received guidance on note validation and ID generation.

**Implementation:**
Implemented follow-up notes in notes.py.

**Verification:**
Tested valid notes, invalid messages, and restrictions
on resolved tickets.

**What I Learned:**
How to preserve data integrity when adding related records.

### Learning Entry 3: JSON Storage Reliability

**Problem Encountered:**
Preventing invalid JSON data and duplicate ticket IDs
from affecting existing records.

**AI Assistance:**
Received guidance on storage validation and error handling.

**Implementation:**
Improved storage.py.

**Verification:**
Tested invalid JSON, duplicate IDs, and saving/loading.

**What I Learned:**
Why stored data must be validated before being trusted.

### Learning Entry 4: Git Integration

**Problem Encountered:**
Integrating changes from two engineers without losing work.

**AI Assistance:**
Received guidance on Git branches, fetching, merging,
resolving conflicts, and running integration tests.

**Implementation:**
Merged Engineer B's changes into the integration branch.

**Verification:**
Ran the complete automated test suite.

**What I Learned:**
How to integrate independently developed modules and
verify that they work together.


## Engineer B — Onah Samuel

### Learning Entry 1: Work Queue

**Problem Encountered:**
[Engineer B should describe the actual problem encountered.]

**AI Assistance:**
[Describe the AI guidance received.]

**Implementation:**
Implemented queue.py.

**Verification:**
Tested queue filtering and priority ordering.

**What I Learned:**
[Engineer B should describe what he learned.]

### Learning Entry 2: Search and Filtering

**Problem Encountered:**
[Engineer B should describe the actual problem encountered.]

**AI Assistance:**
[Describe the AI guidance received.]

**Implementation:**
Implemented search.py.

**Verification:**
Tested title searching and combined filters.

**What I Learned:**
[Engineer B should describe what he learned.]

### Learning Entry 3: Reporting

**Problem Encountered:**
[Engineer B should describe the actual problem encountered.]

**AI Assistance:**
[Describe the AI guidance received.]

**Implementation:**
Implemented reports.py.

**Verification:**
Tested report counts and resolution percentages.

**What I Learned:**
[Engineer B should describe what he learned.]

### Learning Entry 4: Engineering Understanding Check

**Problem Encountered:**
Updating the quiz and its tests to match the project requirements.

**AI Assistance:**
Received guidance on quiz validation, scoring,
written explanations, and automated tests.

**Implementation:**
Updated understanding_checks.py and test_understanding.py.

**Verification:**
Confirmed that the updated understanding-check tests passed.

**What I Learned:**
[Engineer B should describe what he learned.]

## Final Integration Testing

Both engineers' contributions were integrated into:

test/campusflow-integration

The integrated project was tested using:

python3 -m unittest discover -s tests -v

Result:

Ran 69 tests


## Reflection

AI assistance supported debugging, code review,
test development, and understanding project requirements.

However, AI suggestions were checked against the project
requirements and verified through automated and manual testing.