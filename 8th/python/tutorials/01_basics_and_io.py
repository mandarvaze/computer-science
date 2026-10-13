"""
=============================================================================
MODULE 01: Basics, Variables, Data Types, and Input/Output (I/O)
=============================================================================
Welcome! This file introduces the foundational building blocks of Python.
Read through the comments and run the code to see how everything works.
"""

# ==========================================
# 1. PRINTING TO THE SCREEN (Output)
# ==========================================
# The print() function displays text or values onto the console screen.
print("Hello, Python learner! Welcome to your exam review.")
print("You can print numbers directly:", 42)
print("You can also perform math inside print:", 10 + 5)


# ==========================================
# 2. VARIABLES AND ASSIGNMENT
# ==========================================
# A variable is a container for storing data values. 
# In Python, you don't need to declare the type beforehand; just assign a value using '='.

student_name = "Alex"  # A string variable (text)
exam_score = 95        # An integer variable (whole number)
is_passed = True       # A boolean variable (True or False)

print("Student Info")
print("Name:", student_name)
print("Score:", exam_score)
print("Passed:", is_passed)


# ==========================================
# 3. CORE DATA TYPES
# ==========================================
# You can check the data type of any variable using the type() function.

age = 14               # int (integer)
percentage = 92.5      # float (decimal number)
subject = "Computer Science"  # str (string)
passed_exam = True     # bool (boolean)

print("Data Types Check")
print(type(age))         # Output: <class 'int'>
print(type(percentage))  # Output: <class 'float'>
print(type(subject))     # Output: <class 'str'>
print(type(passed_exam)) # Output: <class 'bool'>


# ==========================================
# 4. TAKING INPUT FROM THE USER (Input)
# ==========================================
# The input() function pauses the program and lets the user type something.
# ⚠️ EXAM WATCHOUT: input() ALWAYS returns data as a STRING, even if you type a number!

print(" User Input Demo ")
user_name = input("Enter your name: ")
print("Hello, " + user_name + "! Let's check your math skills.")


# ==========================================
# 5. TYPE CASTING (Converting Data Types)
# ==========================================
# Because input() returns a string, we must convert (cast) it to an integer or float 
# if we want to do arithmetic operations with it.

# Wrong way for numbers: 
# user_age = input("Enter age: ")
# next_year = user_age + 1  # ❌ ERROR! Can't add an integer to a string.

# Right way (Type Casting):
birth_year_str = input("Enter your birth year: ")  # e.g., "2012"
birth_year_int = int(birth_year_str)                # Converts string to integer 2012

current_year = 2026
calculated_age = current_year - birth_year_int

print("Approximate age calculated:", calculated_age)


# ==========================================
# QUICK EXAM SUMMARY CHECKLIST:
# ==========================================
# 1. print() shows output; input() takes text input.
# 2. input() ALWAYS outputs a string (str). Use int() or float() to convert it.
# 3. Variable names cannot start with a number (e.g., '8th_grade' is illegal, 'grade_8' is valid).
# ==========================================
