# Python Expense Tracker

A command-line expense tracking application built with Python and SQLite. The application allows users to manage daily expenses through a simple and intuitive interface.

## Features

- Add new expenses
- View all expenses
- Delete expenses
- Store data in SQLite
- Automatic database creation
- Object-oriented design
- Unit tests with pytest

## Technologies

- Python 3
- SQLite
- Pytest

## Project Structure

```
python-expense-tracker/
│
├── src/
│   ├── main.py
│   ├── database.py
│   └── models.py
│
├── tests/
│   └── test_database.py
│
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Ahzrn-dev/python-expense-tracker.git
cd python-expense-tracker
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the application:

```bash
python src/main.py
```

Example:

```
=== Expense Tracker ===

1. Add Expense
2. View Expenses
3. Delete Expense
4. Exit

Choose an option:
```

## Running Tests

```bash
pytest
```

or

```bash
python -m pytest -v
```

## Future Improvements

- Update existing expenses
- Search expenses
- Filter by category
- Monthly reports
- Expense summaries
- Export to CSV
- Export to Excel
- Charts and statistics
- Budget management
- Streamlit web interface

## License

This project is licensed under the MIT License.
