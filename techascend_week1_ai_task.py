"""
python fundamental excercises
-------------------------------
Covers: variables, loops, functions, lists, dictionaries, and a mini program.
"""

# ─────────────────────────────────────────────
# 1. VARIABLES
# ─────────────────────────────────────────────

age: int = 25
name: str = "Gabriel"
temperature: float = 36.9

# ─────────────────────────────────────────────
# 2. LOOPS
# ─────────────────────────────────────────────

print("Print numbers from 1 to 10 using a for loop")
for number in range(1, 11):
    print(number)

print("Print numbers from 1 to 10 using a while loop")
num = 1
while num <= 10:
    print(num)
    num += 1
