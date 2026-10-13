"""
=============================================================================
MODULE 04: Loops (`for`, `while`), `range(start, stop, step)`, and Comparisons
=============================================================================
Loops are used to repeat a block of code multiple times. This module covers 
how to iterate efficiently, the differences between loop types, and common traps.
"""

# ==========================================
# 1. THE `range(start, stop, step)` BREAKDOWN
# ==========================================
# The range() function is the powerhouse of 'for' loops in Python. It takes 3 arguments:
# - start: Where the sequence begins (inclusive, defaults to 0 if left blank).
# - stop: Where the sequence ends (⚠️ EXCLUSIVE: it stops right *before* this number).
# - step: How much to increment/decrement by each time (defaults to 1).

print("--- Range Examples ---")
print("Using stop only range(3) -> starts at 0, stops before 3:")
for i in range(3):
    print(i, " ")  # Output: 0 1 2

print("\n\nUsing start and stop range(1, 5) -> starts at 1, stops before 5:")
for i in range(1, 5):
    print(i, " ")  # Output: 1 2 3 4

print("\n\nUsing start, stop, and step range(1, 10, 2) -> steps by 2:")
for i in range(1, 10, 2):
    print(i, " ")  # Output: 1 3 5 7 9


# ==========================================
# 2. `for` LOOPS vs. `while` LOOPS (WHEN TO USE WHICH)
# ==========================================
"""
=============================================================================
FEATURE             | FOR LOOP                      | WHILE LOOP
=============================================================================
Best Used For       | Definite iteration (when you  | Indefinite iteration (when you 
                    | know exact counts/items).     | loop based on a changing condition).
-----------------------------------------------------------------------------
Control Variable    | Handled automatically by      | Must be initialized manually 
                    | Python (e.g., in range/list). | and updated inside the loop.
-----------------------------------------------------------------------------
Risk of Infinite    | Very low (unless iterating    | High! If the condition never 
Loop                | over a dynamic changing list).| becomes False, it runs forever.
=============================================================================
"""

print("\n--- For Loop Example (Fixed Count) ---")
for attempt in range(1, 4):
    print(f"System login attempt {attempt}")

print("\n--- While Loop Example (Condition-Based) ---")
# Useful when you don't know how many times it will take, like user password retries
battery_level = 15
while battery_level > 0:
    print(f"Battery at {battery_level}%. Running...")
    battery_level -= 5  # Decreases battery until condition fails
print("Battery dead! Shutting down.\n")


# ==========================================
# 3. MANUAL FOR LOOP (UNDER THE HOOD)
# ==========================================
# We can recreate how a loop works using a custom function with start, stop, and step!
# (Note: For functions, check out `05_functions.py`)

def my_loop(stop, start=0, step=1):
    """
    A manual simulation of loop behavior using a while loop and parameters.
    """
    current = start
    while current < stop:
        print(f"Manual loop value: {current}")
        current += step

print("--- Testing Manual Loop ---")
my_loop(5, 1, 1)


# ==========================================
# 4. USING LOOPS TO ACCESS LISTS (Preview)
# ==========================================
# Loops are extremely powerful when combined with data structures.
# For a deep dive, check out `07_data_structures.py`!

print("\n--- Accessing Lists with Loops ---")
subjects = ["Math", "Python", "Physics", "Chemistry"]

# Direct item iteration
for subject in subjects:
    print("- Studying:", subject)


# ==========================================
# 5. ❌ LOOP TRAPS & COMMON MISTAKES (WHAT *NOT* TO DO)
# ==========================================
"""
--- TRAP 1: The Infinite `while` Loop ---
count = 1
while count <= 5:
    print(count)
    # ❌ ERROR: Forgot to write 'count += 1'. Runs infinitely!
"""

"""
--- TRAP 2: Misunderstanding `range()` Stop Value ---
# If you want to loop 5 times (1 through 5):
for i in range(1, 5):
    print(i)
# ❌ TRAP: This stops at 4! Use range(1, 6) instead.
"""


# ==========================================
# QUICK EXAM SUMMARY CHECKLIST:
# ==========================================
# 1. Use `for` loops when dealing with sequences or known counts. Use `while` for condition checks.
# 2. In `range(start, stop, step)`, the `stop` boundary value is always excluded.
# 3. Always update your loop variables in a `while` loop to avoid freezing your code.
# ==========================================
