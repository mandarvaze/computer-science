"""
=============================================================================
MODULE 06: Lists, Data Manipulation, and Dictionaries
=============================================================================
Compound data structures allow you to store multiple items in a single variable.
This module covers Lists (ordered, changeable sequences) and Dictionaries 
(key-value pairs for quick lookups).
"""

# ==========================================
# 1. LISTS: CREATION AND INDEXING
# ==========================================
# A list is an ordered collection of items enclosed in square brackets [].
# ⚠️ EXAM WATCHOUT: Python uses 0-based indexing! The first item is at index 0.

print("--- Lists and Indexing ---")
exam_subjects = ["Math", "Python", "Physics", "Chemistry"]

print("Full list:", exam_subjects)
print("First subject (index 0):", exam_subjects[0])  # Output: Math
print("Last subject (index -1):", exam_subjects[-1]) # Output: Chemistry (negative index counts from the back)


# ==========================================
# 2. LIST MUTATION AND METHODS
# ==========================================
# Lists are mutable, meaning you can change, add, or remove items after creation.

print("\n--- Modifying Lists ---")

# Adding items
exam_subjects.append("Biology")  # Adds to the very end
print("After append():", exam_subjects)

exam_subjects.insert(1, "English")  # Inserts at a specific index
print("After insert(1):", exam_subjects)

# Removing items
exam_subjects.remove("Physics")  # Removes by matching value name
print("After remove():", exam_subjects)

popped_item = exam_subjects.pop()  # Removes and returns the last item
print(f"Popped item: {popped_item} | Remaining list:", exam_subjects)


# ==========================================
# 3. LIST SLICING
# ==========================================
# Slicing allows you to extract a subset of a list using list[start:stop].
# ⚠️ EXAM WATCHOUT: Just like range(), the stop index is exclusive!

print("\n--- List Slicing ---")
numbers = [10, 20, 30, 40, 50, 60]
# Gets items from index 1 up to index 3 (excludes index 4)
subset = numbers[1:4] 
print("Slice numbers[1:4]:", subset)  # Output: [20, 30, 40]


# ==========================================
# 4. DICTIONARIES (KEY-VALUE PAIRS)
# ==========================================
# A dictionary stores data in key-value pairs inside curly brackets {}.
# Keys must be unique and immutable (like strings or numbers), while values can be anything.

print("\n--- Dictionaries ---")
student_record = {
    "name": "Alex",
    "grade": 8,
    "subject": "Python",
    "score": 95
}

print("Student Record Dictionary:", student_record)

# Accessing values using keys:
print("Student Name:", student_record["name"])
print("Student Score:", student_record.get("score"))

# Adding or updating dictionary entries:
student_record["score"] = 98  # Updates existing value
student_record["passed"] = True  # Adds a brand new key-value pair
print("Updated Record:", student_record)


# ==========================================
# 5. ❌ COMMON DATA STRUCTURE MISTAKES (WHAT *NOT* TO DO)
# ==========================================
"""
--- MISTAKE 1: Index Out of Range Error ---
my_list = [10, 20, 30]
# print(my_list[3])  # ❌ ERROR! Indexes only go from 0 to 2 for a length-3 list.
"""

"""
--- MISTAKE 2: Trying to access dictionary values using numeric index ---
student = {"name": "Sam", "age": 14}
# print(student[0])  # ❌ ERROR! Dictionaries are unordered; use the key name like student["name"]!
"""


# ==========================================
# QUICK EXAM SUMMARY CHECKLIST:
# ==========================================
# 1. Lists use square brackets `[]`, are ordered, and use 0-based indexing.
# 2. In list slicing `[start:stop]`, the `stop` index is excluded.
# 3. Dictionaries use curly brackets `{}` and store data as `key: value` pairs instead of positions.
# ==========================================
