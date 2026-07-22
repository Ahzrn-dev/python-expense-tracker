from dataclasses import dataclass


@dataclass(slots=True)
class Expense:
    """Represent a single expense."""

    id: int | None
    title: str
    amount: float
    category: str
    created_at: str