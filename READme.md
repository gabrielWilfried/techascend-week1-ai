# 🐍 Python Fundamentals Exercises

A clean, well-documented Python script covering the core building blocks of the language — written to modern best-practice standards (PEP 8, PEP 526, type hints, docstrings).

---

## 📋 Table of Contents

- [Overview](#overview)
- [Exercises Covered](#exercises-covered)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Code Standards](#code-standards)
- [Example Output](#example-output)
- [Author](#author)

---

## Overview

This project is a single-file Python reference covering six fundamental programming concepts. Each section is clearly delimited, independently readable, and written with production-quality conventions — making it useful both as a learning resource and as a coding style reference.

---

## Exercises Covered

| # | Topic | What it demonstrates |
|---|-------|----------------------|
| 1 | **Variables** | `int`, `float`, and `str` declarations with type annotations |
| 2 | **Loops** | `for` loop with `range()` to iterate 1 → 10 |
| 3 | **Functions** | Typed function with docstring returning the sum of two numbers |
| 4 | **Lists** | 5-item list iterated with `enumerate()` |
| 5 | **Dictionary** | Person record printed key-by-key with `.items()` |
| 6 | **Mini Problem** | Interactive sentence analyser — input → process → output |

---

## Requirements

- **Python 3.10+** (uses `X | Y` union type syntax from PEP 604)
- No third-party dependencies — standard library only

---

## Usage

**Clone or download the file, then run:**

```bash
python techascend_week1_ai_task.py
```

The script will:
1. Automatically print the output for exercises 1–5
2. Prompt you interactively for exercise 6 (the mini problem)

**Example run:**

```
Enter a sentence: The quick brown fox jumps
```

---

## File Structure

```
📄 python_fundamentals_exercises.py   ← single script, all exercises
📄 README.md                          ← this file
```

---

## Code Standards

This script was written to the following standards:

- **[PEP 8](https://peps.python.org/pep-0008/)** — style guide for Python code (naming, spacing, line length)
- **[PEP 526](https://peps.python.org/pep-0526/)** — variable annotation syntax (`age: int = 25`)
- **[PEP 604](https://peps.python.org/pep-0604/)** — union types with `X | Y` instead of `Optional[X]`
- **Google-style docstrings** — `Args` / `Returns` sections on all functions
- **`if __name__ == "__main__"`** guard — separates library-safe logic from script execution
- **Separation of concerns** — pure data-processing functions kept separate from I/O functions

---

## Example Output

```
========================================
1. VARIABLES
========================================
  Integer : 25  → type: int
  Float   : 36.9  → type: float
  String  : 'Gabriel'  → type: str

========================================
2. LOOPS  (1 → 10)
========================================
  Print numbers from 1 to 10 using a for loop   
  1
  2
  ...
  10
  Print numbers from 1 to 10 using a while loop
  1
  2
  ...
  10

========================================
3. FUNCTIONS
========================================
  The sum is: 10.0

========================================
4. LISTS
========================================
  iterating over players:
    1. kobe
    2. jordan
    3. curry
    4. james
    5. siakam

========================================
5. DICTIONARY
========================================
  Name  : Yagaka Gabriel
  Age   : 25
  City  : Yaoundé

========================================
6. MINI PROBLEM – Sentence Analyser
========================================
  Enter a sentence: The quick brown fox jumps

  Word count   : 5
  Char count   : 21
  Unique words : brown, fox, jumps, quick, the
```

---

## Author

Built as a Python fundamentals reference with a focus on clean, idiomatic, and maintainable code by YAGAKA TAGNE GABRIEL WILFRIED for TechAscend-week1-ai-task.