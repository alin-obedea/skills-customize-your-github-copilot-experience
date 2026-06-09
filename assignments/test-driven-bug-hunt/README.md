# 📘 Assignment: Test-Driven Bug Hunt in Python

## 🎯 Objective

Practice writing focused unit tests with Python's built-in `unittest` module, then use those tests to find and fix bugs in a small program.

## 📝 Tasks

### 🛠️ Write Tests Before Fixing Code

#### Description
Open the starter program and read the function and class docstrings. Create a test file named `test_starter_code.py` and write tests for each behavior before changing the implementation.

#### Requirements
Completed program should:

- Create `test_starter_code.py` using the built-in `unittest` module (no external libraries)
- Include at least 6 tests covering normal cases and edge cases
- Test all public behaviors: `calculate_average`, `grade_letter`, and `StudentSummary.is_passing()`
- Include at least one test for invalid input in `calculate_average`


### 🛠️ Fix Bugs and Confirm with Tests

#### Description
After writing tests, run them and fix the bugs in `starter-code.py` until all tests pass.

#### Requirements
Completed program should:

- Keep function names and class names unchanged
- Make all written tests pass without deleting tests
- Ensure `calculate_average` raises `ValueError` for an empty score list
- Ensure grade boundaries are correct: A (90+), B (80-89), C (70-79), D (60-69), F (<60)
