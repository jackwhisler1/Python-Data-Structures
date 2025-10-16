"""
Jon Whisler
Class: CS 521 - Fall
Description: Expense class for tracking individual expenses
"""


class Expense:
    """Represents a single expense with validation and formatting capabilities"""

    def __init__(self, expense_id,  date, category, description, amount):
        """Initialize expense with validation

        Args:
            expense_id (int): Unique identifier for the expense
            date (str): Date in MM-DD-YYYY format
            category (str): Expense category
            description (str): Description of the expense
            amount (float): Amount of the expense
        """
        self.__id = expense_id  # private attribute
        self.description = description  # public attribute
        self.date = date  # public attribute
        self.amount = self.__validate_amount(amount)  # use private validation
        self.category = category  # public attribute

    def to_dict(self):
        """Returns expense data as dictionary
        Returns:
            dict: Dictionary containing all expense fields
        """
        return {
            "id": self.__id,
            "date": self.date,
            "description": self.description,
            "amount": self.amount,
            "category": self.category
        }

    def update_amount(self, new_amount):
        """Public method to update expense amount

        Args:
            new_amount (float): New amount to set

        Returns:
            float: The updated amount
        """
        self.amount = self.__validate_amount(new_amount)
        return self.amount

    def get_id(self):
        """Public method to access private id attribute

        Returns:
            int: The expense ID
        """
        return self.__id

    def __validate_amount(self, amount):
        """Private method to validate amount is positive number

        Args:
            amount: Value to validate as amount

        Returns:
            float: Validated amount

        Raises:
            ValueError: If amount is not positive
        """
        try:
            amt = float(amount)
            if amt < 0:
                raise ValueError("Amount must be positive.")
            return amt
        except (ValueError, TypeError):
            raise ValueError("Amount must be a valid positive number")

    def __str__(self):
        """String representation of expense

         Returns:
            str: Formatted expense string
        """
        return f"{self.date} | {self.category} | {self.description} | ${self.amount:.2f}"

    def __repr__(self):
        """Developer-friendly representation (magic method)

        Returns:
            str: Representation showing all attributes
        """
        return (f"Expense(expense_id={self.__id}, date='{self.date}', "
                f"category='{self.category}', description='{self.description}', "
                f"amount={self.amount})")

    def __lt__(self, other):
        """Less than comparison based on amount

        Args:
            other (Expense): Another expense to compare

        Returns:
            bool: True if this expense amount is less than other
        """
        if not isinstance(other, Expense):
            return NotImplemented
        return self.amount < other.amount

    def __eq__(self, other):
        """Equality comparison

        Args:
            other (Expense): Another expense to compare

        Returns:
            bool: True if expenses have same id
        """
        if not isinstance(other, Expense):
            return NotImplemented
        return self.__id == other.__id
