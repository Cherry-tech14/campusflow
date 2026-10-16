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
I encountered difficulties pulling the latest project changes from GitHub and getting the updated files to display correctly in VS Code. I also needed to ensure that the work queue displayed only open tickets in the correct priority order.

**AI Assistance:**
I received guidance on checking my Git branch, fetching updates, and understanding how switching branches affects the files displayed in VS Code. I also received guidance on how to organize the work queue according to ticket priority.

**Implementation:**
Implemented `queue.py` to display open tickets in priority order: critical, high, medium, and low.

**Verification:**
Checked the updated project files in VS Code and tested queue filtering and priority ordering.

**What I Learned:**
I learned how Git branches affect the files displayed in my project and how to retrieve updated project changes. I also learned how to filter and sort tickets based on their status and priority.

### Learning Entry 2: Search and Filtering

**Problem Encountered:**
I needed to implement a search feature that could find tickets using different criteria while ensuring that multiple filters worked correctly together.

**AI Assistance:**
I received guidance on using case-insensitive string comparisons and combining multiple filtering conditions.

**Implementation:**
Implemented `search.py` to search tickets by title, category, status, and priority.

**Verification:**
Tested title searching, individual filters, combined filters, and searches that returned no results.

**What I Learned:**
I learned how to filter Python data using multiple conditions and how to make searches more flexible and accurate.

### Learning Entry 3: Reporting

**Problem Encountered:**
I needed to generate accurate ticket reports, including ticket counts by category, status, and priority, as well as the percentage of resolved tickets.

**AI Assistance:**
I received guidance on counting records, organizing report results, and calculating resolution percentages safely.

**Implementation:**
Implemented `reports.py` to generate ticket statistics and resolution percentages.

**Verification:**
Tested report counts, resolution percentages, and reporting when there were no tickets.

**What I Learned:**
I learned how to summarize application data, calculate percentages, and handle empty datasets without causing errors.

### Learning Entry 4: Engineering Understanding Check

**Problem Encountered:**
I encountered difficulties updating the engineering understanding check and its automated tests to match the project requirements.

**AI Assistance:**
I received guidance on validating multiple-choice answers, calculating scores, collecting written explanations, and correcting automated test failures.

**Implementation:**
Updated `understanding_checks.py` and `test_understanding.py` to support six multiple-choice questions, answer validation, scoring, and two written explanations.

**Verification:**
Ran the understanding-check tests and confirmed that the corrected tests passed.

**What I Learned:**
I learned how to validate user input, calculate quiz scores, test interactive functions, and debug automated tests.

## Final Integration Testing

Both engineers' contributions were integrated into the branch:

`test/campusflow-integration`

The integrated project was tested using:

```bash
python3 -m unittest discover -s tests -v
```

**Recorded Result:**

```text
Ran 69 tests

OK
```

## Reflection

Working on CampusFlow Next helped me improve my understanding of Python programming, Git collaboration, debugging, and automated testing.

One challenge I encountered was retrieving updated project files after switching Git branches. Through guidance and practical troubleshooting, I learned how to check my current branch, fetch updates, and understand why different branches display different versions of a project.

I also improved my understanding of filtering, sorting, reporting, and validating user input.

AI assistance helped me understand possible solutions, but I learned the importance of checking suggestions against project requirements and verifying implementations through testing.