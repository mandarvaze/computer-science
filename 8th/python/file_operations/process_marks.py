# Finally we are ready to process the data

def avg(marklist):
    return sum(marklist)/len(marklist)

all_marks = []
with open("marks.csv", "r") as f:
    for line in f.readlines():
        name, marks = line.strip().split(",")
        # We also convert it to a number, so that we can do mathematical operations on it
        all_marks.append(int(marks))

# Earlier we got average printed as 63.57142857142857
# Let us print only 2 digits after the decimal
#
# This is called f-strings, fancy way to print
# f-string stands for formatted string
print(f"Average marks : {avg(all_marks):.2f}")

# Top 3 marks
#
# We did the following in the classroom
# sorted_marks = sorted(all_marks, reverse=True)
# top_3 = sorted_marks[:3]
#
# But we can skip intermediate variables like sorted_marks and top_3 etc.
print("Top 3 highest marks: ", sorted(all_marks, reverse=True)[:3])
