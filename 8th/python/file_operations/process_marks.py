# Finally we are ready to process the data

def avg(marklist):
    return sum(marklist)/len(marklist)

all_marks = []
with open("marks.csv", "r") as f:
    for line in f.readlines():
        name, marks = line.strip().split(",")
        # We also convert it to a number, so that we can do mathematical operations on it
        all_marks.append(int(marks))

print(all_marks)

print("Average marks : ", avg(all_marks))
