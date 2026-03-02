"""
Integration Tests for Quick-Calc.

Integration tests verify that the Calculator core logic works correctly together
with the application's input/output layer, simulating realistic user workflows.
These tests use a black-box perspective — inputs go in, outputs come out.
"""

import pytest
from calculator.core import Calculator


@pytest.fixture
def calc():
    """Return a fresh Calculator instance for each integration test."""
    return Calculator()


class TestUserWorkflows:
    """Simulate end-to-end user interaction sequences."""

    def test_full_addition_workflow(self, calc):
        """
        Simulate: user enters 5, presses '+', enters 3, presses '='.
        Expected display result: 8.
        """
        # User types '5', selects '+', types '3', hits '='
        first_number = 5
        operator = "+"
        second_number = 3

        if operator == "+":
            result = calc.add(first_number, second_number)

        assert result == 8, f"Expected 8 but got {result}"

    def test_clear_after_calculation_resets_to_zero(self, calc):
        """
        Simulate: user performs a calculation, then presses 'C' (Clear).
        Expected: display resets to 0.
        """
        # Perform an operation first
        calc.multiply(9, 9)
        assert calc.current_result == 81, "Pre-condition: result should be 81"

        # User presses 'C'
        cleared = calc.clear()

        assert cleared == 0, "Clear should return 0"
        assert calc.current_result == 0, "current_result should be 0 after clear"

    def test_sequential_operations_workflow(self, calc):
        """
        Simulate a multi-step session:
          Step 1: 10 - 4 = 6
          Step 2: 6 * 3 = 18
          Step 3: 18 / 2 = 9
        Verifies that sequential operations produce correct intermediate and final results.
        """
        step1 = calc.subtract(10, 4)
        assert step1 == 6

        step2 = calc.multiply(step1, 3)
        assert step2 == 18

        step3 = calc.divide(step2, 2)
        assert step3 == 9.0

    def test_division_by_zero_in_workflow_is_graceful(self, calc):
        """
        Simulate: user attempts to divide by zero.
        Application must handle this gracefully via ZeroDivisionError — not crash.
        """
        # Simulate catching the error as the UI layer would
        try:
            calc.divide(100, 0)
            error_message = None
        except ZeroDivisionError as e:
            error_message = str(e)

        assert error_message is not None, "A ZeroDivisionError should have been raised"
        assert "zero" in error_message.lower(), "Error message should mention 'zero'"
        # After the error, state should remain predictable
        assert calc.current_result == 0, "Result should remain at initial state after failed division"
