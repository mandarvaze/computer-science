students = {}
with open("marks.csv", "r") as f:
    for line in f.readlines():
        name, marks = line.strip().split(",")
        # We also convert it to a number, so that we can do mathematical operations on it
        students[name] = int(marks)

print(students)

# We do not need separate list of marks
# dict has .values() function which returns list of all the values
print(f"Average marks: {(sum(students.values())/len(students)):.2f}")

print("Top 3 Highest marks:", sorted(students.values(), reverse=True)[:3])
