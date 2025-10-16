from expense import Expense


def test_update_amount():
    expense = Expense(
        1, "10/14/2025", "Food", "Takeout from Chinese Restaurant", 12.50)
    expense.update_amount(15.50)
    print(expense)
    assert expense.amount == 15.50, "update_amount did not update value correctly"


def test_to_dict():
    expense = Expense(2, "2025-10-11", "Transport", "Bus fare", 2.25)
    data = expense.to_dict()
    expected = {
        "id": 2,
        "date": "2025-10-11",
        "category": "Transport",
        "description": "Bus fare",
        "amount": 2.25
    }
    print(expense)
    assert data == expected, "to_dict did not return correct dictionary"


if __name__ == "__main__":
    test_update_amount()
    test_to_dict()
    print("All tests passed.")
