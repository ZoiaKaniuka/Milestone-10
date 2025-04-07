import pytest
from tasks import count_birthdays_by_month

def test_count_birthdays_by_month_success():
    employees = [
        {"name": "Alice", "birthdate": "1990-01-15"},
        {"name": "Bob", "birthdate": "1992-01-20"},
        {"name": "Charlie", "birthdate": "1993-02-10"}
    ]
    result = count_birthdays_by_month(employees)
    assert result["January"] == 2
    assert result["February"] == 1

def test_count_birthdays_with_invalid_date():
    employees = [
        {"name": "Alice", "birthdate": "not-a-date"}
    ]
    with pytest.raises(ValueError, match="Corrupted birthdate"):
        count_birthdays_by_month(employees)
