"""
Quick-Calc: Core Calculator Logic
Provides basic arithmetic operations with proper error handling.
"""


class Calculator:
    """A simple calculator that supports add, subtract, multiply, divide, and clear."""

    def __init__(self):
        self.current_result = 0

    def add(self, a: float, b: float) -> float:
        """Return the sum of a and b."""
        result = a + b
        self.current_result = result
        return result

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of a minus b."""
        result = a - b
        self.current_result = result
        return result

    def multiply(self, a: float, b: float) -> float:
        """Return the product of a and b."""
        result = a * b
        self.current_result = result
        return result

    def divide(self, a: float, b: float) -> float:
        """
        Return the quotient of a divided by b.

        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result = a / b
        self.current_result = result
        return result

    def clear(self) -> float:
        """Reset the current result to zero and return 0."""
        self.current_result = 0
        return self.current_result
