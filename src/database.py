import sqlite3
from pathlib import Path

DATABASE_NAME = "expenses.db"


class Database:
    """SQLite database for storing expenses."""

    def __init__(self, database_name: str = DATABASE_NAME) -> None:
        self.database_name = database_name
        self.create_database()

    def connect(self) -> sqlite3.Connection:
        """Return a database connection."""

        return sqlite3.connect(self.database_name)

    def create_database(self) -> None:
        """Create the expenses table if it does not exist."""

        Path(self.database_name).touch(exist_ok=True)

        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS expenses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    amount REAL NOT NULL,
                    category TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )

            connection.commit()

    def add_expense(
        self,
        title: str,
        amount: float,
        category: str,
        created_at: str,
    ) -> None:
        """Insert a new expense."""

        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                INSERT INTO expenses
                (title, amount, category, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (title, amount, category, created_at),
            )

            connection.commit()

    def get_expenses(self) -> list[tuple]:
        """Return all expenses."""

        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT *
                FROM expenses
                ORDER BY id DESC
                """
            )

            return cursor.fetchall()

    def delete_expense(self, expense_id: int) -> None:
        """Delete an expense."""

        with self.connect() as connection:
            cursor = connection.cursor()

            cursor.execute(
                "DELETE FROM expenses WHERE id = ?",
                (expense_id,),
            )

            connection.commit()