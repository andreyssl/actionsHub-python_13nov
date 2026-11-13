# Exercise: Python Testing with pytest and GitHub Actions

In this exercise you will explore an existing Python project, run its automated tests,
watch them fail, understand why, fix the code, and finally push to GitHub to see
the same test pipeline run in the cloud via GitHub Actions.

---

## Learning Objectives

By the end of this exercise you will be able to:

- Fork a repository and clone it locally
- Read and understand an existing Python project structure
- Install project dependencies from a `requirements.txt` file
- Run automated tests with `pytest` and read the output
- Understand what a failing test is telling you
- Fix code to make tests pass
- Push code to GitHub and observe a CI pipeline run

---

## Project Structure

Before writing a single line of code, take a few minutes to look at every file in this repo:

```
.
├── calc.py               # A calculator script
├── greet.py              # A greeting script
├── test_calc.py          # Tests for calc.py
├── test_greet.py         # Tests for greet.py
├── requirements.txt      # Python dependencies
└── .github/
    └── workflows/
        ├── calc.yml      # GitHub Actions workflow (runs calc.py)
        └── test.yml      # GitHub Actions workflow (runs the tests)
```

---

## Part 1 — Fork and Clone

1. Go to the GitHub page for this repository.
2. Click **Fork** (top right). This creates your own copy of the repo under your GitHub account.
3. Clone **your fork** to your machine:

```bash
git clone git@github.com:YOUR_USERNAME/REPO_NAME.git
cd REPO_NAME
```

4. Open the folder in VS Code:

```bash
code .
```

---

## Part 2 — Analyse the Project (Read Before You Code)

Open each file and read it carefully. Then answer the questions below in your head
or write them down — you will need this understanding for the rest of the exercise.

### Questions about `calc.py`

- What does the `calculate` function take as inputs?
- What does it return?
- Which operators are currently implemented?
- What does `if __name__ == "__main__":` mean? Why is it there?
- What happens if you run `python calc.py` directly in the terminal?

### Questions about `greet.py`

- What does `greet_user` do?
- What does `if __name__ == "__main__":` protect here?
- If you import `greet.py` in another file, will the `input()` line run? Why or why not?

### Questions about `test_calc.py` and `test_greet.py`

Open `test_calc.py`:

```python
from calc import calculate

def test_addition():
    assert calculate(10, "+", 3) == 13

def test_subtraction():
    assert calculate(10, "-", 3) == 7

def test_multiplication():
    assert calculate(10, "*", 3) == 30

def test_division():
    assert calculate(10, "/", 2) == 5

def test_invalid_operator():
    assert calculate(10, "%", 3) is None
```

- What does `assert` do?
- What does `from calc import calculate` mean?
- How many tests are there for the calculator?
- Based on what you read in `calc.py`, which of these tests do you expect to **pass** and which to **fail**? Write down your prediction before running anything.

Open `test_greet.py`:

```python
from greet import greet_user

def test_greet_user(capsys):
    greet_user("Alice")
    captured = capsys.readouterr()
    assert captured.out == "Hello Alice\n"
```

- What is `capsys`? (Hint: it is a pytest feature that captures printed output.)
- What exact string does the test expect `greet_user("Alice")` to print?
- Look at `greet.py` — what does `greet_user` currently print?
- Do you expect this test to pass or fail?

### Questions about `requirements.txt`

```
pytest
```

- What is `requirements.txt` used for?
- How would you install everything listed in it?

### Questions about the GitHub Actions workflows

Open `.github/workflows/test.yml`:

```yaml
name: Run Tests

on: [push]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run tests
        run: pytest
```

- When does this workflow trigger?
- What operating system does it run on?
- What are the three steps it executes in order?
- What do you think will happen when you push your code to GitHub right now, before fixing anything?

---

## Part 3 — Install Dependencies and Run the Tests (Broken State)

### Install pytest

```bash
pip install -r requirements.txt
```

You should see output like:

```
Successfully installed pytest-x.x.x ...
```

### Run the tests

```bash
pytest
```

Read the output carefully. You will see something like this:

```
========================= FAILURES ==========================

FAILED test_calc.py::test_subtraction - assert None == 7
FAILED test_calc.py::test_multiplication - assert None == 30
FAILED test_calc.py::test_division - assert None == 5
FAILED test_greet.py::test_greet_user - AssertionError: assert 'Hi Alice\n' == 'Hello Alice\n'

==================== 2 passed, 4 failed ====================
```

### Understand the output

Look at the failure messages one by one:

**`assert None == 7`**
The test called `calculate(10, "-", 3)` and expected `7`, but got `None`.
This means the subtraction case is not implemented — the function falls through to `return None`.

**`assert 'Hi Alice\n' == 'Hello Alice\n'`**
The test expected the output `"Hello Alice\n"` but the function printed `"Hi Alice\n"`.
One word is wrong. Tests are exact — even a single character difference is a failure.

### Check your predictions

- Did the results match what you predicted in Part 2?
- Which 2 tests passed? Why do those pass while the others do not?

---

## Part 4 — Push the Broken Code to GitHub

Before fixing anything, push the code as-is so you can see GitHub Actions run and fail.

```bash
git add .
git commit -m "start exercise - tests failing"
git push
```

Now go to your repository on GitHub:

1. Click the **Actions** tab at the top.
2. You will see a workflow run appear (it may take a few seconds to start).
3. Click on it to open it, then click on the **test** job.
4. Expand the **Run tests** step.

You should see the exact same pytest output you saw locally:

```
FAILED test_calc.py::test_subtraction - assert None == 7
FAILED test_calc.py::test_multiplication - assert None == 30
FAILED test_calc.py::test_division - assert None == 5
FAILED test_greet.py::test_greet_user - AssertionError: assert 'Hi Alice\n' == 'Hello Alice\n'
```

The red cross next to your commit on the main page also shows the pipeline failed.

> This is exactly how CI (Continuous Integration) works in real projects:
> every push is automatically tested, and the team can see at a glance
> whether the code is in a working state.

---

## Part 5 — Fix the Code

Now it is time to write code. You should fix **only** `calc.py` and `greet.py`.
Do **not** modify the test files.

### Fix `greet.py`

Open `greet.py`. Find the `greet_user` function and look at what it currently prints:

```python
def greet_user(user_name):
    # TODO: greet the user with the correct greeting
    print("Hi", user_name)
```

The test expects `"Hello Alice\n"`. What needs to change?

Fix it, then run the greet test on its own to confirm:

```bash
pytest test_greet.py -v
```

You should see:

```
PASSED test_greet.py::test_greet_user
PASSED test_greet.py::test_greet_user_different_name
```

### Fix `calc.py`

Open `calc.py`. Find the `calculate` function:

```python
def calculate(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    # TODO: implement subtraction
    # TODO: implement multiplication
    # TODO: implement division
    else:
        return None
```

Add the three missing cases. Use `elif` just like the `+` case.

Run the calculator tests to check your work:

```bash
pytest test_calc.py -v
```

You should see:

```
PASSED test_calc.py::test_addition
PASSED test_calc.py::test_subtraction
PASSED test_calc.py::test_multiplication
PASSED test_calc.py::test_division
PASSED test_calc.py::test_invalid_operator
```

### Run all tests

Once both files are fixed, run the full suite:

```bash
pytest
```

Expected output:

```
==================== 7 passed in 0.XXs ====================
```

All 7 tests pass.

---

## Part 6 — Push the Fixed Code to GitHub

```bash
git add .
git commit -m "fix calc and greet - all tests passing"
git push
```

Go back to the **Actions** tab on GitHub. A new workflow run will appear.
This time, all steps should complete with a green checkmark.

Click into the run → **test** job → **Run tests** step.
You should see:

```
==================== 7 passed in 0.XXs ====================
```

The commit on your main page will now show a green checkmark instead of a red cross.

---

## Bonus Challenges

If you finish early, try these:

1. **Add a new operator** — implement modulo (`%`) in `calculate()`. Then update `test_invalid_operator` in `test_calc.py` to test a truly invalid operator (like `^`) and add a new test for `%`. Run the tests to confirm they pass.

2. **Break a test on purpose** — change `return num1 + num2` to `return num1 - num2`. Run pytest. Read the error. Then fix it back.

3. **Read the `calc.yml` workflow** — it uses `printf` to pipe input into `calc.py`. Why does it do this instead of just running `python calc.py` directly?

---

## Summary

| Step | What you did |
|------|-------------|
| Fork & clone | Got your own copy of the repo |
| Analyse | Read the code and predicted what would fail |
| Run tests (broken) | Saw real pytest failure messages |
| Push broken | Saw the same failures in GitHub Actions |
| Fix code | Implemented the missing logic |
| Run tests (fixed) | Confirmed all 7 tests pass |
| Push fixed | Saw the green checkmark in GitHub Actions |
