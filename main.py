#!/usr/bin/env python3
"""
Quick-Calc — A simple command-line calculator application.
Supports addition, subtraction, multiplication, division, and clear.
"""

from calculator.core import Calculator


OPERATIONS = {
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",
}

MENU = """
╔══════════════════════════════╗
║        Quick-Calc v1.0       ║
╠══════════════════════════════╣
║  Operators: +  -  *  /       ║
║  Commands : C (clear) Q (quit)║
╚══════════════════════════════╝
"""


def get_number(prompt: str) -> float:
    """Prompt the user for a number until a valid float is entered."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)
        except ValueError:
            print(f"  ⚠ '{raw}' is not a valid number. Please try again.")


def run_session():
    """Run an interactive calculator session."""
    calc = Calculator()
    print(MENU)

    while True:
        # --- First operand ---
        first_input = input("Enter first number (or 'C' to clear / 'Q' to quit): ").strip()

        if first_input.upper() == "Q":
            print("Goodbye! 👋")
            break

        if first_input.upper() == "C":
            calc.clear()
            print("  → Display cleared. Current result: 0\n")
            continue

        try:
            a = float(first_input)
        except ValueError:
            print(f"  ⚠ '{first_input}' is not a valid number.\n")
            continue

        # --- Operator ---
        op = input("Enter operator (+, -, *, /): ").strip()
        if op not in OPERATIONS:
            print(f"  ⚠ Unknown operator '{op}'.\n")
            continue

        # --- Second operand ---
        b = get_number("Enter second number: ")

        # --- Compute ---
        method = getattr(calc, OPERATIONS[op])
        try:
            result = method(a, b)
            print(f"  → Result: {a} {op} {b} = {result}\n")
        except ZeroDivisionError as exc:
            print(f"  ⚠ Error: {exc}\n")


if __name__ == "__main__":
    run_session()
