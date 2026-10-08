# Here we split the line into name and marks
# Save the marks in a list

all_marks = []
with open("marks.csv", "r") as f:
    for line in f.readlines():
        name, marks = line.split(",")
        all_marks.append(marks)

print(all_marks)
