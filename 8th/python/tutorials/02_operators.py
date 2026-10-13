"""
=============================================================================
MODULE 02: Operators (Arithmetic, Comparison, and Logical)
=============================================================================
Operators are special symbols used to perform operations on variables and values.
This file covers the three main types of operators tested in exams.
"""

# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================
# Used to perform standard mathematical calculations.

a = 10
b = 3

print() #blank line
print(" Arithmetic Operators")
print("Addition (a + b):", a + b)       # Output: 13
print("Subtraction (a - b):", a - b)    # Output: 7
print("Multiplication (a * b):", a * b) # Output: 30
print("Division (a / b):", a / b)       # Output: 3.3333333333333335 (Always yields a float)

# ⚠️ EXAM WATCHOUT FOR THESE TWO:
print("Floor Division (a // b):", a // b) # Output: 3 (Rounds down to the nearest whole integer)
print("Modulus / Remainder (a % b):", a % b) # Output: 1 (Gives the remainder of division: 10 = 3*3 + 1)
print("Exponent / Power (a ** b):", a ** b)  # Output: 1000 (10 to the power of 3)


# ==========================================
# 2. COMPARISON (RELATIONAL) OPERATORS
# ==========================================
# Used to compare two values. They always evaluate to a boolean (True or False).

x = 15
y = 20

print()
print(" Comparison Operators")
print("Is x equal to y? (x == y):", x == y)         # Output: False
print("Is x NOT equal to y? (x != y):", x != y)     # Output: True
print("Is x greater than y? (x > y):", x > y)       # Output: False
print("Is x less than y? (x < y):", x < y)          # Output: True
print("Is x greater than or equal to y? (x >= y):", x >= y) # Output: False
print("Is x less than or equal to y? (x <= y):", x <= y)    # Output: True


# ==========================================
# 3. LOGICAL OPERATORS
# ==========================================
# Used to combine multiple conditions together.
# - 'and': Returns True ONLY IF both conditions are true.
# - 'or': Returns True if AT LEAST ONE condition is true.
# - 'not': Reverses the boolean value (turns True to False, and vice versa).

is_student = True
has_id_card = False

print()
print(" Logical Operators")
# AND Operator
print("Both student AND has ID card:", is_student and has_id_card)  # Output: False

# OR Operator
print("Is student OR has ID card:", is_student or has_id_card)      # Output: True

# NOT Operator
print("NOT a student (not is_student):", not is_student)             # Output: False


# ==========================================
# QUICK EXAM SUMMARY CHECKLIST:
# ==========================================
# 1. Division (/) returns a float; Floor Division (//) discards the decimal.
# 2. Modulus (%) finds the remainder—extremely useful for checking even/odd numbers (num % 2 == 0).
# 3. Double equals (==) is for comparison; single equals (=) is for variable assignment.
# ==========================================
