"""
=============================================================================
MODULE 03: Control Flow (Conditional Statements & Common Pitfalls)
=============================================================================
Control flow allows your program to make decisions and execute different blocks 
of code depending on whether certain conditions are true or false.
"""

# ==========================================
# 1. THE IF STATEMENT
# ==========================================
# An 'if' statement checks a condition. If it evaluates to True, the indented code runs.
score = 85

print("--- Basic If Statement ---")
if score >= 50:
    print("Congratulations! You passed the exam.")


# ==========================================
# 2. THE IF-ELSE STATEMENT
# ==========================================
# Use 'else' to provide an alternative block of code that runs when the 'if' condition is False.
print("\n--- If-Else Statement ---")
temperature = 28

if temperature > 30:
    print("It's a hot day outside. Stay hydrated!")
else:
    print("The weather is pleasant.")


# ==========================================
# 3. THE ELIF (ELSE-IF) STATEMENT & THE 'IF' RULE
# ==========================================
# ⚠️ CRITICAL RULE: An 'elif' statement ALWAYS requires an 'if' statement at the very start. 
# You cannot use 'elif' or 'else' by themselves without a preceding 'if'. 
# Furthermore, 'else' must always be at the very end of the ladder.

print("\n--- Grading System (If-Elif-Else) ---")
marks = 78

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "Needs Improvement"

print(f"Your marks: {marks} | Grade assigned: {grade}")


# ==========================================
# 4. ❌ WRONG CODE EXAMPLES (WHAT *NOT* TO DO)
# ==========================================
# Read these carefully so you don't lose marks in your exam due to syntax errors!

"""
--- MISTAKE 1: Using 'elif' or 'else' without an 'if' ---
# THIS WILL CAUSE A SyntaxError: invalid syntax
elif marks >= 50:
    print("Pass")
"""

"""
--- MISTAKE 2: Forgetting the colon (:) at the end of conditional lines ---
# THIS WILL CAUSE A SyntaxError: expected ':'
if marks >= 50
    print("Passed")
"""

"""
--- MISTAKE 3: Incorrect Indentation ---
# THIS WILL CAUSE AN IndentationError: expected an indented block
if marks >= 50:
print("Passed")  # Missing 4-space indentation!
"""

"""
--- MISTAKE 4: Using assignment (=) instead of comparison (==) inside conditions ---
# THIS WILL CAUSE A SyntaxError or logic bug
if marks = 50:  # Single '=' assigns a value; use '==' to compare!
    print("Half marks")
"""


# ==========================================
# QUICK EXAM SUMMARY CHECKLIST:
# ==========================================
# 1. Every 'if', 'elif', and 'else' block MUST end with a colon (:).
# 2. Indentation (4 spaces) is mandatory for code inside the block.
# 3. An 'elif' can NEVER exist on its own; it must follow an 'if' statement.
# 4. Use '==' for checking equality, not '='.
# ==========================================
