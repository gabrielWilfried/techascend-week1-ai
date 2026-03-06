"""
python fundamental excercises
-------------------------------
Covers: variables, loops, functions, lists, dictionaries, and a mini problem.
"""

# ─────────────────────────────────────────────
# 1. VARIABLES
# ─────────────────────────────────────────────

age: int = 25
name: str = "Gabriel"
temperature: float = 36.9

print("=" * 40)
print("1. VARIABLES")
print("=" * 40)
print(f"  Integer : {age!r}  → type: {type(age).__name__}")
print(f"  Float   : {temperature!r}  → type: {type(temperature).__name__}")
print(f"  String  : {name!r}  → type: {type(name).__name__}")

# ─────────────────────────────────────────────
# 2. LOOPS
# ─────────────────────────────────────────────

print("\n" + "=" * 40)
print("2. LOOPS  (1 → 10)")
print("=" * 40)
print("Print numbers from 1 to 10 using a for loop")
for number in range(1, 11):
    print(number)

print("Print numbers from 1 to 10 using a while loop")
num = 1
while num <= 10:
    print(num)
    num += 1


# ─────────────────────────────────────────────
# 3. FUNCTIONS
# ─────────────────────────────────────────────

def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numbers.

        Args:
            a: First operand.
            b: Second operand.

        Returns:
            The arithmetic sum of *a* and *b*.
    """
    return a + b
print("\n" + "=" * 40)
print("3. FUNCTIONS")
print("=" * 40)
result = add_numbers(7.0, 3.0)
print(f"The sum is: {result}")

# ─────────────────────────────────────────────
# 4. LISTS
# ─────────────────────────────────────────────

# Create a list of fruits
players: list[str] = ["kobe", "jordan", "curry", "james", "siakam"]

print("\n" + "=" * 40)
print("4. LISTS")
print("=" * 40)
print("iterating over players:")
for index, player in enumerate(players, start=1):
    print(f" {index}. {player}")

# ─────────────────────────────────────────────
# 5. DICTIONARY
# ─────────────────────────────────────────────

person: dict[str, str | int] = {
    "name": "Yagaka Gabriel",
    "age": 25,
    "city": "Yaoundé",
}
print("\n" + "=" * 40)
print("5. DICTIONARY")
print("=" * 40)
for key, value in person.items():
    print(f"  {key.capitalize():<6}: {value}")


# ─────────────────────────────────────────────
# 6. MINI PROBLEM – word analyser
# ─────────────────────────────────────────────

def analyse_sentence(sentence: str) -> dict[str, int | list[str]]:
    """Analyse a sentence and return basic statistics i.e. the number of words, characters, and unique words form the sentence.

    Args:
        sentence: Raw text entered by the user.

    Returns:
        A dict with 'word_count', 'char_count', and 'unique_words'.
    """
    words = sentence.lower().split()

    return {
        "word_count": len(words),
        "char_count": len(sentence.replace(" ", "")),
        "unique_words": sorted(set(words)),
    }


def run_mini_problem() -> None:
    """Ask the user to enter a sentence and print the analysis."""

    print("\n" + "=" * 40)
    print("6. MINI PROBLEM – Sentence Analyser")
    print("=" * 40)

    user_input = input("Enter a sentence: ").strip()

    if not user_input:
        print("No input provided. Analysis aborted.")
        return

    analysis = analyse_sentence(user_input)

    print("\nAnalysis Results:")
    print(f"  Word Count: {analysis['word_count']}")
    print(f"  Character Count: {analysis['char_count']}")
    print(f"  Unique Words: {', '.join(analysis['unique_words'])}")

if __name__ == "__main__":
    run_mini_problem()
