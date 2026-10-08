# Just splitting was not helpful
# We get `\n`
# We use `strip()` to removing whitespaces from the beginning and the end of the string
#

all_marks = []
with open("marks.csv", "r") as f:
    for line in f.readlines():
        name, marks = line.strip().split(",")
        # We also convert it to a number, so that we can do mathematical operations on it
        all_marks.append(int(marks))

print(all_marks)
