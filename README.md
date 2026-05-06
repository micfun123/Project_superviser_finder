# Supervisor Finder

A single-page tool for browsing and searching academic supervisors by research topic, MSc course, and name.

## Setup

Place the following files in the same directory as `index.html`:

- `data.csv` — the supervisor/topic matrix
- `staff.csv` — staff contact details (name, email, room number)

## CSV format

**data.csv**

- Row 0: supervisor names starting at column 2
- Row 2: MSc specialisation codes per supervisor (`CNAM`, `CSFIT`, `DA`, `IS`, `CS`, `AIML`)
- Rows 5 onwards: topic rows, where column 0 is the subject area, column 1 is the topic name, and each supervisor column contains `y` or `d` if they supervise that topic
- A row with `count` in column 0 marks the end of topic data
- A row containing `additional` in column 0 is read as free-text notes per supervisor

**staff.csv**

| Column | Content |
|--------|---------|
| 0 | Full name (must match data.csv) |
| 1 | Email address |
| 2 | Room number |

## Features

- Search by supervisor name or topic keyword
- Filter by subject area using the dropdown
- Click a card to see full topic list, contact details, and notes
