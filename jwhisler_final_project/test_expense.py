from expense import Expense


def test_update_amount():
    expense = Expense(
        1, "10/14/2025", "Takeout from Chinese Restaurant", 12.50, "Food")
    expense.update_amount(15.50)
    print(expense)
    assert expense.amount == 15.50, "update_amount did not update value correctly"


if __name__ == "__main__":
    test_update_amount()
    print("All tests passed.")
