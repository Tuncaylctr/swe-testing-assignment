"""
Unit Tests for Quick-Calc Core Calculator Logic.

Tests cover all four basic operations and multiple edge cases,
following a white-box testing approach with knowledge of the internal implementation.
"""

import pytest
from calculator.core import Calculator


@pytest.fixture
def calc():
    """Return a fresh Calculator instance for each test."""
    return Calculator()


# ─────────────────────────────────────────────
# Addition Tests
# ─────────────────────────────────────────────

class TestAddition:
    def test_add_two_positive_integers(self, calc):
        """5 + 3 should equal 8."""
        assert calc.add(5, 3) == 8

    def test_add_positive_and_negative(self, calc):
        """10 + (-4) should equal 6."""
        assert calc.add(10, -4) == 6

    def test_add_two_decimal_numbers(self, calc):
        """1.1 + 2.2 should be approximately 3.3."""
        assert calc.add(1.1, 2.2) == pytest.approx(3.3)


# ─────────────────────────────────────────────
# Subtraction Tests
# ─────────────────────────────────────────────

class TestSubtraction:
    def test_subtract_two_positive_integers(self, calc):
        """10 - 4 should equal 6."""
        assert calc.subtract(10, 4) == 6

    def test_subtract_resulting_in_negative(self, calc):
        """3 - 7 should equal -4."""
        assert calc.subtract(3, 7) == -4


# ─────────────────────────────────────────────
# Multiplication Tests
# ─────────────────────────────────────────────

class TestMultiplication:
    def test_multiply_two_positive_integers(self, calc):
        """6 × 7 should equal 42."""
        assert calc.multiply(6, 7) == 42

    def test_multiply_by_zero(self, calc):
        """Any number multiplied by zero should equal zero."""
        assert calc.multiply(99999, 0) == 0

    def test_multiply_two_negative_numbers(self, calc):
        """(-3) × (-3) should equal 9."""
        assert calc.multiply(-3, -3) == 9


# ─────────────────────────────────────────────
# Division Tests
# ─────────────────────────────────────────────

class TestDivision:
    def test_divide_two_positive_integers(self, calc):
        """8 / 2 should equal 4.0."""
        assert calc.divide(8, 2) == 4.0

    def test_divide_by_zero_raises_error(self, calc):
        """Dividing by zero must raise ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            calc.divide(10, 0)

    def test_divide_negative_number(self, calc):
        """-9 / 3 should equal -3.0."""
        assert calc.divide(-9, 3) == -3.0


# ─────────────────────────────────────────────
# Edge Case Tests
# ─────────────────────────────────────────────

class TestEdgeCases:
    def test_add_very_large_numbers(self, calc):
        """Adding two very large numbers should not overflow."""
        assert calc.add(1e15, 1e15) == 2e15

    def test_multiply_decimal_numbers(self, calc):
        """0.1 × 0.2 should be approximately 0.02."""
        assert calc.multiply(0.1, 0.2) == pytest.approx(0.02)

    def test_divide_results_in_decimal(self, calc):
        """1 / 3 should be approximately 0.333..."""
        assert calc.divide(1, 3) == pytest.approx(1 / 3)


# ─────────────────────────────────────────────
# Clear Tests
# ─────────────────────────────────────────────

class TestClear:
    def test_clear_resets_result_to_zero(self, calc):
        """After any operation, clear() should reset current_result to 0."""
        calc.add(100, 200)
        result = calc.clear()
        assert result == 0
        assert calc.current_result == 0
