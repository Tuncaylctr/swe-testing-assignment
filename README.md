# Quick-Calc

A simple, well-tested command-line calculator application built in Python. **Quick-Calc** supports the four fundamental arithmetic operations — addition, subtraction, multiplication, and division — with graceful error handling, all driven by clean and testable code.

This project was developed as part of the *Advanced Software Engineering* course to demonstrate a professional software development workflow: feature implementation, multi-layered testing, conventional commits, and semantic versioning.

---

## Features

| Operation      | Example             |
|----------------|---------------------|
| Addition       | `5 + 3 = 8`         |
| Subtraction    | `10 − 4 = 6`        |
| Multiplication | `6 × 7 = 42`        |
| Division       | `8 / 2 = 4.0`       |
| Division by 0  | Raises `ZeroDivisionError` with a friendly message |
| Clear (C)      | Resets result to `0` |

---

## Project Structure

```
swe-testing-assignment/
├── calculator/
│   ├── __init__.py       # Package export
│   └── core.py           # Core Calculator class (business logic)
├── tests/
│   ├── __init__.py
│   ├── test_unit.py      # Unit tests (13 tests)
│   └── test_integration.py # Integration tests (4 tests)
├── main.py               # CLI entry point
├── pytest.ini            # Pytest configuration
├── requirements.txt      # Project dependencies
├── README.md             # This file
└── TESTING.md            # Testing strategy documentation
```

---

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- `pip` (comes with Python)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/<your-username>/swe-testing-assignment.git
   cd swe-testing-assignment
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Running the Application

```bash
python main.py
```

Follow the on-screen prompts. Type `C` to clear the display or `Q` to quit.

---

## How to Run Tests

All tests are executed with a **single command**:

```bash
pytest
```

This will automatically discover and run all test files matching `test_*.py` in the `tests/` directory, as configured in `pytest.ini`.

For verbose output with a summary:

```bash
pytest -v
```

To run only unit tests or only integration tests:

```bash
pytest tests/test_unit.py           # Unit tests only
pytest tests/test_integration.py    # Integration tests only
```

---

## Testing Framework Research: Pytest vs Unittest

### Overview

Python ships with a built-in testing module, **`unittest`**, modelled after Java's JUnit framework. A popular third-party alternative, **`pytest`**, has grown to dominate Python testing due to its simplicity and rich plugin ecosystem. Both can be used to test the same codebase, but they differ substantially in philosophy and developer experience.

### `unittest` — The Standard Library Choice

`unittest` is batteries-included: it ships with Python and requires zero installation. It follows an object-oriented, xUnit-style structure where every test lives inside a class that inherits from `unittest.TestCase`, and assertions are made through dedicated methods such as `self.assertEqual()`, `self.assertRaises()`, and `self.assertTrue()`. This structure is familiar to developers coming from Java or C#, and it integrates naturally with tools like the Python standard library's `unittest.mock`. The main downside is **boilerplate**: even the simplest test requires a class definition and method naming conventions, and the assertion API is more verbose than idiomatic Python.

### `pytest` — The Community Standard

`pytest` takes a "plain Python" approach. Tests are ordinary functions (or optionally classes without inheritance), and assertions are written using Python's native `assert` keyword — pytest rewrites assertion expressions at collection time to produce detailed, human-readable failure messages. Its **fixture system** (the `@pytest.fixture` decorator) allows clean dependency injection of shared test resources, far more composable than `unittest.setUp`/`tearDown`. `pytest` also natively runs `unittest`-style tests, making migration straightforward. The plugin ecosystem (`pytest-cov`, `pytest-mock`, `pytest-asyncio`, etc.) extends it far beyond basic unit testing.

### Justification for This Project

**`pytest` was chosen** for Quick-Calc because:

1. **Readability** — `assert result == 8` is more expressive than `self.assertEqual(result, 8)`, keeping tests close to natural language.
2. **Fixtures** — The `@pytest.fixture` decorator cleanly provides a fresh `Calculator()` instance to each test, avoiding shared mutable state.
3. **Approx comparisons** — `pytest.approx` elegantly handles floating-point precision, essential for decimal operation tests.
4. **Single command** — `pytest` auto-discovers tests and runs them without any runner configuration, satisfying the assignment's requirement for a simple test command.

---

## Version History

| Version | Description                              |
|---------|------------------------------------------|
| v1.0.0  | Initial release with full feature set and complete test suite |

---

## License

This project is submitted as coursework for educational purposes.
