"""
=============================================================================
MODULE 05: Functions, Parameters, Return Values, and Scope
=============================================================================
A function is a reusable block of code that performs a specific task. 
Instead of writing the same code over and over, you write it once inside 
a function and call it whenever you need it.
"""

# ==========================================
# 1. BASIC FUNCTION DEFINITION AND CALLING
# ==========================================
# Use the 'def' keyword to define a function, followed by parentheses () and a colon (:).
# ⚠️ EXAM WATCHOUT: Defining a function doesn't run it! You must *call* it.

print("--- Basic Function ---")

def say_hello():
    # A simple function that prints a welcome message.
    print("Hello! Welcome to Python functions.")

# Calling the function:
say_hello()


# ==========================================
# 2. FUNCTIONS WITH PARAMETERS & ARGUMENTS
# ==========================================
# Parameters are variables listed inside the parentheses in the function definition.
# Arguments are the actual values you pass into the function when you call it.

print("\n--- Functions with Parameters ---")

def greet_student(student_name, subject):
    print("Good luck" , student_name , "! Ready to ace your ", subject , " exam?")

# Calling with arguments:
greet_student("Alex", "Python")
greet_student("Sam", "Mathematics")


# ==========================================
# 3. DEFAULT ARGUMENTS & KEYWORD ARGUMENTS
# ==========================================
# You can give parameters default values (like we did in our `my_loop` function in Module 04!).
# If the caller doesn't provide an argument, the default value is used.

print("\n--- Default and Keyword Arguments ---")

def calculate_total_marks(scored, max_marks=100):
    percentage = (scored / max_marks) * 100
    return percentage

# Using default max_marks (100):
result1 = calculate_total_marks(45)
print("Percentage with default max (100): " , result1 , "%")

result2 = calculate_total_marks(85, 150)
print("Percentage with custom max (150): " , result2 , "%")


# ==========================================
# 4. THE `return` STATEMENT vs. `print()`
# ==========================================
# ⚠️ EXAM TRAP: Students often confuse `print()` with `return`.
# - print(): Just displays text on the screen. The function actually returns `None`.
# - return: Sends a value *back* out of the function so you can store it in a variable and use it later.

print("\n--- Return vs Print ---")

def add_numbers_r(a, b): # return function
    return a + b  # Sends the calculated sum back

def add_numbers_p(a, b):
  print(a+b)
# We can store the returned value in a variable:
sum_result = add_numbers_r(10, 20)
sum_result1 = add_numbers_p(10, 20)
# ^^^ doesnt save to the variable
print("Stored sum from function: ", sum_result)
print("Stored? sum from function: ", sum_result1)

# ==========================================
# 5. VARIABLE SCOPE (LOCAL vs. GLOBAL)
# ==========================================
# - Local Variable: Created *inside* a function. It cannot be accessed outside of it.
# - Global Variable: Created *outside* all functions. It can be read anywhere.

print("\n--- Variable Scope ---")

global_subject = "Computer Science"  # Global variable

def check_scope():
    local_score = 95  # Local variable
    print("Inside function - Global variable can be read:", global_subject)
    print("Inside function - Local variable:", local_score)

check_scope()

# print(local_score)  # ❌ ERROR! local_score doesn't exist outside the function!


# ==========================================
# 6. ❌ COMMON FUNCTION MISTAKES (WHAT *NOT* TO DO)
# ==========================================
"""
--- MISTAKE 1: Forgetting the colon ':'or parentheses () ---
# THIS WILL CAUSE A SyntaxError
def my_func
    print("Hello")
"""

"""
--- MISTAKE 2: Trying to use a returned value without capturing it or using print ---
def square(x):
    return x * x

square(5)  # ❌ Code runs, but the answer is lost because it wasn't assigned or printed!
print(square(5))  # ✅ Correct way to view it.
"""


# ==========================================
# QUICK EXAM SUMMARY CHECKLIST:
# ==========================================
# 1. Functions are defined using `def function_name(parameters):`.
# 2. Always use `return` if you want to use the function's result later in your program.
# 3. Variables created inside a function are "local" and vanish once the function finishes running.
# ==========================================
