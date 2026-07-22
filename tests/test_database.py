from src.database import Database


def test_database_creation(tmp_path) -> None:
    database_file = tmp_path / "test.db"

    database = Database(str(database_file))

    assert database_file.exists()
    assert database.get_expenses() == []


def test_add_expense(tmp_path) -> None:
    database_file = tmp_path / "test.db"

    database = Database(str(database_file))

    database.add_expense(
        "Coffee",
        5.50,
        "Food",
        "2026-07-22 10:00:00",
    )

    expenses = database.get_expenses()

    assert len(expenses) == 1
    assert expenses[0][1] == "Coffee"
    assert expenses[0][2] == 5.50
    assert expenses[0][3] == "Food"


def test_delete_expense(tmp_path) -> None:
    database_file = tmp_path / "test.db"

    database = Database(str(database_file))

    database.add_expense(
        "Coffee",
        5.50,
        "Food",
        "2026-07-22 10:00:00",
    )

    expense_id = database.get_expenses()[0][0]

    database.delete_expense(expense_id)

    assert database.get_expenses() == []