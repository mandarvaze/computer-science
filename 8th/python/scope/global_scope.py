def change_x():
    global x # Inform the Python interpreter NOT to create new local variable
    x=4

x=5  # Define variable x and assign value 5
change_x() # Change X to 4
print("x is: ",x) # Do we get what we want?
