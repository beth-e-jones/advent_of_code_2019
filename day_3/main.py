# %%
import pandas as pd

# %%
# Set input datapath
DATAPATH = "input.txt"

# %%
# Read each individual line of the txt file as a list
with open(DATAPATH) as f:
    lines = f.readlines()

# %%
# Set the wires to correspond with txt file lines    
WIRE_1 = lines[0].split(",")
WIRE_2 = lines[1].split(",")

# %%
# Check lines allocated without error
print(WIRE_1)
print(WIRE_2)

#%%
# Confirm WIRE_1 steps stored as a list
type(WIRE_1)

# %%
# Use first character in each step to identify the direction of the step
for step in range (len(WIRE_1)):
    direction = WIRE_1[step] [0]
    # Check this by printing the direction
    print(direction)


# %%
def wire_1_journey():
    wire_1_x_axis = 0
    wire_1_y_axes = 0

    for step in WIRE_1:
        if direction == "R":
            #print(int(step[1:]))
            wire_1_x_axis = wire_1_x_axis + int(step[1:])
        elif direction == "L": 
            print(int(step[1:]))
            wire_1_x_axis = wire_1_x_axis - int(step[1:]) 
        elif direction == "U":
            print(int(step[1:]))
            wire_1_y_axes = wire_1_y_axes + int(step[1:])
        elif direction == "D":
            print(int(step[1:]))
            wire_1_y_axes = wire_1_y_axes - int(step[1:])

# this isn't working the numbers only go down WHY BETH

   # return (wire_1_x_axis, wire_1_y_axes)
            
# %%
wire_1_journey()

# %%

# for wire 1, 
# if instruction begins with R, add number to first number and print first 
#  number,if instruction begins with L, minus the number from the 
# second number and print it 
# if instruction begins with U, add number to second number, print 
# second number, if instruction begins with D, minus the number from the 
# second number and print it 

# This should lead to a printed path of where it;s been


# for wire 2, 
# if instruction begins with R, add number to first number and print first 
#  number,if instruction begins with L, minus the number from the 
# second number and print it 
# if instruction begins with U, add number to second number, print 
# second number, if instruction begins with D, minus the number from the 
# second number and print it 

# This should lead to a printed path of where it;s been

# consider .intersections method
# there is a python manhattan method 
# https://www.statology.org/manhattan-distance-python/



""""
https://www.w3schools.com/python/ref_file_readlines.asp
"""
# %%
