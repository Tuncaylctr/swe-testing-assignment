# TESTING.md — Quick-Calc Testing Strategy

## 1. Overview

This document describes the testing strategy applied to the **Quick-Calc** calculator application and explains how that strategy maps to the core software testing concepts covered in Lecture 3 of the Advanced Software Engineering course.

---

## 2. What Was Tested

| Component | What Was Tested |
|-----------|-----------------|
| `Calculator.add()` | Positive integers, mixed sign, decimal precision |
| `Calculator.subtract()` | Positive integers, result crossing into negatives |
| `Calculator.multiply()` | Two positives, multiply-by-zero, two negatives |
| `Calculator.divide()` | Normal division, division by zero (error), negative dividend |
| `Calculator.clear()` | Reset to zero, return value, `current_result` state |
| User workflows | Full add session (5+3=8), clear after multiply, chained ops, graceful zero-division |

## 3. What Was NOT Tested (and Why)

| Area | Reason Not Tested |
|------|------------------|
| **CLI interface** (`main.py`) | The CLI reads from `stdin` and writes to `stdout`; testing it directly requires mocking I/O, which adds complexity. The core logic it delegates to (`Calculator`) is fully covered. If this were a production system, the CLI would be integration-tested against the CLI layer using a tool like `pexpect`. |
| **Performance / load** | Quick-Calc performs in-memory arithmetic — there are no realistic scalability concerns for this scope. |
| **Concurrency** | The `Calculator` object is not shared across threads; concurrency issues are out of scope. |
| **Security** | Input validation for type errors is handled by Python's type system and the CLI's `try/except` block. SQL injection, buffer overflows, etc. are irrelevant for a CLI calculator. |

---

## 4. Testing Strategy in Relation to Lecture Concepts

### 4.1 The Testing Pyramid

The Testing Pyramid (Cohn, 2009) prescribes having many unit tests at the base, fewer integration tests in the middle, and even fewer end-to-end tests at the top.

Quick-Calc's test suite follows these proportions:

```
            ┌──────────┐
            │  E2E (0) │   ← CLI interaction not automated
           ┌┴──────────┴┐
           │Integration │   ← 4 tests (test_integration.py)
          ┌┴────────────┴┐
          │  Unit Tests  │  ← 13 tests (test_unit.py)
          └──────────────┘
```

- **Unit tests (13)** are fast, isolated, and verify every function in isolation — forming the wide, stable base.
- **Integration tests (4)** verify that the `Calculator` object behaves correctly in realistic end-to-end workflows, including sequential multi-step sessions.
- **No E2E tests** were written for the CLI layer; the business logic it delegates to is covered at lower levels.

This matches the pyramid's intent: invest the most in fast, granular unit tests and use integration tests sparingly to verify cross-component behaviour.

---

### 4.2 Black-Box vs White-Box Testing

**Unit tests** used a **white-box** approach: because the implementation of `Calculator` was known, tests were written to exercise specific code paths — for example, testing that `current_result` is updated after each operation and that `clear()` sets it back to exactly `0`. Tests like `test_multiply_by_zero` target the multiplicative identity path deliberately.

**Integration tests** took a **black-box** perspective: they simulate how a user (or a UI layer) would interact with the calculator without knowledge of the internal state machine. `test_full_addition_workflow` mimics a user pressing buttons and checking the display; it does not inspect any private attributes.

---

### 4.3 Functional vs Non-Functional Testing

**Functional testing** asks: *does the software do what it is supposed to do?* All 17 tests in this suite are functional — they assert that specific inputs produce correct outputs (e.g., `divide(8, 2) == 4.0`, `clear()` returns `0`).

**Non-functional testing** (performance, security, usability, reliability) was **intentionally not automated** for this project:
- *Performance*: Python's native arithmetic is O(1) and well within any acceptable threshold.
- *Usability*: Usability of a CLI is best assessed manually or through user research, not automated assertions.
- *Security*: There is no attack surface (no network, no persistence, no authentication).

Documenting what was *not* tested is as important as documenting what was, because it shows deliberate scope management rather than oversight.

---

### 4.4 Regression Testing

The test suite serves as a **regression safety net**. Because all 17 tests can be executed in under one second with `pytest`, they should be run:

1. **Before every commit** — locally, to prevent committing broken changes.
2. **On every pull request** — via a CI/CD pipeline (e.g., GitHub Actions) to block regressions from merging.
3. **After every dependency upgrade** — to catch unintended breaking changes introduced by updated packages.

For example, if a future contributor refactors `Calculator.divide()` to use integer division (`//`), the test `test_divide_results_in_decimal` (which asserts `divide(1, 3) ≈ 0.333`) would immediately catch the regression. Similarly, any change to `clear()` that fails to reset `current_result` would be caught by `test_clear_resets_result_to_zero`.

---

## 5. Test Results Summary

All 17 tests pass. The following table documents each test, its type, and its status:

| # | Test Name | Type | Status |
|---|-----------|------|--------|
| 1 | `test_add_two_positive_integers` | Unit | ✅ PASS |
| 2 | `test_add_positive_and_negative` | Unit | ✅ PASS |
| 3 | `test_add_two_decimal_numbers` | Unit | ✅ PASS |
| 4 | `test_subtract_two_positive_integers` | Unit | ✅ PASS |
| 5 | `test_subtract_resulting_in_negative` | Unit | ✅ PASS |
| 6 | `test_multiply_two_positive_integers` | Unit | ✅ PASS |
| 7 | `test_multiply_by_zero` | Unit | ✅ PASS |
| 8 | `test_multiply_two_negative_numbers` | Unit | ✅ PASS |
| 9 | `test_divide_two_positive_integers` | Unit | ✅ PASS |
| 10 | `test_divide_by_zero_raises_error` | Unit | ✅ PASS |
| 11 | `test_divide_negative_number` | Unit | ✅ PASS |
| 12 | `test_add_very_large_numbers` | Unit (Edge Case) | ✅ PASS |
| 13 | `test_multiply_decimal_numbers` | Unit (Edge Case) | ✅ PASS |
| 14 | `test_divide_results_in_decimal` | Unit (Edge Case) | ✅ PASS |
| 15 | `test_clear_resets_result_to_zero` | Unit | ✅ PASS |
| 16 | `test_full_addition_workflow` | Integration | ✅ PASS |
| 17 | `test_clear_after_calculation_resets_to_zero` | Integration | ✅ PASS |
| 18 | `test_sequential_operations_workflow` | Integration | ✅ PASS |
| 19 | `test_division_by_zero_in_workflow_is_graceful` | Integration | ✅ PASS |

**Total: 19 tests — 19 PASSED, 0 FAILED, 0 ERRORS**

---

## 6. Running the Tests

```bash
# Run all tests
pytest

# Run only unit tests
pytest tests/test_unit.py

# Run only integration tests
pytest tests/test_integration.py

# Run with coverage report (requires pytest-cov)
pip install pytest-cov
pytest --cov=calculator --cov-report=term-missing
```
