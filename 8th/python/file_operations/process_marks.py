# We do not really process marks
# This is what most of you did (after reading the entire file as a single chunk)

with open("marks.csv", "r") as f:
    for line in f.readlines():
        print(line)
