"""Placeholder"""


class Expense:
    def __init__(self, expense_id, description, date, amount, category):
        self.__id = expense_id  # private attribute
        self.description = description
        self.date = date
        self.amount = self.__validate_amount(amount)  # private validation
        self.category = category

    def __validate_amount(self, value):
        """Private method to validate amount is a number"""
        try:
            return float(value)
        except ValueError:
            raise ValueError("Amount must be a number")

    def to_dict(self):
        """Returns expense data as dictionary"""
        return {
            "id": self.__id,
            "date": self.date,
            "description": self.description,
            "amount": self.amount,
            "category": self.category
        }

    def update_amount(self, new_amount):
        """Public method to update expense amount"""
        self.amount = self.__validate_amount(new_amount)
        return self.amount

    def __str__(self):
        return f"{self.date} | {self.category} | {self.description} | ${self.amount:.2f}"
