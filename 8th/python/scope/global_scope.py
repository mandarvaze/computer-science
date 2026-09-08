def change_x(new_value):
    global x # Inform the Python interpreter NOT to create new local variable
    x=new_value

x=5  # Define variable x and assign value 5
change_x(4) # Change X to 4
print("x is: ",x)

# Change X to whatever you want without changing change_x function's code
change_x("Hello") # Change X to 4
print("x is: ",x)
