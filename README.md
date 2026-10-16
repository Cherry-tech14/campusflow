# CampusFlow Next — Campus IT Helpdesk Ticketing System

## Project Overview

CampusFlow Next is a Python-based command-line application designed to help campus IT support teams manage technical support requests.

The application allows users to create tickets, calculate priorities, assign support staff, manage ticket statuses, add follow-up notes, search tickets, generate reports, and save ticket information using JSON.

CampusFlow Next improves the original CampusFlow application by introducing additional features, stronger input validation, reliable data storage, and automated testing.

The project was developed collaboratively by two engineers using Python, Git, GitHub, and the unittest framework.


## Problem Statement

Campus IT departments regularly receive complaints involving network connectivity, computer hardware, software applications, and other technical services.

Without an organized ticket management system, these complaints can become difficult to track, prioritize, assign, and resolve.

CampusFlow Next addresses these challenges by providing a structured helpdesk ticketing system.

### Project Objectives

- Create and manage technical support tickets.
- Automatically calculate ticket priorities.
- Assign tickets to support staff.
- Track ticket resolution progress.
- Record follow-up notes.
- Organize unresolved tickets by priority.
- Search and filter tickets.
- Generate ticket reports.
- Save and retrieve ticket information.
- Prevent invalid operations from corrupting data.
- Evaluate engineering understanding through scenario-based questions.

### Team members and contributions

#### Engineer A _ Mariam Mohammed


#### Responsibilities

- Input validation.
- Ticket creation.
- Automatic priority calculation.
- Ticket workflow validation.
- Follow-up note management.
- JSON storage reliability.
- Automated testing.


#### Contributions

1. Implemented ticket creation with automatically generated unique IDs.
2. Developed validation for ticket titles, categories, urgency levels, and affected users.
3. Implemented automatic ticket priority calculation.
4. Implemented ticket assignment and status transition validation.
5. Developed follow-up note functionality.
6. Added validation for note authors and messages.
7. Prevented notes from being added to resolved tickets.
8. Improved JSON storage validation and error handling.
9. Implemented checks against duplicate ticket IDs.
10. Developed unit tests for assigned modules.

#### Main Files

- `campusflow/validation.py`
- `campusflow/tickets.py`
- `campusflow/workflow.py`
- `campusflow/notes.py`
- `campusflow/storage.py`
- `tests/test_tickets.py`
- `tests/test_workflow.py`
- `tests/test_notes.py`
- `tests/test_storage.py`


## Project Structure

```text
campusflow/
│
├── campusflow/
│   ├── __init__.py
│   ├── validation.py
│   ├── tickets.py
│   ├── workflow.py
│   ├── notes.py
│   ├── storage.py
│   ├── queue.py
│   ├── search.py
│   ├── reports.py
│   └── understanding_checks.py
│
├── tests/
│   ├── __init__.py
│   ├── test_tickets.py
│   ├── test_workflow.py
│   ├── test_notes.py
│   ├── test_storage.py
│   ├── test_queue.py
│   ├── test_search.py
│   ├── test_reports.py
│   └── test_understanding.py
│
├── data/
│   └── tickets.json
│
├── docs/
│   ├── baseline-check.md
│   └── ai-learning-log.md
│
├── main.py
├── README.md
└── .gitignore
```

## Automated Testing

CampusFlow Next uses Python's built-in `unittest` framework.

The integrated application successfully passed **69 automated unit tests**.

### Run All Tests

```bash
python3 -m unittest discover -s tests -v
```

### Run Individual Test Modules

**Engineer A's Tests**

Ticket creation:

```bash
python3 -m unittest discover -s tests -p "test_tickets.py" -v
```

Ticket workflow:

```bash
python3 -m unittest discover -s tests -p "test_workflow.py" -v
```

Follow-up notes:

```bash
python3 -m unittest discover -s tests -p "test_notes.py" -v
```

JSON storage:

```bash
python3 -m unittest discover -s tests -p "test_storage.py" -v
```



## Engineer B — Onah Samuel

**GitHub:** https://github.com/SamuelOnah

### Responsibilities

- Ticket search and combined filtering.
- Ticket reports and analytics.
- Engineering Understanding Check.
- Command-line interface integration.
- Automated testing for search, reporting, and understanding-check functionality.

### Contributions

1. Worked on ticket search functionality using title matching and optional filters for category, status, and priority.
2. Worked on combining search filters so that matching tickets satisfy all supplied criteria.
3. Contributed to ticket reporting, including ticket totals, status counts, priority counts, category counts, unresolved tickets, and resolution percentages.
4. Worked on the interactive Engineering Understanding Check, covering important application rules through multiple-choice scenarios.
5. Contributed to command-line interaction for accessing application features.
6. Worked on automated tests for search, reporting, and understanding-check functionality.

### Main Files

**Application modules**
- `campusflow/search.py`
- `campusflow/reports.py`
- `campusflow/understanding_checks.py`
- `main.py`

**Test modules**
- `tests/test_search.py`
- `tests/test_reports.py`
- `tests/test_understanding.py`

### Testing

CampusFlow Next uses Python's built-in `unittest` framework.

Run the complete test suite from the project root:

```bash
python3 -m unittest discover -s tests -v
```

Run Engineer B's test modules individually:

**Ticket search**
```bash
python3 -m unittest discover -s tests -p "test_search.py" -v
```

**Reports and analytics**
```bash
python3 -m unittest discover -s tests -p "test_reports.py" -v
```

**Engineering Understanding Check**
```bash
python3 -m unittest discover -s tests -p "test_understanding.py" -v
```



#### Main Work Repo 
***Github**  https://github.com/Cherry-tech14/campusflow